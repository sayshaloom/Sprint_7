from faker import Faker
 
fake = Faker()
 
 
def generate_courier_payload():
    """Генерирует данные нового курьера (логин уникальный за счёт числового суффикса)"""
    return {
        "login": f"{fake.user_name()}_{fake.random_number(digits=5, fix_len=True)}",
        "password": fake.password(length=4),
        "firstName": fake.first_name()
    }
 
 
def delete_courier(api_client, payload):
    """Удаляет курьера по логину и паролю, если он был создан"""
    login_payload = {
        "login": payload["login"],
        "password": payload["password"]
    }
    login_response = api_client.login_courier(login_payload)
 
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        if courier_id:
            api_client.delete_courier(courier_id)
 