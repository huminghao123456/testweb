# 购物车页面
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class CartPage(BasePage):
    """购物车-对象库"""

    def __init__(self):
        super().__init__()

        self.check_all = (By.CLASS_NAME, 'checkCartAll')  # 全选复选框
        self.go_balance = (By.LINK_TEXT, '去结算')  # 去结算按钮

    def find_check_all(self):
        """定位全选复选框方法"""
        return self.find_element(self.check_all)

    def find_go_balance(self):
        """定位去结算按钮方法"""
        return self.find_element(self.go_balance)


class CartHandle(BaseHandle):
    """购物车-操作层"""

    def __init__(self):
        self.cart_page = CartPage()

    def click_check_all(self):
        """点击全选复选框方法"""

        check_all = self.cart_page.find_check_all()
        # 判断全选按钮为非选中状态
        if not check_all.is_selected():
            check_all.click()

    def click_go_balance(self):
        """点击去结算按钮方法"""
        self.cart_page.find_go_balance().click()


class CartProxy(object):
    """购物车-业务层"""

    def __init__(self):
        self.cart_handle = CartHandle()

    def go_to_check_order(self):
        """跳转订单确认页面方法"""
        # 确认全选
        self.cart_handle.click_check_all()
        # 点击去结算
        self.cart_handle.click_go_balance()
