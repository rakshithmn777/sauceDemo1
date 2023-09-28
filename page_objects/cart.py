import time


class Cart:

    cart_list_items= "//div[@class='cart_list']//div[@class='inventory_item_name']"

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