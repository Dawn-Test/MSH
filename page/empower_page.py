import time

import allure
from selenium.webdriver.common.by import By

from base.base import BasePage, BaseHandle

from utils import click_app_control, UtilsDriver


class EmpowerPage(BasePage):
    def __init__(self):
        super().__init__()
        # 授权申请按钮
        self.empower_btn = By.XPATH, '//*[@id="preAuthorizationList"]/div[3]/button'
        # 就诊人
        self.the_patient = By.CSS_SELECTOR, '.van-cell__value'
        # 就诊人弹框
        self.patient_confirm = By.XPATH, '//*[@id="preAuthorizationDiagno"]/div[4]/div/div[1]/button[2]'
        # 就诊人手机号
        self.phone = By.XPATH, '//*[@id="preAuthorizationDetail"]/div[1]/div[1]/div[9]/div[2]/div/input'
        # 就诊人邮箱
        self.email = By.XPATH, '//*[@id="preAuthorizationDetail"]/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div/input'
        # 就诊人详情页面确认
        self.basic_confirm = By.XPATH, '//*[@id="preAuthorizationDetail"]/div[2]/button'
        # 医院名称
        self.hospital_name = By.XPATH, '//*[@id="preAuthorizationDiagno"]/div[1]/div[2]/div[3]/div[2]/div/input'
        # 医疗诊断
        self.medical_diagnosis = By.XPATH, '//*[@id="preAuthorizationDiagno"]/div[1]/div[3]/div/div[2]/div/div/textarea'
        # 治疗方案
        self.treatment_plan = By.XPATH, '//*[@id="preAuthorizationDiagno"]/div[1]/div[4]/div[2]/div[2]'
        # 确认治疗方案
        # self.confirm_treatment_plan = By.XPATH, '//*[@id="preAuthorizationDiagno"]/div[5]/div/div[1]/button[2]'
        self.confirm_treatment_plan = By.CSS_SELECTOR, '.van-picker__confirm'
        # 治疗日期
        self.treatment_date = By.XPATH, '//*[@id="preAuthorizationDiagno"]/div[1]/div[4]/div[3]/div[2]'
        # 确定治疗日期
        self.confirm_treatment_date = By.XPATH, '//*[@id="preAuthorizationDiagno"]/div[4]/div/div[1]/button[2]'
        # 手术名称
        self.operation_name = By.XPATH, '//*[@id="preAuthorizationDiagno"]/div[1]/div[4]/div[4]/div[2]/div/input'
        # 预估费用
        self.estimated_cost = By.XPATH, '//*[@id="preAuthorizationDiagno"]/div[1]/div[4]/div[6]/div[2]/div/input'
        # 上传图片
        self.upload_pictures = By.XPATH, '//*[@id="preAuthorizationDiagno"]/div[1]/div[5]/div/div[3]/div/div/input'
        # 提交
        self.submit = By.XPATH, '//*[@id="preAuthorizationDiagno"]/div[2]/button'
        # 弹框
        self.define = By.XPATH, '//*[@id="preAuthorizationDiagno"]/div[6]/div[3]/button[2]/span'

        # 预授权成功弹框
        self.empower = By.XPATH, '//*[@id="preAuthorizationDiagno"]/div[7]/div[2]/div'

    def find_empower_btn(self):
        return self.get_element(self.empower_btn)

    def find_the_patient(self):
        return self.get_element(self.the_patient)

    def find_patient_confirm(self):
        return self.get_element(self.patient_confirm)

    def find_phone(self):
        return self.get_element(self.phone)

    def find_email(self):
        return self.get_element(self.email)

    def find_basic_confirm(self):
        return self.get_element(self.basic_confirm)

    def find_hospital_name(self):
        return self.get_element(self.hospital_name)

    def find_medical_diagnosis(self):
        return self.get_element(self.medical_diagnosis)

    def find_treatment_plan(self):
        return self.get_element(self.treatment_plan)

    def find_confirm_treatment_plan(self):
        return self.get_element(self.confirm_treatment_plan)

    def find_treatment_date(self):
        return self.get_element(self.treatment_date)

    def find_confirm_treatment_date(self):
        return self.get_element(self.confirm_treatment_date)

    def find_operation_name(self):
        return self.get_element(self.operation_name)

    def find_estimated_cost(self):
        return self.get_element(self.estimated_cost)

    def find_upload_pictures(self):
        return self.get_element(self.upload_pictures)

    def find_submit(self):
        return self.get_element(self.submit)

    def find_define(self):
        return self.get_element(self.define)

    def find_empower(self):
        return self.get_element(self.empower)


