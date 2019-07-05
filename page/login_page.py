# 登录页面
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    """登录-对象库层"""

    def __init__(self):
        super().__init__()

        self.username = (By.ID, 'username')  # 用户名
        self.password = (By.ID, 'password')  # 密码
        self.verify_code = (By.ID, 'verify_code')  # 验证码
        self.login_btn = (By.NAME, 'sbtbutton')  # 登录按钮

    def find_username(self):
        """定位用户名方法"""
        return self.find_element(self.username)

    def find_password(self):
        """定位密码方法"""
        return self.find_element(self.password)

    def find_verify_code(self):
        """定位验证码方法"""
        return self.find_element(self.verify_code)

    def find_login_btn(self):
        """定位登录按钮"""
        return self.find_element(self.login_btn)


class LoginHandle(BaseHandle):
    """登录-操作层"""

    def __init__(self):
        self.login_page = LoginPage()

    def input_username(self, username):
        """输入用户名方法"""
        self.input_text(self.login_page.find_username(), username)

    def input_password(self, pwd):
        """输入密码方法"""
        self.input_text(self.login_page.find_password(), pwd)

    def input_verify_code(self, code):
        """输入验证码方法"""
        self.input_text(self.login_page.find_verify_code(), code)

    def click_login_btn(self):
        """点击登录按钮方法"""
        self.login_page.find_login_btn().click()


class LoginProxy(object):
    """登录-业务层"""

    def __init__(self):
        self.login_handle = LoginHandle()

    def login(self, username, pwd, code):
        """登录方法"""

        # 输入用户名
        self.login_handle.input_username(username)
        # 输入密码
        self.login_handle.input_password(pwd)
        # 输入验证码
        self.login_handle.input_verify_code(code)
        # 点击登录按钮
        self.login_handle.click_login_btn()
