import pytest
from playwright.sync_api import Playwright

@pytest.fixture()
def log_in(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("https://phptravels.net/")
    page.set_default_timeout(5000)

    page.get_by_role("button", name="Account ").click()
    page.get_by_role("link", name="Customer Login").click()
    page.wait_for_url("https://phptravels.net/login")

    yield page
    page.close()
