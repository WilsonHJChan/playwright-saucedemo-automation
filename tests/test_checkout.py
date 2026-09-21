from playwright.sync_api import expect


def test_complete_order(checkout_overview_page):

    checkout_overview_page.finish_order()

    expect(
        checkout_overview_page.complete_header
    ).to_have_text("Thank you for your order!")