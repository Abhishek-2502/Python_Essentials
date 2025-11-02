from locust import HttpUser, task

class ApacheUser(HttpUser):
    @task
    def index(self):
        self.client.get("/")


# To install Locust
# pip install locust

# To Run
# python -m locust -f locust_traffic.py --host url_of_your_application
# python -m locust -f locust_traffic.py --host http://127.0.0.1:8000/