from datetime import time
import datetime
import time #for time sleep option

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Smoothbore_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    title_2 = "//h1[@class='catalog_title__lU65A']"
    price_from = "//input[@data-input='price_from']"
    price_to = "//input[@data-input='price_to']"
    calibr_down = "//button[@id=':r2:']"
    calibr_input = "//input[@id='kalibr_2-filter']"
    calibr_chbox = "//label[contains(text(),'12x76')]"
    type_action_down = "//button[@id=':r5:']"
    type_action_chbox = "//label[contains(text(),'Полуавтомат газоотводный')]"
    shotgun = "//button[@title='Купить Ружье ВЕПРЬ-12 Молот 12/76 L=430']"
    basket = "//a[@title='Корзина']"



    #Getters
    def get_title_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_2)))

    def get_price_from(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_from)))

    def get_price_to(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_to)))

    def get_calibr_down(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.calibr_down)))

    def get_calibr_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.calibr_input)))

    def get_calibr_chbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.calibr_chbox)))

    def get_type_action_down(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_action_down)))

    def get_type_action_chbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_action_chbox)))

    def get_shotgun(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shotgun)))

    def get_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket)))



    #Actions
    def set_price_from(self):
        self.get_price_from().send_keys("50000")
        self.get_price_from().send_keys(Keys.RETURN)
        time.sleep(1)
        print("Set minimum price: 50000 RUB")

    def set_price_to(self):
        self.get_price_to().send_keys("150000")
        self.get_price_to().send_keys(Keys.RETURN)
        time.sleep(1)
        print("Set maximum price: 150000 RUB")

    def set_calibr(self):
        time.sleep(2)
        self.get_calibr_down().click()
        time.sleep(1)
        self.get_calibr_input().send_keys("12x76")
        self.get_calibr_input().send_keys(Keys.RETURN)
        time.sleep(1)
        self.get_calibr_chbox().click()
        time.sleep(1)
        print("Set calibr: 12x76")

    def set_type_action(self):
        self.get_type_action_down().click()
        time.sleep(1)
        self.get_type_action_chbox().click()
        time.sleep(1)
        print("The desired operating principle: gas-operated machine")

    def click_shotgun(self):
        self.get_shotgun().click()
        print("Choose shotgun: Ружье ВЕПРЬ-12 Молот 12/76 L=430")
        time.sleep(10)

    def set_basket(self):
        num = self.get_basket().text
        print(f"Basket has {num} stuff")
        self.get_basket().click()
        time.sleep(3)
        print("Navigation into basket")



    #Methods
    def check_current_location(self):
        Logger.add_start_step(method="check_current_location")
        time.sleep(3)
        url_2 = "https://ohotaktiv.ru/catalog/gladkostvolnoe-oruzhie/"
        get_url2 = self.driver.current_url
        assert url_2 == get_url2
        print(get_url2)
        value_header = self.get_title_2().text
        assert value_header == "Гладкоствольное оружие"
        print(value_header)
        Logger.add_end_step(url=self.driver.current_url, method="check_current_location")


    def set_product_filters(self):
        Logger.add_start_step(method="set_product_filters")
        print("Set filter for price")
        self.driver.execute_script("window.scrollTo(0, 250)")
        time.sleep(1)
        self.set_price_from()
        self.set_price_to()

        print("Set filter for calibr")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 450)")
        time.sleep(1)
        self.set_calibr()

        print("Set filter for type of action")
        self.driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(1)
        self.set_type_action()
        Logger.add_end_step(url=self.driver.current_url, method="set_product_filters")


    def choose_product(self):
        Logger.add_start_step(method="choose_product")
        print("Select shotgun")
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(1)
        self.click_shotgun()
        time.sleep(12)
        self.get_screenshot("smoothbore-gun","catalog")
        Logger.add_end_step(url=self.driver.current_url, method="choose_product")


    def click_basket(self):
        Logger.add_start_step(method="click_basket")
        self.set_basket()
        Logger.add_end_step(url=self.driver.current_url, method="click_basket")