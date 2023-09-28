import random
import time
import names
class Cart:
    cart_list_items = "//div[@class='cart_list']//div[@class='inventory_item_name']"
    checkout_btn = "checkout"
    continue_btn = "continue"
    first_name_id = "first-name"
    last_name_id = "last-name"
    zip_id = "postal-code"
    finish_btn_id = "finish"

    def __init__(self, driver):
        self.driver = driver

    def return_items_in_cart(self):
        time.sleep(3)
        cart_items = self.driver.find_elements_by_xpath(self.cart_list_items)
        items = []
        for c in cart_items:
            items.append(c.text)
        print(items)
        return items

    def click_checkout(self):
        time.sleep(3)
        self.driver.find_element_by_id(self.checkout_btn).click()
        time.sleep(3)

    def click_continue_btn(self):
        time.sleep(3)
        self.driver.find_element_by_id(self.continue_btn).click()

    def input_first_name(self):
        time.sleep(3)
        self.driver.find_element_by_id(self.first_name_id).send_keys(names.get_first_name())

    def input_last_name(self):
        time.sleep(3)
        self.driver.find_element_by_id(self.last_name_id).send_keys(names.get_last_name())

    def input_zip(self):
        self.driver.find_element_by_id(self.zip_id).send_keys(random.randrange(500000, 600000))

    def verify_total(self):
        time.sleep(3)
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element_by_class_name("summary_subtotal_label"))
        total = self.driver.find_element_by_class_name("summary_subtotal_label").text
        total = float(total.split()[2].removeprefix("$"))
        total = "{:.2f}".format(total)
        tax = self.driver.find_element_by_class_name("summary_tax_label").text
        tax = float(tax.split()[1].removeprefix("$"))
        tax = "{:.2f}".format(tax)
        tot_one = float(total) + float(tax)
        tot = self.driver.find_element_by_xpath("//div[contains(text(),'Total: $')]").text
        tot = float(tot.split()[1].removeprefix("$"))
        tot = "{:.2f}".format(tot)

        assert float(tot) == tot_one

    def click_finish_btn(self):
        time.sleep(3)
        self.driver.find_element_by_id(self.finish_btn_id).click()

    def return_order_confirmation_msg(self):
        time.sleep(3)
        return self.driver.find_element_by_id("checkout_complete_container").text

    def click_back_to_home(self):
        time.sleep(3)
        self.driver.find_element_by_id("back-to-products").click()
        time.sleep(5)