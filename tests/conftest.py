import pytest
import json
import requests
import jsonpath
import random
from urllib.parse import urljoin
from library.config import Config

# @pytest.fixture(scope="session")

@pytest.fixture()
def authenticate():
    endpoint = "/api-clients/"
    num = random.randint(1, 100000)
    body = {"clientName": "Chandu", "clientEmail": f"Chandu+{num}@example.com"}
    response = requests.post(urljoin(Config.BASE_URL, endpoint), json=body)
    res = json.loads(response.text)
    token_list = jsonpath.jsonpath(res, "accessToken")
    token = token_list[0]
    # print(token)
    return token