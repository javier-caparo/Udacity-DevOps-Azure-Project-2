import time
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    # @task
    # def index_page(self):
    #     self.client.get(url="/hello")

    @task
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
