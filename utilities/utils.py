from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

base_url = "https://www.saucedemo.com/"
pwd = "secret_sauce"


def initialize_browser():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(base_url)
    return driver


def wait_until_element_is_visible(driver, locator):
    wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
    return wait
