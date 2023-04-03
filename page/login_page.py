# 登录页面封装
import allure
from selenium.webdriver.common.by import By

from base.base import BasePage, BaseHandle


# 定义对象库层
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 账号输入框
        self.username = By.XPATH, '//*[@id="login"]/div[2]/div[2]/div/div/input'
        # 密码输入框
        self.password = By.XPATH, '//*[@id="login"]/div[2]/div[4]/div/div/input'
        # 勾选协议按钮
        self.agreement = By.XPATH, '//*[@id="login"]/div[4]/div[1]/div'
        # 登录按钮
        self.login_btn = By.XPATH, '//*[@id="login"]/button'

    # 定位用户名输入框
    def find_username(self):
        return self.get_element(self.username)

    # 定位密码输入框
    def find_password(self):
        return self.get_element(self.password)

    # 定位协议按钮
    def find_agreement(self):
        return self.get_element(self.agreement)

    # 定位登录按钮
    def find_login_btn(self):
        return self.get_element(self.login_btn)


# 定义操作层
class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    # 输入用户名
    @allure.step(title="输入用户名")
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    # 输入密码
    @allure.step(title="输入密码")
    def input_password(self, password):
        self.input_text(self.login_page.find_password(), password)

    # 勾选协议
    @allure.step(title="勾选协议")
    def click_agreement(self):
        self.login_page.find_agreement().click()

    # 点击登录按钮
    @allure.step(title="点击登录按钮")
    def click_login_btn(self):
        self.login_page.find_login_btn().click()


# 定义业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    def login(self, username, password):
        """

        :rtype: object
        """
        self.login_handle.input_username(username)
        self.login_handle.input_password(password)
        self.login_handle.click_agreement()
        self.login_handle.click_login_btn()
