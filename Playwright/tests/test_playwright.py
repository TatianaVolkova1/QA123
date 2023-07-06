from playwright.sync_api import Page, expect
from config import url_demo_playwright


def test_login_page(page: Page):
    page.goto('https://demo.opencart.com/admin/')
    page.fill('input#input-username', 'demo')
    page.fill('input#input-password', 'demo')
    page.click('button:text("Login")')
    page.wait_for_load_state('load')
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()

    
def test_google_search(page: Page):
    page.goto('https://www.google.com/')
    page.fill('.gLFyf', 'Playwright Python')
    page.wait_for_timeout(5000)
    page.click('.gNO89b')
    page.wait_for_timeout(40000)
    expect(page.get_by_role("heading", name="Похожие запросы")).to_be_visible()
   



