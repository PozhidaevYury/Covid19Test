from selenium.webdriver.common.by import By
from src.pages.BasePage import BasePage

LOCATOR_INN_FILED = (By.XPATH, "//*[@id=\"query\"]")
LOCATOR_SEARCH_BUTTON = (By.XPATH, "//*[@id=\"sectionQuery\"]/div/div[1]/div[3]/button")
LOCATOR_MEASURE_BUTTON = (By.XPATH, "//*[@id=\"sectionAll\"]/div/div/div[1]/a")
LOCATOR_PROLONGATION_REPORT_BUTTON = (By.XPATH, "//*[@id=\"sectionAll\"]/div/div/div[2]")
LOCATOR_PROLONGATION_DOCS_BUTTON = (By.XPATH, "/html/body/div[1]/div[3]/div/form/div[2]/div/div/div[3]")
LOCATOR_PAUSE_PENALTIES_BUTTON = (By.XPATH, "//*[@id=\"sectionAll\"]/div/div/div[4]")


class CovidPage(BasePage):

    def open(self):
        self.driver.get("https://service.nalog.ru/covid19/")
        return self

    def search_by_inn(self, inn):
        [self.find_element(LOCATOR_INN_FILED).send_keys(x) for x in inn]
        self.find_element(LOCATOR_SEARCH_BUTTON).click()
        return self

    def go_to_check_measure(self):
        self.find_element(LOCATOR_MEASURE_BUTTON).click()

    def go_to_prolongation_report(self):
        self.find_element(LOCATOR_PROLONGATION_REPORT_BUTTON).click()

    def go_to_prolongation_docs(self):
        self.find_element(LOCATOR_PROLONGATION_DOCS_BUTTON).click()

    def go_to_pause_penalties(self):
        self.find_element(LOCATOR_PAUSE_PENALTIES_BUTTON).click()
