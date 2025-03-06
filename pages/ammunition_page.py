from datetime import time
import datetime
import time #for time sleep option

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Ammunition_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    title_1 = "//h1[@class='catalog_title__lU65A']"
    smoothbore_patron = "//*[@id='main']/div/section/div/div[1]/div[2]/div[1]/div/a[2]"
    rifled_patron =     "//*[@id='main']/div/section/div/div[1]/div[2]/div[1]/div/a[3]"
    traumatic_patron =  "//*[@id='main']/div/section/div/div[1]/div[2]/div[1]/div/a[4]"


    #Getters
    def get_title_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_1)))

    def get_smoothbore_patron(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smoothbore_patron)))

    def get_rifled_patron(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.rifled_patron)))

    def get_traumatic_patron(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.traumatic_patron)))


    #Actions
    def click_smoothbore_patron(self):
        self.get_smoothbore_patron().click()
        time.sleep(1)
        print("catalog -> ammunition -> smoothbore patron")

    def click_rifled_patron(self):
        self.get_rifled_patron().click()
        time.sleep(1)
        print("catalog -> ammunition -> rifled patron")

    def click_traumatic_patron(self):
        self.get_traumatic_patron().click()
        time.sleep(1)
        print("catalog -> ammunition -> traumatic patron")


    #Methods
    def check_current_location(self):
        Logger.add_start_step(method="check_current_location")
        time.sleep(3)
        url_1 = "https://ohotaktiv.ru/catalog/patrony_dlya_oruzhiya/"
        get_url1 = self.driver.current_url
        assert url_1 == get_url1
        print(get_url1)
        value_header = self.get_title_1().text
        assert value_header == "Патроны для оружия"
        print(value_header)
        Logger.add_end_step(url=self.driver.current_url, method="check_current_location")


    def select_smoothbore_patron(self):
        Logger.add_start_step(method="select_smoothbore_patron")
        self.click_smoothbore_patron()
        time.sleep(1)
        Logger.add_end_step(url=self.driver.current_url, method="select_smoothbore_patron")


    def select_rifled_patron(self):
        Logger.add_start_step(method="select_rifled_patron")
        self.click_rifled_patron()
        time.sleep(1)
        Logger.add_end_step(url=self.driver.current_url, method="select_rifled_patron")


    def select_traumatic_patron(self):
        Logger.add_start_step(method="select_traumatic_patron")
        self.click_traumatic_patron()
        time.sleep(1)
        Logger.add_start_step(method="select_traumatic_patron")