import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class DzenPage:
    find_button = [By.XPATH, "//div[contains(text(), 'Удобный и быстрый Яндекс.Браузер')]"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание загрузки страницы')
    def wait_for_loading_page(self):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.find_button))
