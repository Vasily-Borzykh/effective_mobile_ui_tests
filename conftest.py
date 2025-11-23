from playwright.sync_api import sync_playwright
import pytest
import os

BASE_URL = os.getenv("BASE_URL", "https://effective-mobile.ru/")

@pytest.fixture(scope="session")
def start_playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(start_playwright):
    browser = start_playwright.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()