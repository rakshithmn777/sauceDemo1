import logging
import time
import logging
from utilities.utils import *
from selenium.webdriver.support.select import Select

class HomePage:

    burger_xpath = "//div[@class='bm-burger-button']/button"
    logout_id = "logout_sidebar_link"
    items_name_xpath = "//div[@class='inventory_list']//div[@class='inventory_item_name']"
    cart_class = "shopping_cart_link"
    backpack_atc_id = "add-to-cart-sauce-labs-backpack"
    light_atc_id = "add-to-cart-sauce-labs-bike-light"
    shirt_atc_id = "add-to-cart-sauce-labs-bolt-t-shirt"

    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        time.sleep(5)
        #wait_until_element_is_visible(self.driver, self.burger_xpath)
        self.driver.find_element_by_xpath(self.burger_xpath).click()
        #wait_until_element_is_visible(self.driver, self.logout_id)
        time.sleep(2)
        print("logging out")
        self.driver.find_element_by_id(self.logout_id).click()
        time.sleep(2)

    def return_order(self):
        time.sleep(3)
        order = self.driver.find_elements_by_xpath(self.items_name_xpath)
        default_order = []
        for i in order:
            default_order.append(i.text)
        print(default_order)
        return default_order

    def change_order(self):
        time.sleep(3)
        select = Select(self.driver.find_element_by_class_name("product_sort_container"))
        select.select_by_visible_text("Price (high to low)")
        time.sleep(5)

    def click_cart(self):
        time.sleep(3)
        self.driver.find_element_by_class_name(self.cart_class).click()
        time.sleep(5)

    def adding_items_to_cart(self):
        time.sleep(3)
        self.driver.find_element_by_id(self.backpack_atc_id).click()
        self.driver.find_element_by_id(self.light_atc_id).click()
        self.driver.find_element_by_id(self.shirt_atc_id).click()