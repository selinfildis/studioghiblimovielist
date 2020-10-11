from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(2, 3)

    @task
    def index_page(self):
        self.client.get("/movies/")
