from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page
        self.cart = page.locator('[data-test="shopping-cart-link"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.product_items = page.locator('[data-test="inventory-item"]')
        self.product_names = page.locator('[data-test="inventory-item-name"]')
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.backpack_add_button = page.locator(
            '[data-test="add-to-cart-sauce-labs-backpack"]'
        )

    def add_backpack_to_cart(self):
        self.backpack_add_button.click()

    def open_cart(self):
        self.cart.click()