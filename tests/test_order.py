import allure
import pytest

from api.order import Order
from helpers import data


@allure.feature("Создание заказа")
class TestOrder:
    @pytest.mark.parametrize('color',
                             [data.generate_order_data('BLACK'),
                              data.generate_order_data('GREY'),
                              data.generate_order_data('BLACK, GREY'),
                              data.generate_order_data('')])
    @allure.story("Успешное создание заказа")
    @allure.title("Создание заказа при указании одного из цветов, оба цвета, ни одного цвета. "
                  "Тело ответа содержит track ")
    def test_create_order_successful(self, color):
        response = Order.create_order(color)
        assert (response.status_code == 201
                and 'track' in response.json()), \
            f"Статус код {response.status_code}, track не найден в ответе"


@allure.feature("Получение списка заказов")
class TestGetOrderList:
    @allure.story("Успешное получение списка заказа")
    @allure.title("Проверка, что API возвращает список заказов. Список не пустой. В списке есть id")
    def test_get_order_list(self):
        response = Order.get_order_list()
        response_json = response.json()
        first_order = response_json['orders'][0]
        assert (response.status_code == 200
                and 'orders' in response_json
                and isinstance(response_json['orders'], list)
                and len(response_json['orders']) > 0
                and 'id' in first_order), (
            f"Ожидался статус код 200 и корректный список заказов с полем 'id', "
            f"но получили статус код {response.status_code}. "
            f"В ответе {response_json}"
        )
