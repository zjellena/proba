"""
https://testpages.eviltester.com/styled/dynamic-buttons-simple.html

Kattintsunk rá az összes gombra.
Ellenőrizzük a sikeres visszajelzést assert-el (All Buttons Clicked)
"""
import pytest
import sys
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = 'https://testpages.eviltester.com/styled/dynamic-buttons-simple.html'


class TestClickAllButtons:

    def setup_method(self):
        options = Options()
        options.add_argument('window-position=2000,50')
        options.add_argument("--disable-search-engine-choice-screen")
        options.add_experimental_option("detach", True)
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=options)

        self.browser.get(URL)



    def teardown_method(self):
        self.browser.quit()

    def test_click_all_buttons(self):
        start_button = self.browser.find_element(By.ID, 'button00')
        start_button.click()

        one_button = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'button01')))
        one_button.click()

        two_button = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'button02')))
        two_button.click()

        three_button = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'button03')))
        three_button.click()

        buttons_clicked = self.browser.find_element(By.ID, 'buttonmessage')
        assert buttons_clicked.text == 'All Buttons Clicked'
