from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Web(object):
        def __init__(self):


            self.usuario = '.\Logistica'
            self.senha = 'eQHw3W{B'

            self.d = webdriver.Chrome()
            self.d.maximize_window()
            self.site = self.d.get('https://qliksense/sense/app/1b7d7429-76b4-49cf-9173-f88319020403')
        
        def login(self):
            self.d.find_element_by_class_name('secondary-button small-link').click()



W = Web()
