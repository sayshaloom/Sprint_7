URL = 'https://qa-scooter.praktikum-services.ru'

# эндпоинты
CREATE_COURIER = '/api/v1/courier'
LOGIN_COURIER = '/api/v1/courier/login'
CREATE_ORDER = '/api/v1/orders'
GET_ORDERS_LIST = '/api/v1/orders'


# сообщение об успешном создании курьера
SUCCESS_COURIER_CREATE = {"ok": True}

# сообщения об ошибках при создании курьера
ERROR_MISSING_FIELDS_CREATE = {
  "code": 400,
  "message": "Недостаточно данных для создания учетной записи"
}

ERROR_DUPLICATE_CREATE = {
  "code": 409,
  "message": "Этот логин уже используется. Попробуйте другой."
}

# ошибка при логине с неверным логином/паролем
ERROR_NONEXISTENT_LOGIN_OR_WRONG_PASSWORD = {
  "code": 404,
  "message": "Учетная запись не найдена"
}

# ошибка при логине без логина или пароля
ERROR_LOGIN_WITHOUT_LOGIN_OR_PASSWORD = {
  "code": 400,
  "message":  "Недостаточно данных для входа"
}