class EmpowerHandle(BaseHandle):
    def __init__(self):
        self.empower_page = EmpowerPage()
        self.driver = UtilsDriver.get_msh_driver()

    @allure.step(title="点击授权申请按钮")
    def click_empower_btn(self):
        self.empower_page.find_empower_btn().click()

    @allure.step(title="点击就诊人按钮")
    def click_the_patient(self):
        self.empower_page.find_the_patient().click()

    @allure.step(title="点击就诊人弹框")
    def click_patient_confirm(self):
        self.driver.execute_script("arguments[0].click();", self.empower_page.find_patient_confirm())

    @allure.step(title="输入就诊人手机号")
    def input_phone(self, phone):
        self.input_text(self.empower_page.find_phone(), phone)

    @allure.step(title="输入就诊人邮箱")
    def input_email(self, email):
        self.input_text(self.empower_page.find_email(), email)

    @allure.step(title="点击就诊人信息基础页面确认按钮")
    def click_basic_confirm(self):
        self.empower_page.find_basic_confirm().click()

    @allure.step(title="输入医院名称")
    def input_hospital_name(self, hospital_name):
        self.input_text(self.empower_page.find_hospital_name(), hospital_name)

    @allure.step(title="输入医疗诊断")
    def input_medical_diagnosis(self, medical_diagnosis):
        self.input_text(self.empower_page.find_medical_diagnosis(), medical_diagnosis)

    @allure.step(title="点击治疗方案")
    def click_treatment_plan(self):
        self.empower_page.find_treatment_plan().click()

    @allure.step(title="确认治疗方案")
    def click_confirm_treatment_plan(self):
        self.driver.execute_script("arguments[0].click();", self.empower_page.find_confirm_treatment_plan())

    @allure.step(title="治疗日期")
    def click_treatment_date(self):
        self.empower_page.find_treatment_date().click()

    @allure.step(title="确定治疗日期")
    def click_confirm_treatment_date(self):
        self.driver.execute_script("arguments[0].click();", self.empower_page.find_confirm_treatment_date())

    @allure.step(title="手术名称")
    def input_operation_name(self, operation):
        self.input_text(self.empower_page.find_operation_name(), operation)

    @allure.step(title="预估费用")
    def input_estimated_cost(self, cost):
        self.input_text(self.empower_page.find_estimated_cost(), cost)

    @allure.step(title="上传图片")
    def click_submit(self):
        self.empower_page.find_submit().click()

    @allure.step(title="提交")
    def click_define(self):
        self.driver.execute_script("arguments[0].click();", self.empower_page.find_define())

    @allure.step(title="弹框")
    def get_empower(self):
        return self.empower_page.find_empower().text


class EmpowerProxy:
    def __init__(self):
        self.empower_handle = EmpowerHandle()
        self.driver = UtilsDriver.get_msh_driver()

    def go_empower(self):
        self.empower_handle.click_empower_btn()
        self.empower_handle.click_the_patient()
        self.empower_handle.click_patient_confirm()
        self.empower_handle.input_phone("12345678900")
        self.empower_handle.input_email("test@qq.com")
        self.empower_handle.click_basic_confirm()
        self.empower_handle.input_hospital_name("Dawn_Test")
        self.empower_handle.input_medical_diagnosis("Dawn_Test")
        self.empower_handle.click_treatment_plan()
        self.empower_handle.click_confirm_treatment_plan()
        self.empower_handle.click_treatment_date()
        self.empower_handle.click_confirm_treatment_date()
        self.empower_handle.input_operation_name("Dawn_Test")
        self.empower_handle.input_estimated_cost("100")
        self.driver.find_element(By.XPATH,
                            '//*[@id="preAuthorizationDiagno"]/div[1]/div[5]/div/div[3]/div/div/input').send_keys(
            r"D:\PythonTest\MSH\image\test.jpg")
        # self.empower_handle.click_upload_pictures(r"D:\PythonTest\MSH\image\test.jpg")
        self.empower_handle.click_submit()
        self.empower_handle.click_define()
