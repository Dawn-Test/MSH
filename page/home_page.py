import time

import allure
from selenium.webdriver.common.by import By

from base.base import BasePage, BaseHandle


# 定义对象库层
class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        # 我的保单按钮
        self.my_policy = By.XPATH, '//*[@id="home"]/div[1]/div[1]/div[3]/div[1]/div[1]/div/div[1]/span'
        # 就诊预约按钮
        self.appointment = By.XPATH, '//*[@id="home"]/div[1]/div[3]/div[1]/div[1]/div[2]'
        # 授权申请按钮
        self.empower = By.XPATH, '//*[@id="home"]/div[1]/div[3]/div[1]/div[2]/div[1]'
        # 理赔申请按钮
        self.claim = By.XPATH, '//*[@id="home"]/div[1]/div[1]/div[3]/div[1]/div[1]/div/div[2]/span/i'

    def find_my_policy(self):
        return self.get_element(self.my_policy)

    def find_appointment(self):
        return self.get_element(self.appointment)

    def find_empower(self):
        return self.get_element(self.empower)

    def find_claim(self):
        return self.get_element(self.claim)


# 定义操作层
class HomeHandle(BaseHandle):
    def __init__(self):
        self.home_page = HomePage()

    def get_my_policy(self):
        return self.home_page.find_my_policy().text

    @allure.step(title="点击就诊预约")
    def click_appointment(self):
        self.home_page.find_appointment().click()

    @allure.step(title="点击预授权预约")
    def click_empower(self):
        self.home_page.find_empower().click()

    @allure.step(title="点击理赔按钮")
    def click_claim(self):
        self.home_page.find_claim().click()


# 定义业务层
class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    def get_my_policy_msg(self):
        return self.home_handle.get_my_policy()

    # 跳转到就诊预约页面
    def go_my_appointment(self):
        self.home_handle.click_appointment()

    def go_my_empower(self):
        self.home_handle.click_empower()

    def go_claim(self):
        self.home_handle.click_claim()