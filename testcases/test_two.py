from selenium import webdriver
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from utilities.utils import *


class TestTwo:

    order = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']

    """
    Verifying Default Order on Homepage
    """
    def test_verify_default_sorting(self):
        driver = initialize_browser()
        login = LoginPage(driver)
        login.login(user, pwd)
        home = HomePage(driver)
        assert self.order == home.return_default_order()
