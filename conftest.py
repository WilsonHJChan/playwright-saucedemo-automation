import pytest
import os
from playwright.sync_api import sync_playwright, Page

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage


@pytest.fixture
def page():
    with sync_playwright() as p:
        headless = os.getenv("CI") == "true"

        browser = p.chromium.launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()


@pytest.fixture
def login_page(page: Page):
    page.goto("https://www.saucedemo.com/")

    return LoginPage(page)

@pytest.fixture
def logged_in_page(login_page: LoginPage):
    login_page.login("standard_user", "secret_sauce")

    return login_page.page


@pytest.fixture
def products_page(logged_in_page: Page):
    return ProductsPage(logged_in_page)


@pytest.fixture
def cart_page(products_page: ProductsPage):
    products_page.add_backpack_to_cart()

    products_page.cart.click()

    return CartPage(products_page.page)


@pytest.fixture
def checkout_page(cart_page: CartPage):
    cart_page.checkout()

    return CheckoutPage(cart_page.page)


@pytest.fixture
def checkout_overview_page(checkout_page: CheckoutPage):
    checkout_page.fill_checkout_form("Test", "User", "12345")

    checkout_page.click_continue()

    return CheckoutOverviewPage(checkout_page.page)