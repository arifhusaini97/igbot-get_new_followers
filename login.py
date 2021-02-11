from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time

class Login:
    def __init__(self, driver, username, password):
        self.driver=driver
        self.username=username
        self.password=password
    def signin(self):
        print('Open the login page...')
        self.driver.get('https://www.instagram.com/accounts/login/?hl=en')
        uid = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')))
        uid.click()
        uid.send_keys(self.username)
        pswd=self.driver.find_element_by_css_selector('div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
        pswd.click()
        pswd.send_keys(self.password)
        btn=self.driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3)')
        btn.click()
