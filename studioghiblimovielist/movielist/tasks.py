import requests
from celery import shared_task
from movielist.models import Film, Person


@shared_task
def get_films_and_people():
    URL_PATH = "https://ghibliapi.herokuapp.com"
    films_fields = [
        "id",
        "title",
        "description",
        "director",
        "producer",
        "release_date",
        "rt_score",
    ]
    people_fields = ["id", "name", "gender", "films"]

    # I couldn't find anything related to pagination in the API description.
    # To be sure I got all the data I could
    films_response = requests.get(
        f"{URL_PATH}/films?limit=250&fields={','.join(films_fields)}"
    )
    people_response = requests.get(
        f"{URL_PATH}/people?limit=250&fields={','.join(people_fields)}"
    )

    for film in films_response.json():
        film_id = film.pop("id")
        Film.objects.update_or_create(
            uuid=film_id,
            defaults={key: film[key] for key in films_fields if key is not "id"},
        )

    for person_data in people_response.json():
        person, _ = Person.objects.update_or_create(
            uuid=person_data["id"],
            defaults={
                key: person_data[key]
                for key in people_fields
                if key not in {"id", "films"}
            },
        )
        for i in person_data["films"]:
            film_id = i.replace(f"{URL_PATH}/films/", "")
            try:
                person.films.add(Film.objects.get(uuid=film_id))
            except Film.DoesNotExist:
                continue
