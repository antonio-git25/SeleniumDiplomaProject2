from datetime import time
import datetime
import time #for time sleep option

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Smoothbore_patron_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    title_2 = "//h1[@class='catalog_title__lU65A']"
    city_present_src = "//input[@id='nalichie_v_gorode-filter']"
    #city_present_ckbox = "//input[@value='moskva']"
    city_present_ckbox = "//label[contains(text(),'Москва')]"

    #calibr_down = "//button[@id=':rv:']"
    calibr_down = "//span[contains(text(),'Калибр, мм')]"
    calibr_input = "//input[@id='kalibr_2-filter']"
    calibr_chbox = "//label[contains(text(),'12x70')]"

    #typebullet_down = "//button[@id=':r12:']"
    typebullet_down = "//span[contains(text(),'Тип заряда')]"
    typebullet_click = "//label[contains(text(),'Картечь')]"

    patron = "//button[@title='Купить Патрон Техкрим 12/70 Жирный гусь картечь № 8,0 (в коробке 10 шт) ( коробка 240)']"
    basket = "//a[@title='Корзина']"



    #Getters
    def get_title_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_2)))

    def get_city_present_src(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_present_src)))

    def get_city_present_ckbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_present_ckbox)))

    def get_calibr_down(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.calibr_down)))

    def get_calibr_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.calibr_input)))

    def get_calibr_chbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.calibr_chbox)))

    def get_typebullet_down(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.typebullet_down)))

    def get_typebullet_click(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.typebullet_click)))

    def get_patron(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.patron)))

    def get_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket)))



    #Actions
    def set_location_present(self):
        self.get_city_present_src().send_keys("Москва")
        self.get_city_present_src().send_keys(Keys.RETURN)
        time.sleep(2)
        self.get_city_present_ckbox().click()
        time.sleep(1)
        print("Set city present: Москва")

    def set_calibr(self):
        time.sleep(2)
        self.get_calibr_down().click()
        time.sleep(1)
        self.get_calibr_input().send_keys("12x70")
        self.get_calibr_input().send_keys(Keys.RETURN)
        time.sleep(1)
        self.get_calibr_chbox().click()
        time.sleep(1)
        print("Set calibr: 12x70")

    def set_type_bullet(self):
        self.get_typebullet_down().click()
        time.sleep(1)
        self.get_typebullet_click().click()
        time.sleep(1)
        print("Type of bullet: Картечь")

    def click_patron(self):
        self.get_patron().click()
        print("Choose bullet: Патрон Техкрим 12/70 Жирный гусь картечь №8")
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
        url_2 = "https://ohotaktiv.ru/catalog/gladkostvolnye_patrony/"
        get_url2 = self.driver.current_url
        assert url_2 == get_url2
        print(get_url2)
        value_header = self.get_title_2().text
        assert value_header == "Гладкоствольные патроны"
        print(value_header)
        Logger.add_end_step(url=self.driver.current_url, method="check_current_location")


    def set_product_filters(self):
        Logger.add_start_step(method="set_product_filters")
        print("Set filter for city location")
        self.driver.execute_script("window.scrollTo(0, 50)")
        time.sleep(1)
        self.set_location_present()
        time.sleep(1)

        print("Set filter for calibr")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(1)
        self.set_calibr()
        time.sleep(1)

        print("Set filter for type of bullet")
        self.driver.execute_script("window.scrollTo(0, 950)")
        time.sleep(1)
        self.set_type_bullet()
        time.sleep(1)
        Logger.add_end_step(url=self.driver.current_url, method="set_product_filters")


    def choose_patron(self):
        Logger.add_start_step(method="choose_patron")
        print("Select patron")
        self.driver.execute_script("window.scrollTo(0, 100)")
        time.sleep(1)
        self.click_patron()
        time.sleep(10)
        self.get_screenshot("smoothbore-patron", "catalog")
        Logger.add_end_step(url=self.driver.current_url, method="choose_patron")


    def click_basket(self):
        Logger.add_start_step(method="click_basket")
        self.set_basket()
        Logger.add_end_step(url=self.driver.current_url, method="click_basket")