from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch the url')
def step_impl(context):
    driver = webdriver.Chrome()
    driver.get('http://www.saucedemo.com')
    driver.implicitly_wait(30)


@step("I input credentials")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # raise NotImplementedError(u'STEP: And I input credentials')
