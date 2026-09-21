import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
])
def test_valid_login(login_page, username, password):

    expect(login_page.login_button).to_be_disabled()

    expect(login_page.login_button).to_have_attribute("id", "login-button")
    expect(login_page.login_button).to_have_attribute("type", "submit")
    expect(login_page.login_button).to_have_attribute("name", "login-button")

    login_page.login(username, password)

    expect(login_page.page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    expect(login_page.page.locator(".title")).to_be_visible()
    expect(login_page.page.locator(".title")).to_have_text("Products")


@pytest.mark.parametrize("username, password, expected_error", [
    (
        "wrong_user",
        "secret_sauce",
        "Epic sadface: Username and password do not match any user in this service"
    ),
    (
        "standard_user",
        "wrong_password",
        "Epic sadface: Username and password do not match any user in this service"
    ),
    (
        "wrong_user",
        "wrong_password",
        "Epic sadface: Username and password do not match any user in this service"
    ),
    (
        "",
        "secret_sauce",
        "Epic sadface: Username is required"
    ),
    (
        "standard_user",
        "",
        "Epic sadface: Password is required"
    ),
    (
        "",
        "",
        "Epic sadface: Username is required"
    ),
    (
        "locked_out_user",
        "secret_sauce",
        "Epic sadface: Sorry, this user has been locked out."
    ),
])
def test_invalid_login(login_page, username, password, expected_error):

    login_page.login(username, password)

    expect(login_page.error_message).to_have_text(expected_error)