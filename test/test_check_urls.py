import allure
from selenium import webdriver

from pages.dzen_page import DzenPage
from pages.main_page import MainPage


class TestCheckURLs:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')

    @allure.description('Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    @allure.title('Если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def test_scooter_logo(self):
        main_page = MainPage(self.driver)
        main_page.click_first_order_button()
        main_page.click_scooter_logo()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.description('Проверить: если нажать на логотип Яндекса, в новом окне откроется главная страница Яндекса.')
    @allure.title('Если нажать на логотип Яндекса, в новом окне откроется главная страница Яндекса.')
    def test_yandex_logo(self):
        main_page = MainPage(self.driver)
        main_page.click_yandex_logo()
        second_window = self.driver.window_handles[1]
        self.driver.switch_to.window(second_window)
        dzen_page = DzenPage(self.driver)
        dzen_page.wait_for_loading_page()
        assert self.driver.current_url.startswith('https://dzen.ru/?yredirect=true')

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
