from selenium import webdriver
import os,time
from selenium.webdriver.common.by import By

crueet_path = os.path.dirname(__file__)
login_path = os.path.join(crueet_path,'../webdriver/chromedriver.exe')

class Login_Project_Test:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=login_path)
        self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        self.driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')
        self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        self.user_name = self.driver.find_element(By.ID,'account')
        self.user_password = self.driver.find_element(By.NAME, 'password')
        self.user_submit = self.driver.find_element(By.ID, 'submit')

    def username_input(self,username):
        self.user_name.send_keys(username)

    def userpass_input(self,password):
        self.user_password.send_keys(password)

    def login_click(self):
        self.user_submit.click()

if __name__ == '__main__':
    login = Login_Project_Test()
    login.username_input('admin')
    login.userpass_input('Pass1234')
    login.login_click()


