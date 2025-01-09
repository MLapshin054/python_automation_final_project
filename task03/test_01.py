import requests
import yaml

with open("./config.yaml") as f:
    data = yaml.safe_load(f)

def test_user_profile(login):
    header = {"X-Auth-Token": login}
    response = requests.get(f"{data['address']}api/users/profile/{data['user_id']}", headers=header)
    response.raise_for_status()
    user_profile = response.json()
    assert user_profile['username'] == data["username"], "Username не соответствует ожидаемому значению."