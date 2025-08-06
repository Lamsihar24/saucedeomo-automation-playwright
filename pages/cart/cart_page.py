from playwright.sync_api import Page

class CartPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_button = page.locator("#add-to-cart-sauce-labs-backpack")
        self.remove_btn_selector = ("#remove-sauce-labs-backpack")
        self.shopping_cart_link = page.locator(".shopping_cart_link")
        self.cart_item = page.locator(".cart_item")

    def add_item_to_cart(self):
        self.add_to_cart_button.click()

    def remove_item_from_cart(self):
        self.page.locator(self.remove_btn_selector).click()

    def open_cart(self):
        self.shopping_cart_link.click()

    def is_item_in_cart(self):
        return self.cart_item.is_visible()