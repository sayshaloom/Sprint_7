import allure
import data

class TestCreateCourier:
    
    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self, api_client, courier_payload):
        response = api_client.create_courier(courier_payload)
        
        assert response.status_code == 201
        assert response.json() == data.SUCCESS_COURIER_CREATE

    @allure.title('Ошибка создания двух одинаковых курьеров')
    def test_create_courier_twice_error(self, api_client, courier_payload):
        api_client.create_courier(courier_payload)
        duplicate_response = api_client.create_courier(courier_payload)

        assert duplicate_response.status_code == 409
        assert duplicate_response.json() == data.ERROR_DUPLICATE_CREATE

    @allure.title('Ошибка создания курьера без обязательного поля login')
    def test_create_courier_without_login_error(self, api_client, courier_payload):
        del courier_payload['login']
        response = api_client.create_courier(courier_payload)
    
        assert response.status_code == 400
        assert response.json() == data.ERROR_MISSING_FIELDS_CREATE

    @allure.title('Ошибка создания курьера без обязательного поля password')
    def test_create_courier_without_password_error(self, api_client, courier_payload):
        del courier_payload['password']
        response = api_client.create_courier(courier_payload)
    
        assert response.status_code == 400
        assert response.json() == data.ERROR_MISSING_FIELDS_CREATE
