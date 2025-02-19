from locust import HttpUser, task

class UserBehavior(HttpUser):
    @task
    def test_homepage(self):
        self.client.get("/")



