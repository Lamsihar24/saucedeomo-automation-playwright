import pytest
from playwright.sync_api import sync_playwright
from pages.auth.login.login_page import LoginPage
from pages.cart.cart_page import CartPage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture()
def browser_page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture()
def login_user(browser_page):  # <-- inject fixture browser_page lewat parameter
    # Login
    login_page = LoginPage(browser_page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    return browser_page

# Add to cart
@pytest.fixture()
def cart_with_item(login_user):
    page = login_user
    cart = CartPage(page)
    cart.add_item_to_cart()
    return page
