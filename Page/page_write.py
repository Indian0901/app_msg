from Base.base_msg import Base_msg
import Page


class Page_write(Base_msg):
    def __init__(self, driver):
        Base_msg.__init__(self, driver)

    def send_num(self, num):
        self.send_element(Page.num_xpath, num)

    def write_text(self,edit):
        self.send_element(Page.text_xpath, edit)
        self.click_element(Page.send_xpath)