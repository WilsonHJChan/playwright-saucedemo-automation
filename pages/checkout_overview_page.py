from playwright.sync_api import Page


class CheckoutOverviewPage:

    def __init__(self, page: Page):
        self.page = page
        self.finish_button = page.locator('[data-test="finish"]')
        self.complete_header = page.locator('[data-test="complete-header"]')

    def finish_order(self):
        self.finish_button.click()