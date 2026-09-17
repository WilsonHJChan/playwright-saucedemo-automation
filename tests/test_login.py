import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage


@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
])
def test_valid_login(page, username, password):
    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)

    expect(login_page.login_button).to_be_enabled()

    expect(login_page.login_button).to_have_attribute("id", "login-button")
    expect(login_page.login_button).to_have_attribute("type", "submit")
    expect(login_page.login_button).to_have_attribute("name", "login-button")

    login_page.login(username, password)

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_be_visible()
    expect(page.locator(".title")).to_have_text("Products")


@pytest.mark.parametrize("username, password", [
    ("wrong_user", "secret_sauce"),
    ("standard_user", "wrong_password"),
    ("wrong_user", "wrong_password"),
])
def test_invalid_login(page, username, password):
    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)
    login_page.login(username, password)

    expect(login_page.error_message).to_be_visible()