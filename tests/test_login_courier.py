import allure
import data
import pytest

class TestCourierLogin:

    @allure.title('Успешная авторизация курьера')
    def test_courier_login_success(self, api_client, registered_courier):
        
        payload = registered_courier
        
        # формируем тело запроса для логина (нужны только login и password)
        login_payload = {
            "login": payload["login"],
            "password": payload["password"]
        }
        
        # отправляем запрос на авторизацию
        response = api_client.login_courier(login_payload)
        
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title('Ошибка авторизации курьера с неверным паролем')
    def test_courier_login_with_wrong_password_error(self, api_client, registered_courier):
        
        payload = registered_courier
        
        # формируем тело запроса, но СПЕЦИАЛЬНО ПОРТИМ пароль
        login_payload = {
            "login": payload["login"],
            "password": f"{payload['password']}_wrong"
        }
        
        # отправляем запрос на логин
        response = api_client.login_courier(login_payload)
        
        assert response.status_code == 404
        assert response.json() == data.ERROR_NONEXISTENT_LOGIN_OR_WRONG_PASSWORD

    @allure.title('Ошибка авторизации курьера с несуществующим логином')
    def test_courier_login_with_wrong_login_error(self, api_client, registered_courier):

        payload = registered_courier
        
        # формируем тело запроса, но СПЕЦИАЛЬНО ПОРТИМ логин
        login_payload = {
            "login": f"{payload['login']}_nonexistent",
            "password": payload["password"]
        }
        
        # отправляем запрос на логин
        response = api_client.login_courier(login_payload)
        
        assert response.status_code == 404
        assert response.json() == data.ERROR_NONEXISTENT_LOGIN_OR_WRONG_PASSWORD

    @allure.title('Ошибка авторизации при отсутствии поля login')
    def test_courier_login_without_login_error(self, api_client, courier_payload):
        
        # готовим payload для логина и удаляем из него ключ login
        login_payload = {
            "login": courier_payload["login"],
            "password": courier_payload["password"]
        }
        del login_payload['login']
        
        # отправляем запрос без логина
        response = api_client.login_courier(login_payload)
        
        assert response.status_code == 400
        assert response.json() == data.ERROR_LOGIN_WITHOUT_LOGIN_OR_PASSWORD

    @allure.title('Ошибка авторизации при отсутствии поля password')
    @pytest.mark.xfail(reason="Бэкенд зависает при отправке запроса без пароля (известный баг)")
    def test_courier_login_without_password_error(self, api_client, courier_payload):
        # готовим payload для логина и удаляем из него ключ password
        login_payload = {
            "login": courier_payload["login"],
            "password": courier_payload["password"]
        }
        del login_payload['password']
        
        # отправляем запрос без пароля
        response = api_client.login_courier(login_payload)
        
        assert response.status_code == 400
        assert response.json() == data.ERROR_LOGIN_WITHOUT_LOGIN_OR_PASSWORD