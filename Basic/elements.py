from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://wikipedia.org")

# el = driver.find_element('id', 'searchInput')

# el = driver.find_element('xpath', '/html/body/main/div[2]/form/fieldset/div/input')
# Relative
# el = driver.find_element('xpath', "//input[@type='search']")
# driver.find_element('xpath', "//*[text()='Italiano']")
# el = driver.find_element('xpath', "//span[@class='lang-list-button-text jsl10n']")
# el.click()

el = driver.find_element('xpath', "//*[@id='search']")
# //*[(@id='fname' or @name='fname') and @type='text']
# //*[@id='lname']/../..//*[@id='fname']




# el.send_keys("as roma")
sleep(6)
