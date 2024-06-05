from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locator

class TestRegistration:

    def test_valid_mail_and_password_get_successful_registration(self, driver):
        # Константы
        USER = "Test User"
        MAIL = "test_user_5_001@yandex.ru"
        PASSWORD = "password123"

        # Переход на главную страницу и регистрация
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.REGISTRATION_BUTTON)))
        driver.find_element(By.XPATH, Locator.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.NAME_INPUT)))
        driver.find_element(By.XPATH, Locator.NAME_INPUT).send_keys(USER)
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys(MAIL)
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys(PASSWORD)
        driver.find_element(By.XPATH, Locator.REGISTRATION_COMMIT_BUTTON).click()

        # Проверка успешной регистрации и логина
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys(MAIL)
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys(PASSWORD)
        driver.find_element(By.XPATH, Locator.LOGIN_BUTTON).click()
        assert driver.find_element(By.XPATH, Locator.CREATE_ORDER_BUTTON) is not None

    def test_valid_mail_and_invalid_password_return_error(self, driver):
        # Константы
        USER = "Test User"
        MAIL = "test_user_5_001@yandex.ru"
        INVALID_PASSWORD = "12345"

        # Переход на главную страницу и регистрация
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.REGISTRATION_BUTTON)))
        driver.find_element(By.XPATH, Locator.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.NAME_INPUT)))
        driver.find_element(By.XPATH, Locator.NAME_INPUT).send_keys(USER)
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys(MAIL)
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys(INVALID_PASSWORD)
        driver.find_element(By.XPATH, Locator.REGISTRATION_COMMIT_BUTTON).click()

        # Проверка появления сообщения об ошибке
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, Locator.ERROR_LABEL)))
        assert driver.find_element(By.CSS_SELECTOR, Locator.ERROR_LABEL).text == 'Некорректный пароль'
