import json
from pprint import pprint
from locust import HttpUser, task, between
from locust_plugins.csvreader import CSVReader, CSVDictReader

# ssn_reader = CSVReader("data.csv")
# print(ssn_reader.file)
#
#
# pprint(vars(ssn_reader))
# # cust=next(ssn_reader)
# # print(cust)
# #
# # ab= CSVDictReader("data.csv")
# # for i in ab:
# #      print(i)
# # #
# #

payload = {
    "name": "morpheus",
    "job": "leader"
}
payload = json.dumps(payload)
# print(payload)
url = "https://reqres.in/api/users"
geturl ="https://reqres.in/api/users/2"


class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    @task(1)
    def reqresget(self):
        response = self.client.get(geturl)
        print(response.status_code)
        print(response.json())

    @task(3)
    def reqrespost(self):
        response = self.client.post(url, payload)
        res = response.json()
        print(res)





    # def on_start(self):
    #     """ on_start is called when a Locust start before any task is scheduled """
    #     pass
    #
    # def on_stop(self):
    #     """ on_stop is called when the TaskSet is stopping """
    #     pass
    #
