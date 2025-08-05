from playwright.sync_api import sync_playwright
from pages.auth.logout.logout_page import LogoutPage
import time

def test_logout(login_user):
    page = login_user
    logout_page = LogoutPage(page)
    logout_page.logout()

    assert page.url =="https://www.saucedemo.com/"


# def test_logout():
#     with sync_playwright() as p:
#         browser = p.chomium.launch(headless=False)
#         page = browser.new_page()

#         logout_page = LogoutPage(page)

#         time.sleep(5)
#         browser.close()

# if __name__ == "__main__":
#     test_login()