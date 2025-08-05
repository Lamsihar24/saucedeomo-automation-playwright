from playwright.sync_api import sync_playwright
from pages.auth.login.login_page import LoginPage
import time

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user","secret_sauce")

        # assert
        expected_url = "https://www.saucedemo.com/inventory.html"
        assert page.url == expected_url, f"Expected URL to be {expected_url} but got {page.url}"
        time.sleep(5)
        
        browser.close()

if __name__ == "__main__":
    test_login()