def test_covid(app):
    app \
        .covid_page() \
        .open() \
        .search_by_inn("773466902356") \
        .go_to_check_measure()

    app \
        .support_page() \
        .switch_to_next_page() \
        .check_info_block() \
        .switch_to_previous_page()

    app \
        .covid_page() \
        .go_to_prolongation_report()

    app \
        .support_page() \
        .switch_to_next_page() \
        .report_info_block() \
        .switch_to_previous_page()

    app \
        .covid_page() \
        .go_to_prolongation_docs()

    app \
        .support_page() \
        .switch_to_next_page() \
        .docs_info_block() \
        .switch_to_previous_page()

    app \
        .covid_page() \
        .go_to_pause_penalties()

    app \
        .support_page() \
        .switch_to_next_page() \
        .pause_info_block() \
        .switch_to_previous_page()
