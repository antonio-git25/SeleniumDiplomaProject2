from datetime import time
import datetime
import time #for time sleep option

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Welcome_page(Base):
    url = 'https://ohotaktiv.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    got_it_bt = "//button[@class='CookiePopup_accept__2FCsg']"
    other_city = "//button[@class='button_button__HOmVR first-time_button__g1t7e first-time_button_incorrect__ISURG']"
    location = "//input[@id='geo-popup-city']"
    current_city = "//button[@class='geo-popup_defaultCitiesButton__ccD9p']"
    close_bunner_1 = "//div[@class='popmechanic-close']"

    catalog = "//button[@class='button_button__HOmVR header-catalog-button_hamburger__4iGFR']"
    firearms = "//div[contains(text(),'Огнестрельное оружие')]"
    ammunition = "//div[contains(text(),'Патроны для оружия')]"


    #Getters
    def get_got_it_bt(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.got_it_bt)))

    def get_other_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.other_city)))

    def get_location(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.location)))

    def get_current_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.current_city)))

    def get_close_bunner_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_bunner_1)))

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_firearms(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.firearms)))

    def get_ammunition(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ammunition)))




    # Actions
    def click_got_it_bt(self):
        self.get_got_it_bt().click()
        print("Accept 18 years old")

    def other_city_click(self):
        self.get_other_city().click()
        print("Set location: other city")

    def find_city(self, city):
        self.get_location().send_keys(city)
        time.sleep(1)
        self.get_location().send_keys(Keys.RETURN)
        time.sleep(1)

    def set_city(self, city):
        self.get_current_city().click()
        time.sleep(1)
        print("Set location:" + city)

    def click_bunner_1(self):
        self.get_close_bunner_1().click()
        print("Bunner is closed")

    def go_navigation(self):
        self.get_catalog().click()
        time.sleep(1)
        print("Navigate to catalog")

    def go_firearms(self):
        self.get_firearms().click()
        print("catalog -> firearms")

    def go_ammunition(self):
        self.get_ammunition().click()
        print("catalog -> ammunition")


    #Methods
    def initialisation(self):
        Logger.add_start_step(method="initialisation")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_got_it_bt()
        time.sleep(1)
        self.other_city_click()
        time.sleep(1)
        self.find_city("Москва")
        self.set_city("Москва")
        time.sleep(1)
        #self.click_bunner_1()
        Logger.add_end_step(url=self.driver.current_url, method="initialisation")

    def catalog_navigation_weapon(self):
        Logger.add_start_step(method="catalog_navigation_weapon")
        self.go_navigation()
        self.go_firearms()
        Logger.add_end_step(url=self.driver.current_url, method="catalog_navigation_weapon")

    def catalog_navigation_ammo(self):
        Logger.add_start_step(method="catalog_navigation_ammo")
        self.go_navigation()
        self.go_ammunition()
        Logger.add_end_step(url=self.driver.current_url, method="catalog_navigation_ammo")







