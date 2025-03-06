from datetime import time
import datetime
import time #for time sleep option

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Firearms_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    title_1 = "//h1[@class='catalog_title__lU65A']"
    smoothbore_gun = "//*[@id='main']/div/section/div/div[1]/div[2]/div/div/a[2]"
    rifled_gun =     "//*[@id='main']/div/section/div/div[1]/div[2]/div/div/a[3]"
    traumatic_gun =  "//*[@id='main']/div/section/div/div[1]/div[2]/div/div/a[4]"


    #Getters
    def get_title_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_1)))

    def get_smoothbore_gun(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smoothbore_gun)))

    def get_rifled_gun(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.rifled_gun)))

    def get_traumatic_gun(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.traumatic_gun)))


    #Actions
    def click_smoothbore_gun(self):
        self.get_smoothbore_gun().click()
        time.sleep(1)
        print("catalog -> firearms -> smoothbore guns")

    def click_rifled_gun(self):
        self.get_rifled_gun().click()
        time.sleep(1)
        print("catalog -> firearms -> rifled guns")

    def click_traumatic_gun(self):
        self.get_traumatic_gun().click()
        time.sleep(1)
        print("catalog -> firearms -> traumatic guns")


    #Methods
    def check_current_location(self):
        Logger.add_start_step(method="check_current_location")
        time.sleep(3)
        url_1 = "https://ohotaktiv.ru/catalog/ognestrelnoe_oruzhie/"
        get_url1 = self.driver.current_url
        assert url_1 == get_url1
        print(get_url1)
        value_header = self.get_title_1().text
        assert value_header == "Огнестрельное оружие"
        print(value_header)
        Logger.add_end_step(url=self.driver.current_url, method="check_current_location")

    def select_smoothbore_gun(self):
        Logger.add_start_step(method="select_smoothbore_gun")
        self.click_smoothbore_gun()
        time.sleep(1)
        Logger.add_end_step(url=self.driver.current_url, method="select_smoothbore_gun")

    def select_rifled_gun(self):
        Logger.add_start_step(method="select_rifled_gun")
        self.click_rifled_gun()
        time.sleep(1)
        Logger.add_end_step(url=self.driver.current_url, method="select_rifled_gun")

    def select_traumatic_gun(self):
        Logger.add_start_step(method="select_traumatic_gun")
        self.click_traumatic_gun()
        time.sleep(1)
        Logger.add_end_step(url=self.driver.current_url, method="select_traumatic_gun")