from Base.base_msg import Base_msg
import Page

class Page_list(Base_msg):
    def __init__(self,driver):
        Base_msg.__init__(self,driver)

    def click_add(self):
        self.click_element(Page.add_id)