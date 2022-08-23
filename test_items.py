<<<<<<< HEAD
import pytest
from selenium import webdriver
=======
>>>>>>> origin/master
import time
from selenium.webdriver.common.by import By

def test_button_add_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    addToBasket = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button").is_enabled()
<<<<<<< HEAD
    assert addToBasket, "No 'add to basket' button."
=======
    assert addToBasket, "No 'add to basket' button."
>>>>>>> origin/master
