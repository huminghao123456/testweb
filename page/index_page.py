# 首页页面
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class IndexPage(BasePage):
    """首页-对象库层"""

    def __init__(self):
        super().__init__()  # 获取父类的初始化方法

        self.login_link = (By.LINK_TEXT, '登录')  # 登录链接
        self.search = (By.ID, 'q')  # 搜索框
        self.search_btn = (By.CSS_SELECTOR, '[type="submit"]')  # 搜索按钮
        self.my_cart = (By.CLASS_NAME, 'share-shopcar-index')  # 我的购物车
        self.my_order_list_link = (By.LINK_TEXT, '我的订单')  # 我的订单链接

    def find_login_link(self):
        """定位登录链接方法"""
        return self.find_element(self.login_link)

    def find_search(self):
        """定位搜索框方法"""
        return self.find_element(self.search)

    def find_search_btn(self):
        """定位搜索按钮方法"""
        return self.find_element(self.search_btn)

    def find_my_cart(self):
        """定位我的购物车方法"""
        return self.find_element(self.my_cart)

    def find_my_order_list_link(self):
        """定位我的订单链接方法"""
        return self.find_element(self.my_order_list_link)


class IndexHandle(BaseHandle):
    """首页-操作层"""

    def __init__(self):
        self.index_page = IndexPage()  # 元素定位对象

    def click_login_link(self):
        """点击登录链接方法"""
        self.index_page.find_login_link().click()

    def input_search(self, kw):
        """输入搜索内容方法"""
        self.input_text(self.index_page.find_search(), kw)

    def click_search_btn(self):
        """点击搜索按钮方法"""
        self.index_page.find_search_btn().click()

    def click_my_cart(self):
        """点击我的购物车方法"""
        self.index_page.find_my_cart().click()

    def click_my_order_list_link(self):
        """点击我的订单链接方法"""
        self.index_page.find_my_order_list_link().click()


class IndexProxy(object):
    """首页-业务层"""

    def __init__(self):
        self.index_handle = IndexHandle()  # 元素操作对象

    def go_to_login(self):
        """跳转登录页面方法"""
        self.index_handle.click_login_link()

    def go_to_goods_search(self, kw):
        """跳转商品搜索页面方法"""
        # 输入要搜索的内容
        self.index_handle.input_search(kw)
        # 点击搜索
        self.index_handle.click_search_btn()

    def go_to_cart(self):
        """跳转购物车页面方法"""
        self.index_handle.click_my_cart()

    def go_to_my_order_list(self):
        """跳转我的订单列表页面方法"""
        self.index_handle.click_my_order_list_link()
