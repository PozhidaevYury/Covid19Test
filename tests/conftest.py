import pytest
from selenium import webdriver

from src.app import Application


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="/Users/urij/PycharmProjects/covid-test/chromedriver")
    # driver.get("https://service.nalog.ru/covid19/")
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def app(browser):
    return Application(browser)
