from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locator

class TestLogin:

    def test_login_from_main_page_successful(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ENTER_ACCOUNT)))
        driver.find_element(By.XPATH, Locator.ENTER_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys("test_user_5_001@yandex.ru")
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys("password123")
        driver.find_element(By.XPATH, Locator.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.CREATE_ORDER_BUTTON)))
        assert driver.find_element(By.XPATH, Locator.CREATE_ORDER_BUTTON).is_displayed()

    def test_login_from_account_button_successful(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys("test_user_5_001@yandex.ru")
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys("password123")
        driver.find_element(By.XPATH, Locator.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.CREATE_ORDER_BUTTON)))
        assert driver.find_element(By.XPATH, Locator.CREATE_ORDER_BUTTON).is_displayed()

    def test_login_from_registration_form_successful(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.REGISTRATION_BUTTON)))
        driver.find_element(By.XPATH, Locator.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ENTER_ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locator.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys("test_user_5_001@yandex.ru")
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys("password123")
        driver.find_element(By.XPATH, Locator.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.CREATE_ORDER_BUTTON)))
        assert driver.find_element(By.XPATH, Locator.CREATE_ORDER_BUTTON).is_displayed()

    def test_login_from_forgot_password_form_successful(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.FORGOT_PASSWORD_BUTTON)))
        driver.find_element(By.XPATH, Locator.FORGOT_PASSWORD_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ENTER_ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locator.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys("test_user_5_001@yandex.ru")
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys("password123")
        driver.find_element(By.XPATH, Locator.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.CREATE_ORDER_BUTTON)))
        assert driver.find_element(By.XPATH, Locator.CREATE_ORDER_BUTTON).is_displayed()