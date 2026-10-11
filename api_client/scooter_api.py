import allure
import data
import requests

class ScooterApi:

    @allure.step('Отправка запроса на создание курьера')
    def create_courier(self, payload):
        return requests.post(f"{data.URL}{data.CREATE_COURIER}", json=payload, timeout=10)

    @allure.step('Отправка запроса на авторизацию курьера')
    def login_courier(self, payload):
        return requests.post(f"{data.URL}{data.LOGIN_COURIER}", json=payload, timeout=10)

    @allure.step('Отправка запроса на удаление курьера с ID: {courier_id}')
    def delete_courier(self, courier_id):
        return requests.delete(f"{data.URL}{data.CREATE_COURIER}/{courier_id}", timeout=10)

    @allure.step('Отправка запроса на создание заказа')
    def create_order(self, payload):
        return requests.post(f"{data.URL}{data.CREATE_ORDER}", json=payload, timeout=10)

    @allure.step('Отправка запроса на получение списка заказов')
    def get_orders_list(self):
        return requests.get(f"{data.URL}{data.GET_ORDERS_LIST}", timeout=30)