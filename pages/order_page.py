import random
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


class Order_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    title_4 = "//h2[@class='step-header_title__heekG']"

    first_name = "//input[@id='name-input']"
    last_name = "//input[@id='lastname-input']"
    cell = "//input[@id='tel-input']"
    mail = "//input[@id='email-input']"
    next_bt = "//button[@type='submit']"
    delivery_open = "//p[@data-choosed-select='moskva']"
    delivery_set = "//li[@data-select='select-store-moskva']"
    delivery_set_patron = "//li[@data-select='select-store-moskva']"

    way_pay = "//button[@data-sentry-source-file='payment-method.tsx']"
    current_stuff = "//p[@class='payment-card-item_cardName__B0Pde']"
    full_price = "(//p[@class='price-block_asideWrapTitle__X_V_C'])[2]"


    #Getters
    def get_title_4(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_4)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_cell(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cell)))

    def get_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mail)))

    def get_next_bt(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.next_bt)))

    def get_delivery_open(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_open)))

    def get_delivery_set(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_set)))

    def get_way_pay(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.way_pay)))

    def get_current_stuff(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.current_stuff)))

    def get_full_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.full_price)))


    #Actions
    def generate_personal_data(self):
        personal_data_mass = []
        f_name_mass = ["Иван", "Сергей", "Дмитрий", "Максим", "Олег", "Андрей", "Борис", "Роман"]
        l_name_mass = ["Тарасов", "Путилин", "Иванов", "Доронин", "Пронин", "Сергеев", "Луков", "Степнов"]
        cell_mask = ['906','910','902','908', '960']
        email_domen = []
        f_name = random.choice(f_name_mass)
        l_name = random.choice(l_name_mass)
        cell_gen = f"{random.choice(cell_mask)}{random.randint(340, 820)}{random.randint(10, 90)}{random.randint(10, 90)}"
        email = f"order_gun{random.randint(10, 99)}{random.randint(20, 80)}@gmail.com"
        personal_data_mass.append(f_name)
        personal_data_mass.append(l_name)
        personal_data_mass.append(cell_gen)
        personal_data_mass.append(email)
        return personal_data_mass


    def click_next(self):
        self.get_next_bt().click()


    def click_delivery(self):
        print(self.get_title_4().text)
        try:
            self.get_delivery_open().click()
            time.sleep(1)
            self.get_delivery_set().click()
            time.sleep(2)
            print(self.get_delivery_open().text)
            time.sleep(1)
        except TimeoutException:
            pass


    def final_order(self):
        print(self.get_title_4().text)
        print("Способ оплаты: ", self.get_way_pay().text)
        print("Ваши товары: ", self.get_current_stuff().text)
        print("Общая стоимость: ", self.get_full_price().text)


    def get_payment_marker(self):
        return self.get_way_pay().text






    #Methods
    def check_current_location(self):
        Logger.add_start_step(method="check_current_location")
        time.sleep(3)
        url_4 = "https://ohotaktiv.ru/order/"
        get_url4 = self.driver.current_url
        assert url_4 == get_url4
        print(get_url4)
        value_header = self.get_title_4().text
        assert value_header == "Введите данные получателя"
        print(value_header)
        Logger.add_end_step(url=self.driver.current_url, method="check_current_location")


    def set_personal_data(self):
        Logger.add_start_step(method="set_personal_data")
        data_mass = self.generate_personal_data()
        self.get_first_name().send_keys(data_mass[0])
        time.sleep(1)
        self.get_last_name().send_keys(data_mass[1])
        time.sleep(1)
        self.get_mail().send_keys(data_mass[3])
        time.sleep(1)
        self.get_cell().click()
        time.sleep(1)
        self.get_cell().send_keys(data_mass[2])
        time.sleep(1)
        for data in data_mass:
            print(data)
        Logger.add_end_step(url=self.driver.current_url, method="set_personal_data")


    def set_delivery(self):
        Logger.add_start_step(method="set_delivery")
        self.click_delivery()
        time.sleep(2)
        Logger.add_end_step(url=self.driver.current_url, method="set_delivery")


    def go_next(self):
        Logger.add_start_step(method="go_next")
        self.click_next()
        print("Next....")
        time.sleep(3)
        Logger.add_end_step(url=self.driver.current_url, method="go_next")


    def show_final_order(self):
        Logger.add_start_step(method="show_final_order")
        self.final_order()
        Logger.add_end_step(url=self.driver.current_url, method="show_final_order")


    def make_screenshot(self, test_marker, page_marker):
        Logger.add_start_step(method="make_screenshot")
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M")
        name_screen = 'screen_' + test_marker + '_' + page_marker + '_' + now_date + '.png'
        # driver.save_screenshot(f"\\doc\\{name_screen}")
        self.driver.save_screenshot('C:\\Users\\Antonio\\PycharmProjects\\SeleniumDiplomaProject\\screen\\' + name_screen)
        Logger.add_end_step(url=self.driver.current_url, method="make_screenshot")




