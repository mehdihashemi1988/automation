from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
from pathlib import Path
from selenium.webdriver.chrome.options import Options

# # Chrome options: Incognito, Headless:
# chrome_options = Options()
# chrome_options.add_argument("--incognito")
# # chrome_options.add_argument("--headless") # without opening browser
# service = ChromeService(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=chrome_options)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://google.com")
# search_field = driver.find_element('name', 'q')
# search_field.send_keys("as roma")
# search_field.send_keys(Keys.RETURN)

# driver.get("https://wikipedia.org")
# driver.back()
# driver.refresh()
# driver.forward()
# window_title= driver.title
# print(window_title)
#
# driver.switch_to.new_window('tab')
# driver.get("https://time.ir")
#
# driver.switch_to.new_window('window')
# driver.get("https://wikipedia.org")
#
# current_window = driver.current_window_handle
# all_window = driver.window_handles
#
# driver.switch_to.window(all_window[1])
# driver.close()  # Close Session

# window_size = driver.get_window_size()
# print(window_size)  # {'width': 1050, 'height': 660}
# print(window_size['width'])
#
# driver.set_window_size(800, 600)
# size = driver.get_window_size()
# assert size['width'] == 800

# window_position = driver.get_window_position()
# print(window_position)
# driver.set_window_position(300, 400)
# assert driver.get_window_position()['y'] == 400
# driver.maximize_window()

# driver.get("https://www.yahoo.com")
# # run java script:
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
# # Screen Shot
# current_path = Path(__file__).parent
# file_path = os.path.join(current_path, 'screenshot1.png')
# driver.save_screenshot(file_path)

# sleep(2)
driver.quit()
