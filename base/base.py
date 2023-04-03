# 定义msh server 的基类
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from utils import UtilsDriver


# 对象库层基类的封装
class BasePage:
    def __init__(self):
        self.driver = UtilsDriver.get_msh_driver()

    def get_element(self, location):
        wait = WebDriverWait(self.driver, 10, 1)
        element = wait.until(lambda x: x.find_element(*location))
        return element


# 操作层基类的封装
class BaseHandle:
    def input_text(self, element, text):
        # element.clear()  下三行代码 针对MSH就诊人页面清空,原来的信息清空不了
        element.click()
        element.click()
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(text)

