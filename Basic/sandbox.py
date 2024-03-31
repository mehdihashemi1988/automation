from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(20)

driver.find_element('xpath', "//input[@name='username']").send_keys('a')
driver.find_element('xpath', "//input[@name='password']").send_keys('b')
driver.find_element('xpath', "//button[@type='submit']").click()

sleep(5)
