import json
import requests
import jsonpath
from urllib.parse import urljoin
from library.config import Config
from library.config import TestData

class OrderOperations(TestData):
    order_id = None
    book = TestData.book

    def __init__(self, token):
        self.token = token

    def orders(self):
        endpoint = "/orders"
        url = urljoin(Config.BASE_URL, endpoint)
        auth = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=auth)
        res = json.loads(response.text)
        # print(res)
        return res

    def place_order(self):
        endpoint = "/orders"
        url = urljoin(Config.BASE_URL, endpoint)
        body = {"bookId": OrderOperations.book, "customerName": "John"}
        auth = {'Authorization': "Bearer " + self.token}
        response = requests.post(url, headers=auth, json=body)
        res = json.loads(response.text)
        # print(res)
        orders = jsonpath.jsonpath(res, "orderId")
        # print(orders)
        OrderOperations.order_id = orders[0]
        return res

    def get_order_details(self):
        endpoint = f"/orders/{OrderOperations.order_id}"
        url = urljoin(Config.BASE_URL, endpoint)
        auth = {'Authorization': "Bearer " + self.token}
        response = requests.get(url, headers=auth)
        res = json.loads(response.text)
        # print(res)
        return res

    def update_order(self):
        endpoint = f"/orders/{OrderOperations.order_id}"
        url = urljoin(Config.BASE_URL, endpoint)
        body = {"customerName": "UpdatedUser"}
        auth = {"Authorization": f"Bearer {self.token}"}
        response = requests.patch(url, headers=auth, json=body)
        # print(response)
        return response

    def del_order(self):
        endpoint = f"/orders/{OrderOperations.order_id}"
        url = urljoin(Config.BASE_URL, endpoint)
        auth = {"Authorization": f"Bearer {self.token}"}
        response = requests.delete(url, headers=auth)
        # print(response)
        return response