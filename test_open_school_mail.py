import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        yield browser


def test_navigate_to_reef_mail(browser):
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.get_by_label("חיפוש", exact=True).click()
    page.get_by_label("חיפוש", exact=True).fill("כרמל וים")
    page.keyboard.press("Enter")
    page.get_by_role("link", name="כרמל וים בי''ס יסודי אזורי").click()
    expect(page.locator("#wrapper_header_page img")).to_be_visible()
    page.get_by_role("link", name="התחברות לסביבת ענן של גוגל").click()
    page.locator("#blocker").click()
    page.get_by_placeholder("קוד משתמש").click()
    page.get_by_placeholder("קוד משתמש").fill("4953832")
    page.get_by_placeholder("סיסמה").click()
    page.get_by_placeholder("סיסמה").fill("5621")
    page.get_by_role("button", name="כניסה").click()
    input("Press Enter to close the browser...")
