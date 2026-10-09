from selenium import webdriver
import pytest


@pytest.fixture()
def set_up():
    print("Start test")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_argument("--guest")
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    print("End test")
    driver.quit()

@pytest.fixture(scope="module")
def set_group():
    print("Enter system")
    yield
    print("Exit system")
