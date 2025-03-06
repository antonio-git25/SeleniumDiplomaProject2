import random
from datetime import time
import datetime
import time #for time sleep option

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Result_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    title_5 = "//h1[@class='result-component_result__title__9dGgE']"
    message = "//p[@class='result-component_result__text__PCLJU']"
    continue_buy = "//a[@class='result - component_result__link__wR0ua']"


    #Getters
    def get_title_5(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_5)))

    def get_message(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.message)))

    def get_continue_buy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_buy)))



    #Actions
    def print_result(self):
        print(self.get_title_5().text)
        msg = self.get_message().text
        print(msg[0:40])



    #Methods
    def check_current_location(self):
        Logger.add_start_step(method="check_current_location")
        time.sleep(3)
        url_5 = "https://ohotaktiv.ru/result/"
        get_url5 = self.driver.current_url
        assert url_5 == get_url5
        print(get_url5)
        # value_down = self.get_continue_buy().text
        # assert value_down == "Продолжить покупки"
        # print(value_down)
        Logger.add_end_step(url=self.driver.current_url, method="check_current_location")


    def show_results(self):
        Logger.add_start_step(method="show_results")
        self.print_result()
        time.sleep(2)
        Logger.add_end_step(url=self.driver.current_url, method="show_results")


    def make_screenshot(self, test_marker, page_marker):
        Logger.add_start_step(method="make_screenshot")
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M")
        name_screen = 'screen_' + test_marker + '_' + page_marker + '_' + now_date + '.png'
        # driver.save_screenshot(f"\\doc\\{name_screen}")
        self.driver.save_screenshot('C:\\Users\\Antonio\\PycharmProjects\\SeleniumDiplomaProject\\screen\\' + name_screen)
        Logger.add_end_step(url=self.driver.current_url, method="make_screenshot")




