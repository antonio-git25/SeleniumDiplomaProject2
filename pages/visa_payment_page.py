from datetime import time
import datetime
import time #for time sleep option
import random

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Visa_payment_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    title_11 = "//span[@data-qa='payment-info2-title']"
    exit_from_payment = "//*[@id='root']/div/div[2]/div[1]/div[6]/a/span"
    bill_sum = "//span[@data-qa='price']"
    bank_card = "//div[@data-qa='payment-option-title']"
    bank_card_number = "//input[@name='card-number']"
    bank_card_valid_mm = "//input[@name='expiry-month']"
    bank_card_valid_yy = "//input[@name='expiry-year']"
    bank_card_cvc = "//input[@name='security-code']"


    #Getters
    def get_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_11)))

    def get_exit_from_payment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.exit_from_payment)))

    def get_bill_sum(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bill_sum)))

    def get_bank_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bank_card)))

    def get_bank_card_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bank_card_number)))

    def get_bank_card_valid_mm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bank_card_valid_mm)))

    def get_bank_card_valid_yy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bank_card_valid_yy)))

    def get_bank_card_cvc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bank_card_cvc)))



    # Actions
    def show_bill_sum(self):
        print(self.get_bill_sum().text)

    def click_bank_card(self):
        self.get_bank_card().click()
        print("Choose bank card payment way")

    def input_bank_card_number(self, number):
        self.get_bank_card_number().send_keys(number)
        time.sleep(2)

    def input_bank_card_valid_mm(self):
        self.get_bank_card_valid_mm().send_keys('12')
        time.sleep(1)

    def input_bank_card_valid_yy(self):
        self.get_bank_card_valid_yy().send_keys('28')
        time.sleep(1)

    def input_bank_card_cvc(self, cvc):
        self.get_bank_card_cvc().send_keys(cvc)
        time.sleep(1)
        self.get_bank_card_cvc().send_keys(Keys.RETURN)
        time.sleep(2)



    #Methods
    def initialisation(self):
        Logger.add_start_step(method="initialisation")
        #self.driver.switch_to.window(self.driver.window_handles[1]) #!!!
        time.sleep(5)
        self.get_current_url()
        tit = self.get_title().text
        assert tit == "https://ohotaktiv.ru"
        self.click_bank_card()
        time.sleep(2)
        Logger.add_end_step(url=self.driver.current_url, method="initialisation")

    def payment_by_card(self):
        Logger.add_start_step(method="catalog_navigation_weapon")
        #number = f"22003001{random.randint(1780, 9090)}{random.randint(1650, 1810)}"
        number = "4716903188098331"
        cvc = random.randint(340, 820)
        print("Card number: ", number)
        print("CVC code: ", cvc)
        self.input_bank_card_number(number)
        self.input_bank_card_valid_mm()
        self.input_bank_card_valid_yy()
        self.input_bank_card_cvc(cvc)
        time.sleep(1)
        print("click pay button")
        time.sleep(3)
        Logger.add_end_step(url=self.driver.current_url, method="catalog_navigation_weapon")








