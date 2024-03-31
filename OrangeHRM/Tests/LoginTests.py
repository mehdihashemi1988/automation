from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from OrangeHRM.Pages.Login import Login
from OrangeHRM.Pages.MainPage import MainPage
import unittest


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        my_login = Login(self.driver)
        my_main_page = MainPage(self.driver)
        my_login.enter_username('Admin')
        my_login.enter_password('admin123')
        my_login.click_login_button()
        my_main_page.check_main_page()
        sleep(3)

    # def test_invalid_login(self):

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
