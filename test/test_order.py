import allure
from selenium import webdriver

from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.description('Тест проверяет заказ самоката')
    @allure.title('Первый позитивный сценарий заказа самоката')
    def test_first_order(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.close_cookie()
        main_page.click_first_order_button()
        order_page = OrderPage(self.driver)
        order_page.set_name()
        order_page.set_surname()
        order_page.set_address()
        order_page.set_metro_station()
        order_page.set_phone_number()
        order_page.click_next_button()

        order_page.set_date()
        order_page.set_rental_period()
        order_page.click_black_checkbox()
        order_page.set_comment()
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.order_has_been_placed_text().startswith('Заказ оформлен')

    @allure.description('Тест проверяет заказ самоката')
    @allure.title('Второй позитивный сценарий заказа самоката')
    def test_second_order(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_second_order_button()
        order_page = OrderPage(self.driver)
        order_page.set_name()
        order_page.set_surname()
        order_page.set_address()
        order_page.set_metro_station()
        order_page.set_phone_number()
        order_page.click_next_button()

        order_page.set_date()
        order_page.set_rental_period()
        order_page.click_grey_checkbox()
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.order_has_been_placed_text().startswith('Заказ оформлен')

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
