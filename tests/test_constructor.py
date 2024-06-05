from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import Locator

class TestConstructor:

    def test_transition_to_sauces_return_current_in_class(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        # Ожидание видимости кнопки "Соусы"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.SAUCESS_BUTTON)))
        element = driver.find_element(By.XPATH, Locator.SAUCESS_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        # Ожидание, что "Соусы" стали текущим разделом
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.PARENT_DIV_OF_SAUCESS_BUTTON[0])))
        assert driver.find_element(By.XPATH, Locator.PARENT_DIV_OF_SAUCESS_BUTTON[0]).find_element(By.XPATH, Locator.PARENT_DIV_OF_SAUCESS_BUTTON[1]) is not None

    def test_transition_to_fillings_return_current_in_class(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        # Ожидание видимости кнопки "Начинки"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.FILLINGS_BUTTON)))
        element = driver.find_element(By.XPATH, Locator.FILLINGS_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        # Ожидание, что "Начинки" стали текущим разделом
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.PARENT_DIV_OF_FILLINGS_BUTTON[0])))
        assert driver.find_element(By.XPATH, Locator.PARENT_DIV_OF_FILLINGS_BUTTON[0]).find_element(By.XPATH, Locator.PARENT_DIV_OF_FILLINGS_BUTTON[1]) is not None

    def test_transition_to_rolls_return_current_in_class(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        # Ожидание видимости кнопки "Булки"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ROLLS_BUTTON)))
        element = driver.find_element(By.XPATH, Locator.ROLLS_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        # Ожидание, что "Булки" стали текущим разделом
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.PARENT_DIV_OF_ROLLS_BUTTON[0])))
        assert driver.find_element(By.XPATH, Locator.PARENT_DIV_OF_ROLLS_BUTTON[0]).find_element(By.XPATH, Locator.PARENT_DIV_OF_ROLLS_BUTTON[1]) is not None

