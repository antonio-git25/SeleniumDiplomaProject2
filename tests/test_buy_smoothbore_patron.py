import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #for chrome webdriver fix problem with closing

from pages.ammunition_page import Ammunition_page
from pages.basket_page import Basket_page
from pages.order_page import Order_page
from pages.result_page import Result_page
from pages.smoothbore_page import Smoothbore_page
from pages.smoothbore_patron_page import Smoothbore_patron_page
from pages.visa_payment_page import Visa_payment_page
from pages.welcome_page import Welcome_page
from pages.firearms_page import Firearms_page


def test_buy_smoothbore_patron():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_argument("--headless") #open driver without visual browser
    # driver = webdriver.Chrome(executable_path='C:\\Users\\Antonio\\PycharmProjects\\ResourceDriver\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=Service())

    print("Start Test 4: Покупка патронов для гладкоствольного оружия 12К")

    wp = Welcome_page(driver)
    wp.initialisation()
    wp.catalog_navigation_ammo()

    ap = Ammunition_page(driver)
    ap.check_current_location()
    ap.select_smoothbore_patron()

    spp = Smoothbore_patron_page(driver)
    spp.check_current_location()
    spp.set_product_filters()
    spp.choose_patron()
    spp.click_basket()

    bp = Basket_page(driver)
    bp.check_current_location()
    bp.click_increase_stuff()
    bp.print_basket_info()
    bp.stuff_value()
    bp.make_screenshot("smoothbore-patron", "basket")
    bp.confirmation()

    op = Order_page(driver)
    op.check_current_location()
    op.set_personal_data()
    op.make_screenshot("smoothbore-patron", "persondata")
    op.go_next()
    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(1)
    op.set_delivery()
    op.make_screenshot("smoothbore-patron", "delivery")
    op.go_next()
    op.show_final_order()
    ###Check marker for next scenario
    marker = op.get_payment_marker()  # "Оплата онлайн"/"Оплата при получении"
    op.go_next()

    rp = Result_page(driver)
    vpp = Visa_payment_page(driver)

    # Choose final scenario: with pya or without
    if marker == "Оплата при получении":
        rp = Result_page(driver)
        rp.check_current_location()
        rp.show_results()
        rp.make_screenshot("traumatic-gun", "result")
    elif marker == "Оплата онлайн":
        time.sleep(2)
        # driver.switch_to.window(driver.window_handles[1])
        vpp.initialisation()
        vpp.payment_by_card()
        time.sleep(3)
        #
        rp.show_results()
        rp.make_screenshot("traumatic-gun", "result")


    print("Complete Test 4")
    time.sleep(5)
    driver.close()


#python -m pytest -s -v test_buy_smoothbore_patron.py