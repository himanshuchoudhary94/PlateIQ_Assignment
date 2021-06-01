import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope='class')
def setup(request):
    browser = request.config.getoption('browser')
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser == 'edge':
        driver = webdriver.Chrome(executable_path="C:\\msedgedriver.exe")

    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    driver.implicitly_wait(3)
    request.cls.driver = driver
    request.cls.webdriver = webdriver
    yield
    driver.close()