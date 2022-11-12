import allure
from selenium import webdriver

from pages.main_page import MainPage


class TestFAQ:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')

    @allure.description('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    @allure.title('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    def test_first_accordion_element(self):
        main_page = MainPage(self.driver)
        main_page.click_first_accordion_element()
        assert main_page.get_first_accordion_panel_element_text() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.description('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    @allure.title('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    def test_second_accordion_element(self):
        main_page = MainPage(self.driver)
        main_page.click_second_accordion_element()
        assert main_page.get_second_accordion_panel_element_text() == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.description('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    @allure.title('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    def test_third_accordion_element(self):
        main_page = MainPage(self.driver)
        main_page.click_third_accordion_element()
        assert main_page.get_third_accordion_panel_element_text() == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.description('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    @allure.title('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    def test_fourth_accordion_element(self):
        main_page = MainPage(self.driver)
        main_page.click_fourth_accordion_element()
        assert main_page.get_fourth_accordion_panel_element_text() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.description('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    @allure.title('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    def test_fifth_accordion_element(self):
        main_page = MainPage(self.driver)
        main_page.click_fifth_accordion_element()
        assert main_page.get_fifth_accordion_panel_element_text() == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.description('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    @allure.title('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    def test_sixth_accordion_element(self):
        main_page = MainPage(self.driver)
        main_page.click_sixth_accordion_element()
        assert main_page.get_sixth_accordion_panel_element_text() == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.description('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    @allure.title('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    def test_seventh_accordion_element(self):
        main_page = MainPage(self.driver)
        main_page.click_seventh_accordion_element()
        assert main_page.get_seventh_accordion_panel_element_text() == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.description('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    @allure.title('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    def test_eighth_accordion_element(self):
        main_page = MainPage(self.driver)
        main_page.click_eighth_accordion_element()
        assert main_page.get_eighth_accordion_panel_element_text() == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
