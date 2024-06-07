from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locator


class TestLogout:

    def test_exit_from_account_page_and_transition_to_main_page_return_enter_account_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        self.login(driver, "test_user_5_001@yandex.ru", "password123")
        self.navigate_to_account_and_logout(driver)
        self.verify_logout_and_navigation(driver)

    def login(self, driver, email, password):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.EMAIL_INPUT)))
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys(email)
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys(password)
        driver.find_element(By.XPATH, Locator.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))

    def navigate_to_account_and_logout(self, driver):
        driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.EXIT_BUTTON)))
        driver.find_element(By.XPATH, Locator.EXIT_BUTTON).click()

    def verify_logout_and_navigation(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.STELLAR_BURGET_BUTTON[0])))
        logo_element = driver.find_element(By.XPATH, Locator.STELLAR_BURGET_BUTTON[0]).find_element(By.XPATH,Locator.STELLAR_BURGET_BUTTON[1])
        driver.execute_script("arguments[0].click();", logo_element)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.CREATE_ORDER_BUTTON)))
        assert driver.find_element(By.XPATH, Locator.CREATE_ORDER_BUTTON) is not None
