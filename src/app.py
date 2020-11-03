from selenium.webdriver.android.webdriver import WebDriver

from src.pages.CovidPage import CovidPage
from src.pages.SupportMeasuresPage import SupportMeasuresPage


# базовый класс, который возвращает ссылки на page object-ы всех стараниц в сценарии
# слой сделан по причине, что сам тест не должен ничего знать ни про драйвер, ни про еще какие-либо штуки селениума
# в тест внедряется зависимость класса Application, от него берется экземпляр нужной страницы и выполняется
# тестовый сценарий для этой страницы
# как по мне, так сам тест становится легкочитаемым и его легко поддерживать,
# в случае каких-либо изменений на странице или в сценарии, сразу понятно куда идти и где менять
class Application(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def covid_page(self):
        return CovidPage(self.driver)

    def support_page(self):
        return SupportMeasuresPage(self.driver)
