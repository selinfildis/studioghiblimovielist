from django.test import RequestFactory, TestCase
from unittest.mock import patch, Mock
from movielist.tasks import get_films_and_people
from movielist.models import Film, Person
import uuid


class HomePageTest(TestCase):
    def test_get_works(self):
        resp = self.client.get("/movies/")
        self.assertEqual(resp.status_code, 200)


class SyncTaskTest(TestCase):
    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        film_id = str(uuid.uuid4())
        if "people" in args[0]:
            return MockResponse(
                [
                    {
                        "id": str(uuid.uuid4()),
                        "name": "melis",
                        "gender": "female",
                        "films": [f"https://ghibliapi.herokuapp.com/films/{film_id}"],
                    }
                ],
                200,
            )
        elif "films" in args[0]:
            return MockResponse(
                [
                    {
                        "id": film_id,
                        "title": "test",
                        "description": "test",
                        "director": "selin",
                        "producer": "selin",
                        "release_date": 1995,
                        "rt_score": 95,
                    }
                ],
                200,
            )

        return MockResponse(None, 404)

    @patch("requests.get", side_effect=mocked_requests_get)
    def test_task_works(self, requests):
        mock = Mock()

        requests.get.return_value.json.return_value = mock
        get_films_and_people()
        self.assertEqual(Film.objects.count(), 1)
        self.assertEqual(Person.objects.count(), 1)
        film = Film.objects.last()
        self.assertEqual(film.title, "test")
        self.assertEqual(film.description, "test")
        self.assertEqual(film.director, "selin")
        self.assertEqual(film.producer, "selin")
        self.assertEqual(film.release_date, 1995)
        self.assertEqual(film.rt_score, 95)

        person = Person.objects.last()
        self.assertEqual(person.name, "melis")
        self.assertEqual(person.gender, "female")
