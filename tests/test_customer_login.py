import os
import time
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from pom.login_page import LoginPage

customer_pass = os.environ["PASSWORD1"]

def test_customer_login(log_in) -> None:

    page = log_in
    log_in_page = LoginPage(page)

    page.locator('internal:attr=[placeholder="Email"]').fill("shubhamshelar623@gmail.com")
    page.get_by_placeholder("Password").fill(customer_pass)
    log_in_page.login_button.click()

    expect(page.locator("text=Hi, Shubham Welcome Back")).to_be_visible()


