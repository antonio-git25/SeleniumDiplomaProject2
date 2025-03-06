from datetime import time
import time #for time sleep option
import pytest
from selenium.webdriver.chrome import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #for chrome webdriver fix problem with closing
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture()
def set_up():
    print("Start test inner")
    yield
    print("Finish test inner")


@pytest.fixture(scope="module")
def set_group():
    print("Enter system")
    yield
    print("Exit system")



@pytest.fixture()
def main_set_up():
    print("Start test inner")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_argument("--headless") #open driver without visual browser
    # driver = webdriver.Chrome(executable_path='C:\\Users\\Antonio\\PycharmProjects\\ResourceDriver\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=Service())
    url = 'https://ohotaktiv.ru/'
    driver.get(url)
    driver.maximize_window()

    yield

    print("Finish test inner")
    time.sleep(3)
    driver.close()