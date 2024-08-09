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


def generate_data_courier():
    return {
        'login': generate_login(),
        "password": generate_password(),
        "firstName": generate_first_name()
    }


headers = {"Content-type": "application/json"}
