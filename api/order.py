import allure
import requests
from helpers import url


class Order:
    @staticmethod
    @allure.step("Создать заказ")
    def create_order(order_data):
        response = requests.post(url.CREATE_ORDER, json=order_data)
        return response

    @staticmethod
    @allure.step("Получить список заказов")
    def get_order_list():
        response = requests.get(url.LIST_ORDERS)
        return response
