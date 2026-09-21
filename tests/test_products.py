from playwright.sync_api import expect


def test_sort_products_a_to_z(products_page):

    expect(products_page.product_items).to_have_count(6)

    products_page.sort_dropdown.select_option("az")

    product_names = products_page.product_names.all_text_contents()
    expected_names = sorted(product_names)

    assert product_names == expected_names


def test_add_backpack(products_page):

    products_page.add_backpack_to_cart()

    expect(products_page.cart_badge).to_have_text("1")