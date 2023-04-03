import time

import allure
from selenium.webdriver.common.by import By

from base.base import BasePage, BaseHandle


# 定义对象层
from utils import click_app_control, UtilsDriver


class AppointmentPage(BasePage):
    def __init__(self):
        super().__init__()
        # 就诊预约按钮
        self.choice = By.CSS_SELECTOR, '.button_middle'
        # 重要提示弹框点击
        self.important_tips = By.XPATH, '//*[@id="body_wrap"]/div[4]/div[3]/button'
        # 就诊人
        self.the_patient = By.CSS_SELECTOR, '.van-cell__value'
        # 就诊人弹框
        self.patient_confirm = By.XPATH, '//*[@id="recommend"]/div[7]/div[7]/div[1]/button[2]'
        # 就诊人手机号
        self.phone = By.XPATH, '//*[@id="preAuthorizationDetail"]/div[1]/div[1]/div[9]/div[2]/div/input'
        # 就诊人邮箱
        self.email = By.XPATH, '//*[@id="preAuthorizationDetail"]/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div/input'
        # 就诊人详情页面确认
        self.basic_confirm = By.XPATH, '//*[@id="preAuthorizationDetail"]/div[2]/button'
        # 期望就诊医院
        self.expect_hospital = By.XPATH, '//*[@id="recommend"]/div[1]/div[3]/div[2]/span'
        # 点击城市
        self.city_btn = By.CSS_SELECTOR, '.city_name'
        # 选择上海
        self.choice_city = By.XPATH, '//*[@id="citySearch"]/div/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div[3]'

        # 搜索医院
        self.search_hospitals = By.XPATH, '//*[@id="advancedSearch"]/div[1]/div[1]/div[2]/div/div/div/div/input'
        # 输入搜索医院的名字
        self.input_hospitals = By.XPATH, '//*[@id="hospitalSearch"]/div/div[1]/form/div/div[1]/div/div/div/input'
        # 搜索按钮
        self.search_btn = By.XPATH, '//*[@id="hospitalSearch"]/div/div[1]/form/div/div[2]/div'
        # 医院预约按钮
        self.hospitals_order_btn = By.XPATH, '//*[@id="hospitalList"]/div[2]/div/div[2]/div[1]/div[3]/div[2]/button'
        # 开始时间
        self.start_time_btn = By.XPATH, '//*[@id="recommend"]/div[1]/div[6]/div[2]/div[1]'
        # 确认开始时间
        self.confirm_start_time = By.XPATH, '//*[@id="recommend"]/div[7]/div[1]/div[1]/button[2]'
        # 结束时间
        self.end_time_btn = By.XPATH, '//*[@id="recommend"]/div[1]/div[7]/div[2]/div[1]'
        # 确认结束时间
        self.confirm_end_time = By.XPATH, '//*[@id="recommend"]/div[7]/div[2]/div[1]/button[2]'
        # 详细症状
        self.detailed_symptoms = By.XPATH, '//*[@id="recommend"]/div[2]/div/div[2]/div/div/textarea'
        # 预约协议
        self.reservation_protocol = By.XPATH, '//*[@id="recommend"]/div[4]/div[1]/div/i'
        # 预约确认
        self.reservation_confirm = By.XPATH, '//*[@id="recommend"]/div[5]/button'

        # 预约成功确认按钮
        self.success = By.XPATH, '//*[@id="recommend"]/div[7]/div[3]/button/span'
        # self.success = By.XPATH, '//*[@id="recommend"]/div[7]/div[2]'

    # 定义就诊预约按钮
    def find_choice_appointment(self):
        return self.get_element(self.choice)

    # 定义就诊人按钮
    def find_the_patient(self):
        return self.get_element(self.the_patient)

    # 定义就诊人弹框
    def find_patient_confirm(self):
        return self.get_element(self.patient_confirm)

    # 定义就诊人手机号
    def find_phone(self):
        return self.get_element(self.phone)

    # 定义就诊人邮箱
    def find_email(self):
        return self.get_element(self.email)

    # 定义就诊人详情页面确认
    def find_basic_confirm(self):
        return self.get_element(self.basic_confirm)

    # 定义期望就诊医院
    def find_expect_hospital(self):
        return self.get_element(self.expect_hospital)

    # 定义城市按钮
    def find_city_btn(self):
        return self.get_element(self.city_btn)

    # 定义选择上海
    def find_choice_city(self):
        return self.get_element(self.choice_city)

    # 定义医院搜索框
    def find_search_hospitals(self):
        return self.get_element(self.search_hospitals)

    # 定义输入医院输入框
    def find_input_hospitals(self):
        return self.get_element(self.input_hospitals)

    # 定义搜索按钮
    def find_search_btn(self):
        return self.get_element(self.search_btn)

    # 定义医院预约按钮
    def find_hospitals_order_btn(self):
        return self.get_element(self.hospitals_order_btn)

    # 定义开始时间
    def find_start_time_btn(self):
        return self.get_element(self.start_time_btn)

    # 定义开始时间确认按钮
    def find_confirm_start_time(self):
        return self.get_element(self.confirm_start_time)

    # 定义结束时间
    def find_end_time_btn(self):
        return self.get_element(self.end_time_btn)

    # 定义结束时间确认按钮
    def find_confirm_end_time(self):
        return self.get_element(self.confirm_end_time)

    # 定义详细症状
    def find_detailed_symptoms(self):
        return self.get_element(self.detailed_symptoms)

    # 定义预约协议
    def find_reservation_protocol(self):
        return self.get_element(self.reservation_protocol)

    # 定义预约确认按钮
    def find_reservation_confirm(self):
        return self.get_element(self.reservation_confirm)

    # 定义我知道了按钮
    def find_success(self):
        return self.get_element(self.success)


