import pytest
import helpers
from api_client.scooter_api import ScooterApi

@pytest.fixture(scope="session")
def api_client():
    """Фикстура предоставляет экземпляр клиента для всего тест-рана"""
    return ScooterApi()

@pytest.fixture
def courier_payload(api_client):
    """Данные нового курьера. Если тест создал курьера, фикстура удалит его после теста"""
    payload = helpers.generate_courier_payload()

    # тесту отдаём копию: тест может удалять из неё поля, а для очистки нужны исходные данные
    yield dict(payload)

    helpers.delete_courier(api_client, payload)

@pytest.fixture
def registered_courier(api_client):
    """Курьер, зарегистрированный на сервере. Эта же фикстура удаляет его после теста"""
    payload = helpers.generate_courier_payload()
    api_client.create_courier(payload)
 
    yield payload
 
    helpers.delete_courier(api_client, payload)
 