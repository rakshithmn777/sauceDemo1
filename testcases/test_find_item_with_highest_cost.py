import time

from selenium import webdriver
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.cart import Cart
from utilities.utils import *

class TestFindItemWithHighestCostAndRemoveFromCart:
    user1 = "standard_user"

    def test_find_item_with_highest_cost(self):
        driver = initialize_browser()
        login = LoginPage(driver)
        login.login(user, pwd)
        home = HomePage(driver)
        cart = Cart(driver)
        home.adding_items(home.backpack_atc_id)
        home.adding_items(home.light_atc_id)
        home.adding_items(home.shirt_atc_id)
        home.adding_items(home.high_item)
        home.click_cart()
        cart.check_the_cost_of_items_and_remove_the_highest()
        time.sleep(5)