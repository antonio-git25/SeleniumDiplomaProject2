from datetime import time
import datetime
import time #for time sleep option

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Basket_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    title_3 = "//h1[@class='cart_title__W1iO7']"
    stuff_name = "//p[@class='name_name__tPObX']"
    stuff_code = "//p[@class='name_code__zoqsy']"
    current_price = "//p[@class='price_price__p0Bbk']"
    old_price = "//p[@class='price_priceOld__35f7z']"
    confirmation_bt = "//button[@type='submit']"
    missed_bt = "//a[@class='enter_buttonAction__I8rhp']"
    up_value = "(//button[@class='counter_counter__7scKW'])[2]"
    num_value = "//input[@class='counter_counterInput__juAkN']"


    #Getters
    def get_title_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_3)))

    def get_stuff_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.stuff_name)))

    def get_stuff_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.stuff_code)))

    def get_current_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.current_price)))

    def get_old_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.old_price)))

    def get_confirmation_bt(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirmation_bt)))

    def get_missed_bt(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.missed_bt)))

    def get_up_value(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.up_value)))

    def get_num_value(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.num_value)))



    #Actions
    def click_confirm(self):
        self.get_confirmation_bt().click()
        time.sleep(2)
        print("Start confirmation process")

    def click_missed(self):
        self.get_missed_bt().click()

    def increase_stuff(self):
        self.get_up_value().click()
        time.sleep(1)

    def show_stuff_value(self):
        count = self.get_num_value().text
        print("Ammount of bullets: ", count)



    #Methods
    def check_current_location(self):
        Logger.add_start_step(method="check_current_location")
        time.sleep(3)
        url_3 = "https://ohotaktiv.ru/cart/"
        get_url3 = self.driver.current_url
        assert url_3 == get_url3
        print(get_url3)
        value_header = self.get_title_3().text
        assert value_header == "Корзина"
        print(value_header)
        Logger.add_end_step(url=self.driver.current_url, method="check_current_location")


    def click_increase_stuff(self):
        Logger.add_start_step(method="click_increase_stuff")
        print("Increase the bullet")
        for i in range(0, 10):
            self.increase_stuff()
            time.sleep(1)
        Logger.add_end_step(url=self.driver.current_url, method="click_increase_stuff")


    def stuff_value(self):
        Logger.add_start_step(method="stuff_value")
        self.show_stuff_value()
        Logger.add_end_step(url=self.driver.current_url, method="stuff_value")


    def print_basket_info(self):
        Logger.add_start_step(method="print_basket_info")
        print(self.get_stuff_name().text)
        print(self.get_stuff_code().text)
        print(self.get_current_price().text)
        try:
            print(self.get_old_price().text)
        except TimeoutException:
            pass
        Logger.add_end_step(url=self.driver.current_url, method="print_basket_info")


    def confirmation(self):
        Logger.add_start_step(method="confirmation")
        self.click_confirm()
        self.click_missed()
        time.sleep(3)
        Logger.add_end_step(url=self.driver.current_url, method="confirmation")


    def make_screenshot(self, test_marker, page_marker):
        Logger.add_start_step(method="make_screenshot")
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M")
        name_screen = 'screen_' + test_marker + '_' + page_marker + '_' + now_date + '.png'
        # driver.save_screenshot(f"\\doc\\{name_screen}")
        self.driver.save_screenshot('C:\\Users\\Antonio\\PycharmProjects\\SeleniumDiplomaProject\\screen\\' + name_screen)
        Logger.add_end_step(url=self.driver.current_url, method="make_screenshot")




