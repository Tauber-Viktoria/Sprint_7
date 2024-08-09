import requests

from helpers import url, data


class TestCreateCourier:

    def test_create_courier_successful(self):
        data_courier = data.generate_data_courier()
        response = requests.post(url.CREATE_COURIER,
                                 json=data_courier)

        assert response.status_code == 201 and response.json() == {'ok': True}

        login_response = requests.post(url.LOGIN_COURIER,
                                       json={'login': data_courier['login'], 'password': data_courier['password']},)

        assert login_response.status_code == 200, f"Expected status code 200, but got {login_response.status_code}"
        courier_id = login_response.json().get('id')
        assert courier_id, "Courier ID not found in login response"

        delete_response = requests.delete(f"{url.DELETE_COURIER}/{courier_id}")
        assert delete_response.status_code == 200
