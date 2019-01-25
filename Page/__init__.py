from selenium.webdriver.common.by import By

add_id = (By.ID,'com.android.mms:id/action_compose_new')
num_xpath = (By.XPATH,"//*[contains(@text,'接收者')]")
text_xpath = (By.XPATH,"//*[contains(@text,'键入信息')]")
send_xpath = (By.ID,'com.android.mms:id/send_button_sms')
res_id = (By.ID,'com.android.mms:id/text_view')