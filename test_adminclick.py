from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture()
def start_driver():
    driver = webdriver.Chrome()
    return driver

def test_login(start_driver):
    start_driver.get("http://localhost/litecart/admin")
    username_field = start_driver.find_element(By.NAME, "username")
    username_field.send_keys("admin")
    pass_field = start_driver.find_element(By.NAME, "password")
    pass_field.send_keys("admin")
    login_button = start_driver.find_element(By.NAME, "login")
    login_button.click()
    
    step1 = start_driver.find_element(By.LINK_TEXT, "Appearence")
    step1.click()
    time.sleep(2)
    assert start_driver.find_element(By.TAG_NAME, "h1")
    start_driver.find_element(By.LINK_TEXT, "Catalog").click()
    start_driver.quit()