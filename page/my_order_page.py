# 订单提交页面
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class MyOrderPage(BasePage):
    """订单提交-对象库层"""

    def __init__(self):
        super().__init__()

        self.submit_order_btn = (By.LINK_TEXT, '提交订单')  # 提交订单按钮

    def find_submit_order_btn(self):
        """定位提交订单按钮方法"""
        return self.find_element(self.submit_order_btn)


class MyOrderHandle(BaseHandle):
    """订单提交-操作层"""

    def __init__(self):
        self.my_order_page = MyOrderPage()

    def click_submit_order_btn(self):
        """点击提交订单按钮方法"""
        self.my_order_page.find_submit_order_btn().click()


class MyOrderProxy(object):
    """订单提交-业务层"""

    def __init__(self):
        self.my_order_handle = MyOrderHandle()

    def submit_order(self):
        """提交订单方法"""
        self.my_order_handle.click_submit_order_btn()
