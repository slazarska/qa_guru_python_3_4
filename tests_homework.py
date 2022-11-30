from selene import have, be
from selene.api import *


def print_func_name(func_name, *args):
    func_name = func_name.__name__
    print("\nName of function: " + f"{func_name.replace('_', ' ')}")
    print(*args)


def open_browser(browser_name):
    print_func_name(open_browser, browser_name)
    browser.open


def go_to_companyname_homepage(page_url):
    print_func_name(go_to_companyname_homepage, page_url)
    browser.open(page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_func_name(find_registration_button_on_login_page, page_url, button_text)
    browser.element(by.text(button_text)).should(be.visible)


def test_check_registration_button_name():
    page_url: str = 'https://github.com/'
    button_text: str = 'Sign up'

    open_browser('Chrome')
    go_to_companyname_homepage(page_url)
    find_registration_button_on_login_page(page_url, button_text)
    browser.element(by.text(button_text)).should(have.text(button_text))
