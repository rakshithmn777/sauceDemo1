class LoginPage:

    username_id = "user-name"
    pwd_id = "password"
    login_btn_id = "login-button"
    error_msg_xpath = "//*[@data-test='error']"

    def __init__(self, driver):
        self.driver = driver

    def input_username(self, username):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def input_password(self, pwd):
        self.driver.find_element_by_id(self.pwd_id).clear()
        self.driver.find_element_by_id(self.pwd_id).send_keys(pwd)

    def click_login_btn(self):
        self.driver.find_element_by_id(self.login_btn_id).click()

    def return_error_msg(self):
        return self.driver.find_element_by_xpath(self.error_msg_xpath).text