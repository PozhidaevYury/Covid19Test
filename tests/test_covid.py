# внедряем фикстуру app, которая возвращает базовый page object с инициализированным вебдрайвером,
# от app уже можно вызывать все переопределнные страницы и их методы
def test_covid(app):

    # переходим на https://service.nalog.ru/covid19/
    # вводим инн
    # нажимаем на "Приостановлены проверки"
    app \
        .covid_page() \
        .open() \
        .search_by_inn("773466902356") \
        .go_to_check_measure()

    # переходим на https://www.nalog.ru/rn77/business-support-2020/#t11
    # переключаем контекст вебдрайвера на открытую страницу
    # проверяем открытие раздела путем сравнения текста элемента и ожидаемого текста
    # закрываем страницу и переходим обратно на https://service.nalog.ru/covid19/
    app \
        .support_page() \
        .switch_to_measured_page() \
        .check_info_block() \
        .switch_to_covid_page()

    # нажимаем на "Продлены сроки сдачи отчетности"
    app \
        .covid_page()\
        .go_to_prolongation_report()

    # переходим на https://www.nalog.ru/rn77/business-support-2020/#t11
    # переключаем контекст вебдрайвера на открытую страницу
    # проверяем открытие раздела путем сравнения текста элемента и ожидаемого текста
    # закрываем страницу и переходим обратно на https://service.nalog.ru/covid19/
    app \
        .support_page() \
        .switch_to_measured_page() \
        .report_info_block() \
        .switch_to_covid_page()

    # нажимаем на "Продлены сроки представления документов по требованию"
    app \
        .covid_page() \
        .go_to_prolongation_docs()

    # переходим на https://www.nalog.ru/rn77/business-support-2020/#t11
    # переключаем контекст вебдрайвера на открытую страницу
    # проверяем открытие раздела путем сравнения текста элемента и ожидаемого текста
    # закрываем страницу и переходим обратно на https://service.nalog.ru/covid19/
    app \
        .support_page() \
        .switch_to_measured_page() \
        .docs_info_block() \
        .switch_to_covid_page()

    # нажимаем на "Приостановлены меры взыскания"
    app \
        .covid_page() \
        .go_to_pause_penalties()

    # переходим на https://www.nalog.ru/rn77/business-support-2020/#t11
    # переключаем контекст вебдрайвера на открытую страницу
    # проверяем открытие раздела путем сравнения текста элемента и ожидаемого текста
    # закрываем страницу и переходим обратно на https://service.nalog.ru/covid19/
    app \
        .support_page() \
        .switch_to_measured_page() \
        .pause_info_block() \
        .switch_to_covid_page()
