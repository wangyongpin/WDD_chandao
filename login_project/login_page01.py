from selenium import webdriver
import os,time
from selenium.webdriver.common.by import By
from commono.log_utlis import logger
from commono.base_page import BasePage

class Login_Project_Test(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.user_name = {'element_name':'用户名输入框',
                          'locator_type':'xpath',
                          'locator_value': '//input[@name="account]',
                          'timeout': 5}
        self.user_password = {'element_name': '密码输入框',
                          'locator_type': 'xpath',
                          'locator_value': '//input[@name="password]',
                          'timeout': 4}
        self.user_submit = {'element_name': '登录按钮',
                          'locator_type': 'xpath',
                          'locator_value': '//button[@id="submit]',
                          'timeout': 2}

    def username_input(self,username):
        self.input(self.user_name,username)
        logger.info('输入用户名：'+ str(username))

    def userpass_input(self,password):
        self.input(self.user_password,password)
        logger.info('输入用密码：' + str(password))

    def login_click(self):
        self.click(self.user_submit)
        logger.info('点击登录')

if __name__ == '__main__':
    crueet_path = os.path.dirname(__file__)
    driver_path = os.path.join(crueet_path, '../webdriver/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=driver_path)
    login = Login_Project_Test(driver)
    login.oper_url('http://127.0.0.1/zentao/user-login.html')
    login.username_input('admin')
    login.userpass_input('Pass1234')
    login.login_click()


