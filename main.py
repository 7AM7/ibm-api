from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os, sys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

URL = "https://www.ibm.com/account/reg/us-en/signup?formid=urx-30967&eventid=dna&lang=en_US&target=https%3A%2F%2Fdeveloper.ibm.com%2Fdwwi%2Fjsp%2Fp%2Fpostregister.jsp%3Feventid%3Ddna%26lang%3Den_US"

def create_broswer():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--lang=en")
    options.add_argument("--headless")
    options.add_argument('--log-level=3')
    options.add_argument('--disable-gpu')
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome("chromedriver.exe",chrome_options=options)
    browser.maximize_window()
    browser.set_page_load_timeout(180)
    browser.get(URL)
    browser.implicitly_wait(10)
    print(browser.current_url)
    return browser 

def scroll_to_and_click(browser, name, type='xpath'):
    if type == 'xpath':
        element = browser.find_element_by_xpath(name)
    elif type == 'class':
        element = browser.find_element_by_class_name(name)
    if element is not None:
        if element.is_displayed():
            browser.execute_script('window.scrollTo(0, ' + str(element.location['y']) + ');')
            element.click()

def registration_post_data(browser, email, first_name, last_name, password):
    try:
        Email = browser.find_element_by_name("email")
        if Email is not None:
            Email.send_keys(str(email))
            time.sleep(0.1)

        First_name = browser.find_element_by_name("firstName")
        if First_name is not None:
            First_name.send_keys(str(first_name))
            time.sleep(0.1)

        Last_name = browser.find_element_by_name("lastName")
        if Last_name is not None:
            Last_name.send_keys(str(last_name))
            time.sleep(0.1)

        Password = browser.find_element_by_name("password")
        if Password is not None:
            Password.send_keys(str(password))
            time.sleep(0.1)

        scroll_to_and_click(browser, '//*[@id=\"signupForm\"]/div[2]/button')
        try:
            error = browser.find_element_by_class_name("ibm-textcolor-red-50")
            if error is not None:
                if error.is_displayed():
                    print(error.text)
                    time.sleep(0.1)
                    browser.close()
                    return str(error.text)
        except:
            pass

        about_form = browser.find_element_by_class_name("ibm-common-overlay-inner")
        if about_form is not None:
            if about_form.is_displayed():
                scroll_to_and_click(browser, '//*[@id=\"ibm-com\"]/div[3]/div/div/div/div/div/p/button')
                time.sleep(0.1)
            else:
                browser.close()
                return "about_form error"
        
    except:
            browser.close()
            return "registration except 1"
    
    return "True"

def verification_post_data(browser, DIGIT_CODE):
    try:
        digit_code = browser.find_element_by_name("token")
        if digit_code is not None:
            digit_code.send_keys(str(DIGIT_CODE))
            time.sleep(0.3)

        scroll_to_and_click(browser, '//*[@id=\"verifyEmailForm\"]/div/div[2]/button')
        try:
            verify_error = browser.find_element_by_xpath('//*[@id="verifyEmailForm"]/div/div[1]/p/span/span[2]/span')
            if verify_error is not None:
                if verify_error.is_displayed():
                    print(verify_error.text)
                    time.sleep(0.1)
                    browser.close()
                    return str(verify_error.text)   
        except:
            pass
    except:
            browser.close()
            return "verification except 1"
            
    return "True"

