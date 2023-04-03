import logging
import time
import pytest
import allure

from config import BaseDir
from page.login_page import LoginProxy
from page.home_page import HomeProxy
from page.appointment_page import AppointmentProxy
from utils import UtilsDriver, ExcelUtil, get_case_data


# case_data = ExcelUtil(excelPath='data/data.xlsx').dict_data()

case_data = get_case_data(BaseDir + "/data/test_login_data.json")



@pytest.mark.run(order=1)
class TestAppointment:
    def setup_class(self):
        self.login_proxy = LoginProxy()
        self.home_proxy = HomeProxy()
        self.appointment_proxy = AppointmentProxy()

    def teardown_class(self):
        UtilsDriver.quit_msh_driver()

    @pytest.mark.parametrize("username, password", case_data)
    @allure.severity(allure.severity_level.CRITICAL)
    # 定义登录测试用例
    def test_login(self, username, password):
        logging.info("用例数据如下：用户名：{}，密码：{}".format(username, password))
        # for i in case_data:
        #     username = i["username"]
        #     password = i["password"]
        #     self.login_proxy.login(username, password)
        #     self.teardown_class()
        self.login_proxy.login(username, password)
        allure.attach(UtilsDriver.get_msh_driver().get_screenshot_as_png(), "登录截图", allure.attachment_type.PNG)
        my_policy = self.home_proxy.get_my_policy_msg()
        assert "我的保单" == my_policy

    # 定义测试方法
    # @pytest.mark.skip(reason="不执行")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_page(self):
        self.home_proxy.go_my_appointment()

    # 定义就诊预约流程
    # @pytest.mark.skip(reason="不执行")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_appointment(self):
        self.appointment_proxy.go_appointment()
        success = self.appointment_proxy.appointment_handle.get_success_msg()
        assert "我知道了" == success
        allure.attach(UtilsDriver.get_msh_driver().get_screenshot_as_png(), "预约成功", allure.attachment_type.PNG)



