import json
import os
import time
import xlrd
from selenium import webdriver


# 定义工具类
from selenium.webdriver.common.by import By


class UtilsDriver:
    _msh_driver = None

    @classmethod
    def get_msh_driver(cls):
        if cls._msh_driver is None:
            chrome_options = webdriver.ChromeOptions()
            # 选择一种存在的模拟手机设备类型
            chrome_options.add_experimental_option(
                "mobileEmulation",
                {"deviceName": "iPhone 5"})
            cls._msh_driver = webdriver.Chrome(executable_path='driver/chromedriver.exe', desired_capabilities=chrome_options.to_capabilities())
            cls._msh_driver.maximize_window()
            cls._msh_driver.get('https://apitest.mshchina.com/wechat/#/login?openid=o_YpJwjcmoetXsDKJCBb9AEOvkSM&state=02&language=zh_cn')
        return cls._msh_driver

    @classmethod
    def quit_msh_driver(cls):
        if cls._msh_driver is not None:
            cls.get_msh_driver().quit()
            cls._msh_driver = None


# 唉，没用到留着吧，切换页面
def choice_appointment(driver, element, appointment):
    """
    :param driver:  浏览器驱动对象
    :param element:  元素对象
    :param appointment:  要选择的文本内容
    :return:
    """
    element.click()
    time.sleep(1)
    css = ".button_middle".format(appointment)
    driver.find_element(By.XPATH, css).click()


# 封装一个点击app控件的方法
def click_app_control(driver, element, find_element):
    element.click()
    xpach = find_element
    driver.execute_script("arguments[0].click();", xpach)


# 封装Json获取测试数据的方法
def get_case_data(filename):
    with open(filename, encoding='utf-8') as f:
        case = json.load(f)
    list_case_data = []
    for case_data in case.values():
        list_case_data.append(tuple(case_data.values()))
    return list_case_data


class ExcelUtil():
    def __init__(self, excelPath, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总的行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数据小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r


if __name__ == "__main__":
    filepath = "data/data.xlsx"
    # sheetName = "Sheet1"
    data = ExcelUtil(filepath)
    print(data.dict_data())


