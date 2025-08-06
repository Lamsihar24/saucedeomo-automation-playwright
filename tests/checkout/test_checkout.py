import pytest
from pages.auth.login.login_page import LoginPage
from pages.checkout.checkout_page import CheckoutPage
from pages.cart.cart_page import CartPage
from data.checkout_data import checkout_user
import time

@pytest.mark.checkout
def test_checkout(cart_with_item):
    page = cart_with_item
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # Buka cart lalu klik checkout
    cart_page.open_cart()
    checkout_page.checkout_cart()

    # Mengisi form paki data faker
    checkout_page.fill_checkout_form(
        checkout_user["first_name"],
        checkout_user["last_name"],
        checkout_user["postal_code"]
    )

    checkout_page.continue_checkout()
    checkout_page.finish_order()

    # assert
    assert page.locator("[data-test=complete-header]").inner_text() == "Thank you for your order!"

    time.sleep(2)