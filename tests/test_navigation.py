from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locator

class TestNavigation:

    def test_navigation_from_main_page_to_account_find_exit_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys("test_user_5_001@yandex.ru")
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys("password123")
        driver.find_element(By.XPATH, Locator.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.EXIT_BUTTON)))
        assert driver.find_element(By.XPATH, Locator.EXIT_BUTTON) is not None

    def test_navigation_from_account_page_to_constructor_find_place_to_order_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys("test_user_5_001@yandex.ru")
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys("password123")
        driver.find_element(By.XPATH, Locator.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.CONSTRUCTOR_BUTTON)))
        driver.find_element(By.XPATH, Locator.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.CREATE_ORDER_BUTTON)))
        assert driver.find_element(By.XPATH, Locator.CREATE_ORDER_BUTTON) is not None

    def test_navigation_from_account_page_to_stellar_button_find_place_to_order_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locator.EMAIL_INPUT).send_keys("test_user_5_001@yandex.ru")
        driver.find_element(By.XPATH, Locator.PASS_INPUT).send_keys("password123")
        driver.find_element(By.XPATH, Locator.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locator.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.STELLAR_BURGET_BUTTON[0])))
        driver.find_element(By.XPATH, Locator.STELLAR_BURGET_BUTTON[0]).find_element(By.XPATH, Locator.STELLAR_BURGET_BUTTON[1]).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.CREATE_ORDER_BUTTON)))
        assert driver.find_element(By.XPATH, Locator.CREATE_ORDER_BUTTON) is not None