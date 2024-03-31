from OrangeHRM.Locators import *


class Login:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, my_username):
        self.driver.find_element('xpath', username_textbox_xpath).send_keys(my_username)

    def enter_password(self, my_password):
        self.driver.find_element('xpath', password_textbox_xpath).send_keys(my_password)

    def click_login_button(self):
        self.driver.find_element('xpath', login_button_xpath).click()
