import os
import time
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from pom.login_page import LoginPage

supplier_pass = os.environ["PASSWORD3"]

def test_supplier_login(log_in) -> None:

    page = log_in
    log_in_page = LoginPage(page)

    page.locator('internal:attr=[placeholder="Email"]').fill("mvpkhanapur@gmail.com")
    page.get_by_placeholder("Password").fill(supplier_pass)
    log_in_page.login_button.click()

    expect(page.locator("tex=H, Ujwala Welcome Back")).to_be_visible()

