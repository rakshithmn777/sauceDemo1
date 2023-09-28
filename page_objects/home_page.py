import time

from utilities.utils import *

class HomePage:

    burger_xpath = "//div[@class='bm-burger-button']/button"
    logout_id = "logout_sidebar_link"

    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        time.sleep(5)
        #wait_until_element_is_visible(self.driver, self.burger_xpath)
        self.driver.find_element_by_xpath(self.burger_xpath).click()
        #wait_until_element_is_visible(self.driver, self.logout_id)
        time.sleep(2)
        self.driver.find_element_by_id(self.logout_id).click()
        time.sleep(2)