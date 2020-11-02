from src.pages.BasePage import BasePage


class SupportMeasuresPage(BasePage):

    def switch_to_next_page(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self

    def check_info_block(self):
        self \
            .driver \
            .find_element_by_xpath(
            "/html/body/form/div[3]/div[1]/div[4]/div[2]/div/div/div/div[2]/div/div[9]/div[2]")
        return self

    def report_info_block(self):
        self \
            .driver \
            .find_element_by_xpath(
            "/html/body/form/div[3]/div[1]/div[4]/div[2]/div/div/div/div[2]/div/div[12]/div[2]")
        return self

    def docs_info_block(self):
        self \
            .driver \
            .find_element_by_xpath("/html/body/form/div[3]/div[1]/div[4]/div[2]/div/div/div/div[2]/div/div[13]/div[2]")
        return self

    def pause_info_block(self):
        self \
            .driver \
            .find_element_by_xpath("/html/body/form/div[3]/div[1]/div[4]/div[2]/div/div/div/div[2]/div/div[14]/div[2]")
        return self

    def switch_to_previous_page(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        return self
