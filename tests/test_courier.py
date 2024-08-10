import allure
import pytest
import requests

from helpers import url, data


@allure.feature("Courier")
class TestCreateCourier:
    @allure.story("Успешное создание учетной записи курьера")
    @allure.title("Создание учетной записи курьера со всеми полями или без поля firstName")
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

    @allure.story("Ошибка при создании учетной записи курьера без обязательных полей")
    @allure.title("Создание учетной записи курьера без обязательного поля")
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

    @allure.story("Ошибка при повторном создании учетной записи курьера с тем же логином")
    @allure.title("Попытка создания учетной записи курьера с уже существующим логином")
    def test_create_courier_repeat_login_error(self, create_and_delete_courier):
        data_courier = create_and_delete_courier

        response = requests.post(url.CREATE_COURIER, json=data_courier)
        assert response.status_code == 409 and response.json().get('message') == ('Этот логин уже используется. '
                                                                                  'Попробуйте другой.')


class TestLoginCourier:
    def test_login_courier_successful(self, create_and_delete_courier):
        data_courier = create_and_delete_courier

        login_response = requests.post(url.LOGIN_COURIER, json=data_courier)
        courier_id = login_response.json()['id']
        assert login_response.status_code == 200 and courier_id, "Courier ID not found in login response"

    @pytest.mark.parametrize("remove_field, expected_status_code, expected_message", [
        # Поле login отсутствует
        ("login", 400, "Недостаточно данных для входа"),
        # Поле password отсутствует
        ("password", 400, "Недостаточно данных для входа")
    ])
    def test_login_courier_no_required_field_error_1(self, create_and_delete_courier, remove_field, expected_status_code, expected_message):
        data_courier = create_and_delete_courier.copy()

        if remove_field in data_courier:
            data_courier.pop(remove_field)

        login_response = requests.post(url.LOGIN_COURIER, json=data_courier)

        assert login_response.status_code == expected_status_code and login_response.json().get('message') == expected_message

    def test_login_courier_no_required_field_error_2(self, create_and_delete_courier):
        data_courier = create_and_delete_courier

        data_courier.pop("password")

        login_response = requests.post(url.LOGIN_COURIER, json=data_courier)

        assert login_response.status_code == 400
