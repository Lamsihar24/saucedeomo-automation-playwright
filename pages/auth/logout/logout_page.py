from playwright.sync_api import Page
class LogoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.burger_menu = page.locator("#react-burger-menu-btn")
        self.button_logout = page.locator("#logout_sidebar_link")

    def logout(self):
        self.burger_menu.click()
        self.button_logout.click()
