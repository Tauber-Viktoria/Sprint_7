import pytest
import requests

from helpers import url, data


@pytest.fixture
def create_and_delete_courier():
    data_courier = data.generate_data_courier()
    requests.post(url=url.CREATE_COURIER, json=data_courier)

    login_response = requests.post(url=url.LOGIN_COURIER,
                                   json={
                                       'login': data_courier['login'],
                                       'password': data_courier['password']}
                                   )
    courier_id = login_response.json()['id']

    yield data_courier

    requests.delete(url=f'{url.DELETE_COURIER}/{courier_id}')
