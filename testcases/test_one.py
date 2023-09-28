from selenium import webdriver
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from utilities.utils import *


class TestOne:
    user1 = "standard_user"
    user2 = "performance_glitch_user"
    user3 = "locked_out_user"
    error_msg = "Epic sadface: Sorry, this user has been locked out."

    """
    1. Checking "standard_user" & "performance_glitch_user” is able to do successful login and land on home page and do logout.
    2. Asserting the error msg on login screen
    """

    def test_login_validations(self):
        driver = initialize_browser()
        login = LoginPage(driver)
        login.input_username(self.user1)
        login.input_password(pwd)
        login.click_login_btn()
        home = HomePage(driver)
        home.logout()
        login.input_username(self.user2)
        login.input_password(pwd)
        login.click_login_btn()
        home.logout()
        login.input_username(self.user3)
        login.input_password(pwd)
        login.click_login_btn()
        error = login.return_error_msg()
        assert error == self.error_msg
        driver.quit()
