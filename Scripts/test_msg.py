import sys,os
sys.path.append(os.getcwd())

from Base.initdriver import get_driver
from Base.page import Get_obj
import pytest
from Data.get_data import get_data
import allure

class Test_msg:
    def setup_class(self):
        self.driver = get_driver('com.android.mms','.ui.ConversationList')
        self.get_obj = Get_obj(self.driver)
    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope='class',autouse=True)
    def add_num(self):
        self.get_obj.list_obj().click_add()
        self.get_obj.write_obj().send_num('13333333333')

    @pytest.mark.parametrize("text", get_data())
    @allure.step(title="发送短信")
    def test_msg(self,text):
        self.get_obj.write_obj().write_text(text)

