from playwright.sync_api import sync_playwright
from pages.auth.login.login_page import LoginPage
import time

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Login success
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user","secret_sauce")

        # assert url
        expected_url = "https://www.saucedemo.com/inventory.html"
        assert page.url == expected_url, f"Expected URL to be {expected_url} but got {page.url}"

        #Assert text
        title_text = page.locator("[data-test=title]").inner_text()
        assert title_text == "Products"

        # Assert button add to cart
        add_to_cart_button = page.locator("#add-to-cart-sauce-labs-backpack").first
        assert add_to_cart_button.is_visible()
        assert add_to_cart_button.inner_text() == "Add to cart"

        # Assert product pertama
        first_item_name = page.locator("[data-test=inventory-item-name]").first.inner_text()
        assert first_item_name == "Sauce Labs Backpack"

        time.sleep(5)
        browser.close()

        

if __name__ == "__main__":
    test_login()