import requests


def get_films_and_people():
    URL_PATH = 'https://ghibliapi.herokuapp.com'
    films_fields = 'id,title,description,director,producer,release_date,rt_score'
    people_fields = 'id,name,gender,films'

    # I couldn't find anything related to pagination in the API description.
    # To be sure I got all the data I could
    films_response = requests.get(f'{URL_PATH}/films?limit=250&fields={films_fields}')
    people_response = requests.get(f'{URL_PATH}/people?limit=250&fields={people_fields}')

    dict_of_films = {}
    for i in films_response.json():
        i['people'] = []
        dict_of_films[i['id']] = i

    for ppl in people_response.json():
        for i in ppl['films']:
            film_id = i.replace(f'{URL_PATH}/films/', '')
            dict_of_films[film_id]['people'].append(ppl)
        del ppl['films']

    return [v for _, v in dict_of_films.items()]
