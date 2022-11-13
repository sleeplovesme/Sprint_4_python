import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:
    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    scooter_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    order_button = [By.CLASS_NAME, 'Button_Button__ra12g']
    cookie_button = [By.ID, 'rcc-confirm-button']

    first_accordion_element = [By.ID, 'accordion__heading-0']
    second_accordion_element = [By.ID, 'accordion__heading-1']
    third_accordion_element = [By.ID, 'accordion__heading-2']
    fourth_accordion_element = [By.ID, 'accordion__heading-3']
    fifth_accordion_element = [By.ID, 'accordion__heading-4']
    sixth_accordion_element = [By.ID, 'accordion__heading-5']
    seventh_accordion_element = [By.ID, 'accordion__heading-6']
    eighth_accordion_element = [By.ID, 'accordion__heading-7']

    first_accordion_panel_element = [By.ID, 'accordion__panel-0']
    second_accordion_panel_element = [By.ID, 'accordion__panel-1']
    third_accordion_panel_element = [By.ID, 'accordion__panel-2']
    fourth_accordion_panel_element = [By.ID, 'accordion__panel-3']
    fifth_accordion_panel_element = [By.ID, 'accordion__panel-4']
    sixth_accordion_panel_element = [By.ID, 'accordion__panel-5']
    seventh_accordion_panel_element = [By.ID, 'accordion__panel-6']
    eighth_accordion_panel_element = [By.ID, 'accordion__panel-7']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать на лого яндекса')
    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

    @allure.step('Нажать на лого самоката')
    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()

    @allure.step('Нажать на первую кнопку Заказать')
    def click_first_order_button(self):
        self.driver.find_elements(*self.order_button)[0].click()

    @allure.step('Нажать на вторую кнопку Заказать')
    def click_second_order_button(self):
        self.driver.find_elements(*self.order_button)[2].click()

    @allure.step('Нажать на первый элемент аккордиона')
    def click_first_accordion_element(self):
        # скролл до последнего элемента аккордиона - иначе тест падает,
        # т.к. 1ый элемент перекрывается картинкой scooter.png
        last_element = self.driver.find_element(*self.eighth_accordion_element)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.first_accordion_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Нажать на второй элемент аккордиона')
    def click_second_accordion_element(self):
        element = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.second_accordion_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Нажать на третий элемент аккордиона')
    def click_third_accordion_element(self):
        element = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.third_accordion_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Нажать на четвертый элемент аккордиона')
    def click_fourth_accordion_element(self):
        element = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.fourth_accordion_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Нажать на пятый элемент аккордиона')
    def click_fifth_accordion_element(self):
        element = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.fifth_accordion_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Нажать на шестой элемент аккордиона')
    def click_sixth_accordion_element(self):
        element = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.sixth_accordion_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Нажать на седьмой элемент аккордиона')
    def click_seventh_accordion_element(self):
        element = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.seventh_accordion_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Нажать на восьмой элемент аккордиона')
    def click_eighth_accordion_element(self):
        element = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.eighth_accordion_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Получить текст первого элемента аккордиона')
    def get_first_accordion_panel_element_text(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.first_accordion_panel_element)).text

    @allure.step('Получить текст второго элемента аккордиона')
    def get_second_accordion_panel_element_text(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.second_accordion_panel_element)).text

    @allure.step('Получить текст третьего элемента аккордиона')
    def get_third_accordion_panel_element_text(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.third_accordion_panel_element)).text

    @allure.step('Получить текст четвертого элемента аккордиона')
    def get_fourth_accordion_panel_element_text(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.fourth_accordion_panel_element)).text

    @allure.step('Получить текст пятого элемента аккордиона')
    def get_fifth_accordion_panel_element_text(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.fifth_accordion_panel_element)).text

    @allure.step('Получить текст шестого элемента аккордиона')
    def get_sixth_accordion_panel_element_text(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.sixth_accordion_panel_element)).text

    @allure.step('Получить текст седьмого элемента аккордиона')
    def get_seventh_accordion_panel_element_text(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.seventh_accordion_panel_element)).text

    @allure.step('Получить текст восьмого элемента аккордиона')
    def get_eighth_accordion_panel_element_text(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(self.eighth_accordion_panel_element)).text

    @allure.step('Закрыть куки')
    def close_cookie(self):
        self.driver.find_element(*self.cookie_button).click()
