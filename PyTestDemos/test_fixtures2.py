import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = None


@pytest.fixture
def setup():
    print('Start Browser')
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield
    driver.quit()
    print('Close Browser')  # Write your cleanup activities


def test_1(setup):
    driver.get("https://www.facebook.com")
    print('Test 1 executed')
    # print('Close Browser')


def test_2(setup):
    driver.get("https://www.google.com")
    print('Test 2 executed')
    # print('Close Browser')


def test_3(setup):
    driver.get("https://www.gmail.com")
    print('Test 3 executed')
    # print('Close Browser')
