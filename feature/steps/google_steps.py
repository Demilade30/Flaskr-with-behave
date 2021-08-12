from helium import *
from behave import then
from behave import when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@when('we visit google')
def step_impl(context):
    set_driver(context.browser)
    go_to('http://www.google.com')


@when(u'search for "{text}"')
def step_impl(context, text):
    set_driver(context.browser)
    write(text)
    press(ENTER)
    WebDriverWait(context.browser, 10)

@then(u'it should have a title "{text}"')
def step_impl(context, text):
    print("" + text + " " + context.browser.title)
    assert text in context.browser.title