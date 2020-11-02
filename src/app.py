from selenium.webdriver.android.webdriver import WebDriver

from src.pages.CovidPage import CovidPage
from src.pages.SupportMeasuresPage import SupportMeasuresPage


class Application(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def covid_page(self):
        return CovidPage(self.driver)

    def support_page(self):
        return SupportMeasuresPage(self.driver)
