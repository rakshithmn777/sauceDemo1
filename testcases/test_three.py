import time

import pytest
from selenium import webdriver
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.cart import Cart
from utilities.utils import *


class TestTwo:
    items = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt']
    fn_err_msg = "Error: First Name is required"
    ln_err_msg = "Error: Last Name is required"
    zip_err_msg = "Error: Postal Code is required"
    order_confirmation_one = "Thank you for your order!"
    order_confirmation_two = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"

    @pytest.mark.run(order=1)
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

    @pytest.mark.run(order=2)
    def test_place_order(self):
        driver = initialize_browser()
        login = LoginPage(driver)
        login.login(user, pwd)
        home = HomePage(driver)
        cart = Cart(driver)
        home.add_high_low_items()
        home.click_cart()
        cart.click_checkout()
        cart.click_continue_btn()
        fn_error = login.return_error_msg()
        assert fn_error == self.fn_err_msg
        cart.input_first_name()
        cart.click_continue_btn()
        ln_error = login.return_error_msg()
        assert ln_error == self.ln_err_msg
        cart.input_last_name()
        cart.click_continue_btn()
        zip_error = login.return_error_msg()
        assert zip_error == self.zip_err_msg
        cart.input_zip()
        cart.click_continue_btn()
        cart.verify_total()
        cart.click_finish_btn()
        order_confirm = cart.return_order_confirmation_msg()
        assert self.order_confirmation_one in order_confirm
        assert self.order_confirmation_two in order_confirm
        cart.click_back_to_home()
        driver.quit()
