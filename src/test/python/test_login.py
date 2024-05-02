import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_valid_credentials_login():
    driver = webdriver.Chrome()
    driver.get('http://www.saucedemo.com')
    driver.implicitly_wait("30")
    driver.find_element(By.ID, "user-name").send_keys("user-name")
    assert driver.title == "Swag Labs"
    driver.close()
