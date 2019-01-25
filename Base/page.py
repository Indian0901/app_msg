from Page.page_list import Page_list
from Page.page_write import Page_write

class Get_obj:
    def __init__(self,driver):
        self.driver = driver

    def list_obj(self):
        return Page_list(self.driver)
    def write_obj(self):
        return Page_write(self.driver)