# 定义操作层
class AppointmentHandle(BaseHandle):
    def __init__(self):
        self.appointment_page = AppointmentPage()
        self.driver = UtilsDriver.get_msh_driver()

    @allure.step(title="点击就诊预约按钮")
    def click_appointment(self):
        self.appointment_page.find_choice_appointment().click()

    @allure.step(title="点击就诊人按钮")
    def click_the_patient(self):
        self.appointment_page.find_the_patient().click()

    @allure.step(title="点击就诊人弹框")
    def click_patient_confirm(self):
        # click_app_control(self.driver, self.appointment_page.find_patient_confirm())
        self.driver.execute_script("arguments[0].click();", self.appointment_page.find_patient_confirm())

    @allure.step(title="输入就诊人手机号")
    def input_phone(self, phone):
        self.input_text(self.appointment_page.find_phone(), phone)

    @allure.step(title="输入就诊人邮箱")
    def input_email(self, email):
        self.input_text(self.appointment_page.find_email(), email)

    @allure.step(title="点击就诊人信息基础页面确认按钮")
    def click_basic_confirm(self):
        self.appointment_page.find_basic_confirm().click()

    @allure.step(title="点击期望就诊医院")
    def click_expect_hospital(self):
        self.appointment_page.find_expect_hospital().click()

    @allure.step(title="点击城市按钮")
    def click_city_btn(self):
        self.appointment_page.find_city_btn().click()

    @allure.step(title="选择上海")
    def click_choice_city(self):
        self.driver.execute_script("arguments[0].click();", self.appointment_page.find_choice_city())

    @allure.step(title="点击搜索医院框")
    def click_search_hospitals(self):
        self.appointment_page.find_search_hospitals().click()

    @allure.step(title="输入期望就诊医院")
    def input_input_hospitals(self, hospitals):
        self.input_text(self.appointment_page.find_input_hospitals(), hospitals)

    @allure.step(title="点击搜索按钮")
    def click_search_btn(self):
        self.appointment_page.find_search_btn().click()

    @allure.step(title="点击医院预约按钮")
    def click_hospitals_order_btn(self):
        self.appointment_page.find_hospitals_order_btn().click()

    @allure.step(title="点击开始时间")
    def click_start_time_btn(self):
        self.appointment_page.find_start_time_btn().click()

    @allure.step(title="点击开始时间确认按钮")
    def click_confirm_start_time(self):
        self.driver.execute_script("arguments[0].click();", self.appointment_page.find_confirm_start_time())

    @allure.step(title="点击结束时间")
    def click_end_time_btn(self):
        self.appointment_page.find_end_time_btn().click()

    @allure.step(title="点击结束时间确认按钮")
    def click_confirm_end_time(self):
        self.driver.execute_script("arguments[0].click();", self.appointment_page.find_confirm_end_time())

    @allure.step(title="输入详细症状")
    def input_detailed_symptoms(self, symptoms):
        self.input_text(self.appointment_page.find_detailed_symptoms(), symptoms)

    @allure.step(title="点击勾选协议")
    def click_reservation_protocol(self):
        self.appointment_page.find_reservation_protocol().click()

    @allure.step(title="点击预约确认")
    def click_reservation_confirm(self):
        self.appointment_page.find_reservation_confirm().click()

    @allure.step(title="获取预约成功按钮文本")
    def get_success_msg(self):
        return self.appointment_page.find_success().text


# 定义业务层
class AppointmentProxy:
    def __init__(self):
        self.appointment_handle = AppointmentHandle()

    # 就诊预约业务
    def go_appointment(self):
        self.appointment_handle.click_appointment()  # 点击就诊预约按钮
        self.appointment_handle.click_the_patient()  # 点击就诊人按钮
        self.appointment_handle.click_patient_confirm()  # 点击就诊人弹框
        self.appointment_handle.input_phone("12345678900")  # 输入手机号
        self.appointment_handle.input_email("test@qq.com")  # 输入邮箱
        self.appointment_handle.click_basic_confirm()      # 点击就诊人信息基础页面确认
        self.appointment_handle.click_expect_hospital()    # 点击期望就诊医院
        self.appointment_handle.click_city_btn()            # 点击城市按钮
        # time.sleep(2)
        self.appointment_handle.click_choice_city()         # 点击上海按钮
        self.appointment_handle.click_search_hospitals()    # 点击搜索输入框
        self.appointment_handle.input_input_hospitals("上海第一")  # 输入期望就诊医院
        self.appointment_handle.click_search_btn()        # 点击搜索按钮
        self.appointment_handle.click_hospitals_order_btn()   # 点击医院预约按钮
        self.appointment_handle.click_start_time_btn()          # 点击开始时间
        self.appointment_handle.click_confirm_start_time()      # 确认开始时间
        self.appointment_handle.click_end_time_btn()            # 点击结束时间
        self.appointment_handle.click_confirm_end_time()        # 确认结束时间
        self.appointment_handle.input_detailed_symptoms('Test_wjl')     # 输入症状
        self.appointment_handle.click_reservation_protocol()    # 勾选预约协议
        self.appointment_handle.click_reservation_confirm()     # 点击预约确认
