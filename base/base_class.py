import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver


    ###Method get current url###
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url: " + get_url)


    ###Method assert word###
    def assert_word(self, word, result):
        value_world = word.text
        assert value_world == result
        print("Good value word")


    ###Method screenshot###
    def get_screenshot(self, test_marker, page_marker):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M")
        name_screen = 'screen_' + test_marker + '_' + page_marker + '_' + now_date + '.png'
        # driver.save_screenshot(f"\\doc\\{name_screen}")
        self.driver.save_screenshot('C:\\Users\\Antonio\\PycharmProjects\\SeleniumDiplomaProject\\screen\\' + name_screen)


    ###Method assert url###
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")