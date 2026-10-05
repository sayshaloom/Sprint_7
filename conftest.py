import pytest
from faker import Faker
from api_client.scooter_api import ScooterApi

fake = Faker()

@pytest.fixture(scope="session")
def api_client():
    """Фикстура предоставляет экземпляр клиента для всего тест-рана"""
    return ScooterApi()

@pytest.fixture
def courier_payload():
    """Генерация данных"""
    return {
        "login": fake.user_name(),
        "password": fake.password(length=4),
        "firstName": fake.first_name()
    }

@pytest.fixture
def registered_courier(api_client, courier_payload, cleanup_courier):
    """4. Фикстура регистрации. Сама ничего не удаляет, 
    а просто делегирует (передает) эту задачу в cleanup_courier.
    """
    # Регистрируем курьера на сервере через клиент
    api_client.create_courier(courier_payload)
    
    # Кладем его данные в фикстуру-дворник (в список couriers_to_delete)
    cleanup_courier.append(courier_payload)
    
    # Отдаем готового курьера в тесты
    yield courier_payload

@pytest.fixture
def cleanup_courier(api_client):
    """3. ЕДИНСТВЕННОЕ МЕСТО С КОДОМ УДАЛЕНИЯ (Наша корзина).
    Принимает фикстуру api_client, чтобы отправлять запросы логина и удаления.
    """
    couriers_to_delete = []
    
    yield couriers_to_delete  # Отдаем список в тесты или в другие фикстуры
    
    # ПОСЛЕ ТЕСТА: Код очистки
    for payload in couriers_to_delete:
        login_payload = {
            "login": payload["login"], 
            "password": payload["password"]
        }
        login_response = api_client.login_courier(login_payload)
        
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            if courier_id:
                api_client.delete_courier(courier_id)