import pytest
from pages.cart.cart_page import CartPage
from pages.auth.login.login_page import LoginPage
import time

@pytest.mark.cart
def test_add_to_cart(login_user):
    page = login_user

    # Add to cart
    cart_page = CartPage(page)
    cart_page.add_item_to_cart()
    cart_page.open_cart()

    # Assert
    assert cart_page.is_item_in_cart(), "Item was not found in the cart"

    time.sleep(2)

@pytest.mark.cart
def test_remove_from_cart(cart_with_item):
    page = cart_with_item
    cart = CartPage(page)

    cart.open_cart()

    cart.remove_item_from_cart()

    assert not cart.is_item_in_cart(), "Cart should be empty after removing item"

    time.sleep(2)