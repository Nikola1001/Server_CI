from builtins import Exception
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, passw
import time
import datetime

def login(username, passw, browser):
    try:
        browser.get("https://vk.com/")
        time.sleep(2)

        username_input = browser.find_element_by_id('index_email')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        pass_input = browser.find_element_by_id("index_pass")
        pass_input.clear()
        pass_input.send_keys(passw)
        pass_input.send_keys(Keys.ENTER)

        time.sleep(3)

        print("LOGIN OK!!")



    except Exception as ex:
        print(ex)
        print("OSHIBKA////////////////////////////////////////////////")
        browser.close()
        browser.quit()


def send_message(send_to, message, browser):
    browser.get("https://vk.com/im")
    time.sleep(3)
    to = browser.find_element_by_css_selector("[data-list-id='65765064']")  # for denis
    print("to")
    print(to)
    to.click()

    time.sleep(3)
    send = browser.find_element_by_id('im_editable0')
    send.send_keys(message)

    time.sleep(3)
    send = browser.find_element_by_class_name('im-chat-input--send')
    send.click()

    time.sleep(5)
    print("SEND MESSAGE OK.")




# browser = webdriver.Chrome("driver/chromedriver.exe")

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=op)

print("start")

login(username, passw, browser)

message = 'Денис - пидорок...'
send_message('_im_dialog_359927637', message, browser)
browser.close()
browser.quit()

