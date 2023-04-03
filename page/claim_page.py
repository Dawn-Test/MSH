import time

import allure
from selenium.webdriver.common.by import By

from base.base import BasePage, BaseHandle

from utils import click_app_control, UtilsDriver


class ClaimPage(BasePage):
    def __init__(self):
        super().__init__()
        # 勾选协议
        self.tick_ip = By.XPATH, '//*[@id="appliNotice"]/div[1]/div[2]/div/div/i'
        # 下一步按钮
        self.next_btn = By.XPATH, '//*[@id="appliNotice"]/div[2]/button'
        # 就诊人
        # 就诊人弹框
        # 联系电话
        # 邮箱
        # 就诊人详情页面确认
        # 银行账户
        # 选择银行
        # 就诊开始时间
        # 选择就诊开始时间
        # 就诊结束时间
        # 选择就诊结束时间
        # 输入医院名称
        # 输入医院所在国家
        # 上传医疗账单
        # 点击下一步
        # 签名
        # 确认
        # 勾选协议
        # 提交

    def find_tick_ip(self):
        return self.get_element(self.tick_ip)

    def find_next_btn(self):
        return self.get_element(self.next_btn)


class ClaimHandle(BaseHandle):
    def __init__(self):
        self.claim_page = ClaimPage()
        self.driver = UtilsDriver.get_msh_driver()

    def click_tick_ip(self):
        self.claim_page.find_tick_ip().click()

    def click_next_btn(self):
        self.claim_page.find_next_btn().click()


class ClaimProxy:
    def __init__(self):
        self.claim_handle = ClaimHandle()
        self.driver = UtilsDriver.get_msh_driver()

    def go_claim(self):
        self.claim_handle.click_tick_ip()
        self.claim_handle.click_next_btn()