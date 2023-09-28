from selenium import webdriver
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.cart import Cart
from utilities.utils import *


class TestTwo:
    items = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt']

    def test_add_to_cart(self):
        driver = initialize_browser()
        login = LoginPage(driver)
        login.login(user, pwd)
        home = HomePage(driver)
        home.adding_items_to_cart()
        home.logout()
        login.login(user, pwd)
        home.click_cart()
        cart = Cart(driver)
        itemss = cart.return_items_in_cart()
        assert itemss == self.items
        driver.quit()
