import logging
import time

import pytest
import allure

from config import BaseDir
from page.login_page import LoginProxy
from page.home_page import HomeProxy
from page.empower_page import EmpowerProxy
from page.appointment_page import AppointmentProxy
from utils import UtilsDriver, get_case_data


# case_data = ExcelUtil(excelPath='data/data.xlsx').dict_data()

case_data = get_case_data(BaseDir + "/data/test_login_data.json")



@pytest.mark.run(order=2)
class TestEmpower:
    def setup_class(self):
        self.login_proxy = LoginProxy()
        self.home_proxy = HomeProxy()
        self.empower_proxy = EmpowerProxy()

    def teardown_class(self):
        UtilsDriver.quit_msh_driver()

    @pytest.mark.parametrize("username, password", case_data)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, username, password):
        logging.info("用例数据如下：用户名：{}，密码：{}".format(username, password))
        self.login_proxy.login(username, password)
        allure.attach(UtilsDriver.get_msh_driver().get_screenshot_as_png(), "登录截图", allure.attachment_type.PNG)
        my_policy = self.home_proxy.get_my_policy_msg()
        assert "我的保单" == my_policy

    @allure.severity(allure.severity_level.CRITICAL)
    def test_home_page(self):
        self.home_proxy.go_my_empower()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_empower(self):
        self.empower_proxy.go_empower()
        empower = self.empower_proxy.empower_handle.get_empower()
        assert "授权申请已提交，请耐心等候审核" == empower
        allure.attach(UtilsDriver.get_msh_driver().get_screenshot_as_png(), "预授权成功截图", allure.attachment_type.PNG)


