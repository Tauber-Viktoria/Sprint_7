import pytest
import requests

from helpers import url, data


class TestCreateCourier:
    @pytest.mark.parametrize("data_courier, expected_status_code, expected_response", [
        (data.generate_data_courier(), 201, {'ok': True}),  # Все поля переданы
        (data.generate_data_courier(include_first_name=False), 201, {'ok': True})  # Поле firstName отсутствует
    ])
    def test_create_courier_successful(self, data_courier, expected_status_code, expected_response):
        response = requests.post(url.CREATE_COURIER, json=data_courier)

        assert response.status_code == expected_status_code and response.json() == expected_response

        login_response = requests.post(url.LOGIN_COURIER,
                                       json={'login': data_courier['login'],
                                             'password': data_courier['password']}
                                       )
        courier_id = login_response.json().get('id')
        requests.delete(f"{url.DELETE_COURIER}/{courier_id}")

    @pytest.mark.parametrize("data_courier, expected_status_code, expected_response", [
        # Поле login отсутствует
        (data.generate_data_courier(include_first_login=False), 400, {'Недостаточно данных для создания '
                                                                      'учетной записи'}),
        # Поле password отсутствует
        (data.generate_data_courier(include_first_password=False), 400, {'Недостаточно данных для создания '
                                                                         'учетной записи'})
    ])
    def test_create_courier_no_required_field_error(self, data_courier, expected_status_code, expected_response):
        response = requests.post(url.CREATE_COURIER, json=data_courier)

        assert response.status_code == expected_status_code and response.json().get('message') == expected_response

    def test_create_courier_repeat_login_error(self, create_and_delete_courier):
        data_courier = create_and_delete_courier

        response = requests.post(url.CREATE_COURIER, json=data_courier)
        assert response.status_code == 409 and response.json().get('message') == ('Этот логин уже используется. '
                                                                                  'Попробуйте другой.')
