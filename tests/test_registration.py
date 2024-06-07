import sys
import os
import logging
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data import TestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locator

logging.basicConfig(level=logging.INFO)

class TestRegistration:

    def test_valid_mail_and_password_get_successful_registration(self, driver):
        USER = TestData.USER
        MAIL = TestData.generate_email()
        PASSWORD = TestData.PASSWORD

        logging.info("Начало теста: test_valid_mail_and_password_get_successful_registration")
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

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys(MAIL)
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys(PASSWORD)
        driver.find_element(By.XPATH, Locator.LOGIN_BUTTON).click()

        # Добавим ожидание для появления кнопки создания заказа
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, Locator.CREATE_ORDER_BUTTON)))

        # Проверка наличия кнопки создания заказа
        assert driver.find_element(By.XPATH, Locator.CREATE_ORDER_BUTTON) is not None

        logging.info("Тест завершен успешно: test_valid_mail_and_password_get_successful_registration")

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