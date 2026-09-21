from playwright.sync_api import expect


def test_backpack_added_to_cart(cart_page):

    expect(cart_page.items).to_have_count(1)

    expect(cart_page.items.first).to_have_text(
        "Sauce Labs Backpack"
    )