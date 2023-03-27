import os
import time
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from pom.login_page import LoginPage

agents_pass = os.environ["PASSWORD2"]

def test_agents_login(log_in) -> None:

    page = log_in
    log_in_page = LoginPage(page)

    page.locator('internal:attr=[placeholder="Email"]').fill("bunty.shelar619@gmail.com")
    page.get_by_placeholder("Password").fill(agents_pass)
    log_in_page.login_button.click()

    expect(page.locator("text=Hi, Bunty Welcome Back")).to_be_visible()

