from selenium import webdriver
import pytest

@pytest.fixture()
def set(browser):
    global driver
    if browser== "edge":
        driver=webdriver.Edge(executable_path="C:\\edgedriver_win64\\msedgedriver.exe")
        print("launching the edge brower")
    elif browser=="firefox":
        driver= webdriver.Firefox(executable_path="C:\\geckodriver-v0.30.0-win64\\geckodriver.exe")
        print("launching the firefox browser")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def  pytest_configure(config):
    config._metadata['Project name'] = 'Nopcommerceapp'
    config._metadata['ModuleName'] = 'Customers'
    config._metadata['Tester'] = 'aaa'
