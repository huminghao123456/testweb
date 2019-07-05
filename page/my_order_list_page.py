# 我的订单列表
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class MyOrderListPage(BasePage):
    """我的订单列表-对象库层"""

    def __init__(self):
        super().__init__()

        self.wait_for_pay = (By.LINK_TEXT, '待付款')  # 待付款
        self.pay_now = (By.LINK_TEXT, '立即支付')  # 立即支付

    def find_wait_for_pay(self):
        """定位待支付方法"""
        return self.find_element(self.wait_for_pay)

    def find_pay_now(self):
        """定位立即支付方法"""
        return self.find_element(self.pay_now)


class MyOrderListHandle(BaseHandle):
    """我的订单列表-操作层"""

    def __init__(self):
        self.my_order_list_page = MyOrderListPage()

    def click_wait_for_pay(self):
        """点击待支付方法"""
        self.my_order_list_page.find_wait_for_pay().click()

    def click_pay_now(self):
        """点击立即支付方法"""
        self.my_order_list_page.find_pay_now().click()


class MyOrderListProxy(object):
    """我的订单列表-业务层"""

    def __init__(self):
        self.my_order_list_handle = MyOrderListHandle()

    def go_to_order_pay(self):
        """调整订单支付页面方法"""
        self.my_order_list_handle.click_wait_for_pay()
        self.my_order_list_handle.click_pay_now()
