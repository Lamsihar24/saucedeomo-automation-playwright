import pytest
from playwright.sync_api import sync_playwright
from pages.auth.login.login_page import LoginPage
from data.user_data import valid_user
from data.user_data import wrong_username
from data.user_data import wrong_password
import time

def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Login success
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login(valid_user["username"], valid_user["password"])

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

@pytest.mark.login
def test_login_invalid_username(browser_page):
    # login dengan username yang salah
    login_page = LoginPage(browser_page)
    login_page.navigate()
    login_page.login(wrong_username["username"], wrong_password["password"])
    error_message = browser_page.locator("[data-test=error]")
    assert error_message.is_visible()
    assert "Epic sadface: Username and password do not match any user in this service" in error_message.inner_text()
    time.sleep(5)

@pytest.mark.login
def test_login_invalid_password(browser_page):
    # Login dengan password yang salah
    login_page = LoginPage(browser_page)
    login_page.navigate()
    login_page.login(wrong_password["username"], wrong_password["password"])
    error_message = browser_page.locator("[data-test=error]")
    assert error_message.is_visible()
    assert "Epic sadface: Username and password do not match any user in this service" in error_message.inner_text()
    time.sleep(5)