import random
import string

class TestData:
    # test_registration data
    USER = "Test User"
    PASSWORD = "password123"
    INVALID_PASSWORD = "12345"
    # test_login Data
    USER_EMAIL = "test_user_5_001@yandex.ru"
    USER_PASSWORD = "password123"
    INVALID_PASSWORD = "invalidpassword"

    @staticmethod
    def generate_email():
        domain = "@yandex.ru"
        local_part = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return local_part + domain