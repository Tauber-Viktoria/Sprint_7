from faker import Faker

fake = Faker("ru_RU")


def generate_login():
    login = fake.first_name()
    return login


def generate_password():
    password = fake.password()
    return password


def generate_first_name():
    first_name = fake.first_name()
    return first_name


def generate_data_courier(include_first_login=True, include_first_password=True, include_first_name=True):
    data_courier = {}
    if include_first_login:
        data_courier['login'] = generate_login()
    if include_first_password:
        data_courier['password'] = generate_password()
    if include_first_name:
        data_courier['firstName'] = generate_first_name()

    return data_courier


def generate_order_data(color):
    order_data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [color]
    }
    return order_data
