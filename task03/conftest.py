import pytest
import yaml
import requests

with open("./config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def login():
    login = requests.post(data["address"] + "gateway/login",
                          data={"username": data["username"], "password": data["password"]})
    token = login.json()["token"]
    return token
