import allure
import pytest
import requests

from helpers import url, data


@allure.feature("Создание заказа")
class TestCreateOrder:
    @pytest.mark.parametrize('color',
                             [data.generate_order_data('BLACK'),
                              data.generate_order_data('GREY'),
                              data.generate_order_data('BLACK, GREY'),
                              data.generate_order_data('')])
    @allure.story("Успешное создание заказа")
    @allure.title("Создание заказа при указании одного из цветов, оба цвета, ни одного цвета. "
                  "Тело ответа содержит track ")
    def test_create_order_successful(self, color):
        response = requests.post(url.CREATE_ORDER, json=color)
        assert (response.status_code == 201
                and 'track' in response.json()), \
            f"Статус код {response.status_code}, track не найден в ответе"
