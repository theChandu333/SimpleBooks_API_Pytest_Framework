import json
import requests
from urllib.parse import urljoin
from library.config import Config

class BookOperations:
    def get_status(self):
        endpoint = "/status"
        response = requests.get(urljoin(Config.BASE_URL, endpoint))
        res = json.loads(response.text)
        # print(res)
        return res

    def get_all_books(self):
        endpoint = "/books"
        response = requests.get(urljoin(Config.BASE_URL, endpoint))
        res = json.loads(response.text)
        # print(res)
        return res

    def get_book(self, book_id):
        endpoint = f"/books/{book_id}"
        response = requests.get(urljoin(Config.BASE_URL, endpoint))
        res = json.loads(response.text)
        # print(res)
        return res
