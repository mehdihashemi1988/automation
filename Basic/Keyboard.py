from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://google.com")
search_box = driver.find_element('name', 'q')

search_box.send_keys("as roma")
sleep(3)

# Clear field using clear()
search_box.clear()
sleep(3)

actions = ActionChains(driver)

actions.key_down(Keys.SHIFT).send_keys_to_element(search_box, ' as roma').key_up(Keys.SHIFT).perform()  # AS ROMA
sleep(3)

actions.key_down(Keys.CONTROL).send_keys('a').perform()  # select+all
sleep(3)

# Clear field using CTRL+A+Del
search_box.click()
actions.key_down(Keys.CONTROL).send_keys('a').send_keys(Keys.DELETE).perform()
sleep(3)


