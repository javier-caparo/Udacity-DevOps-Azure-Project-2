import time
from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def index(self):
        self.client.get("https://jc-my-ml-app.azurewebsites.net/")

    @task(2)
    def predict(self):
        self.client.post("/predict",{
       "CHAS":{
          "0":0
       },
       "RM":{
          "0":6.575
       },
       "TAX":{
          "0":296.0
       },
       "PTRATIO":{
          "0":15.3
       },
       "B":{
          "0":396.9
       },
       "LSTAT":{
          "0":4.98
       }
    },
    headers="Content-Type: application/json")
