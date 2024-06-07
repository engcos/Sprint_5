from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from locators import Locator

class TestConstructor:

    def test_transition_to_sauces_return_current_in_class(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        # Ожидание видимости кнопки "Соусы"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.SAUCESS_BUTTON)))
        sauces_button = driver.find_element(By.XPATH, Locator.SAUCESS_BUTTON)
        ActionChains(driver).move_to_element(sauces_button).click().perform()
        # Ожидание, что "Соусы" стали текущим разделом
        current_sauces_section = f"{Locator.PARENT_DIV_OF_SAUCESS_BUTTON[0]}{Locator.PARENT_DIV_OF_SAUCESS_BUTTON[1]}"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, current_sauces_section)))
        assert driver.find_element(By.XPATH, current_sauces_section) is not None

    def test_transition_to_fillings_return_current_in_class(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        # Ожидание видимости кнопки "Начинки"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.FILLINGS_BUTTON)))
        fillings_button = driver.find_element(By.XPATH, Locator.FILLINGS_BUTTON)
        ActionChains(driver).move_to_element(fillings_button).click().perform()
        # Ожидание, что "Начинки" стали текущим разделом
        current_fillings_section = f"{Locator.PARENT_DIV_OF_FILLINGS_BUTTON[0]}{Locator.PARENT_DIV_OF_FILLINGS_BUTTON[1]}"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, current_fillings_section)))
        assert driver.find_element(By.XPATH, current_fillings_section) is not None

    def test_transition_to_rolls_return_current_in_class(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        # Ожидание видимости кнопки "Булки"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locator.ROLLS_BUTTON)))
        rolls_button = driver.find_element(By.XPATH, Locator.ROLLS_BUTTON)
        ActionChains(driver).move_to_element(rolls_button).click().perform()
        # Ожидание, что "Булки" стали текущим разделом
        current_rolls_section = f"{Locator.PARENT_DIV_OF_ROLLS_BUTTON[0]}{Locator.PARENT_DIV_OF_ROLLS_BUTTON[1]}"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, current_rolls_section)))
        assert driver.find_element(By.XPATH, current_rolls_section) is not None
