import allure
import requests
from helpers import url


class Courier:
    @staticmethod
    @allure.step("Создать учетную запись курьера")
    def create_courier(data_courier):
        response = requests.post(url.CREATE_COURIER, json=data_courier)
        return response

    @staticmethod
    @allure.step("Получить логин курьера")
    def get_login_courier(login, password):
        login_response = requests.post(url.LOGIN_COURIER,
                                       json={'login': login, 'password': password}
                                       )
        return login_response

    @staticmethod
    @allure.step("Удалить учетную запись курьера")
    def delete_courier(courier_id):
        delete_response = requests.delete(f"{url.DELETE_COURIER}/{courier_id}")
        return delete_response
