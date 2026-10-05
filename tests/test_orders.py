import pytest
import allure

class TestOrder:

    @allure.title('Успешное создание заказа')
    @pytest.mark.parametrize('colors', [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_success(self, api_client, colors):
        order_payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2026-06-06",
            "comment": "Saske, come back to Konoha"
        }
        
        # добавляем текущий цвет из параметризации
        order_payload['color'] = colors
       
        response = api_client.create_order(order_payload)

        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title('Успешное получение списка заказов')
    def test_get_orders_list_success(self, api_client):
        
        response = api_client.get_orders_list()
        
        assert response.status_code == 200
        assert "orders" in response.json()