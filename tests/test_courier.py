import json

import requests

from helpers import url


def test_create_courier_successful():
    payload = {
        "login": "ninja12ffwfew",
        "password": "12345",
        "firstName": "saske1"
    }
    payload_str = json.dumps(payload)
    headers = {"Content-type": "application/json"}
    response = requests.post(url.CREATE_COURIER,
                             data=payload_str,
                             headers=headers)

    assert response.status_code == 201 and response.json() == {'ok': True}
