# 商品详情页面
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle
from utils import DriverUtil


class GoodsDetailPage(BasePage):
    """商品详情-对象库层"""

    def __init__(self):
        super().__init__()

        self.join_cart_btn = (By.ID, 'join_cart')  # 添加购物车按钮
        self.join_cart_result = (By.CSS_SELECTOR, '.conect-title>span')  # 添加购物车结果

    def find_join_cart_btn(self):
        """定位添加购物车按钮方法"""
        return self.find_element(self.join_cart_btn)

    def find_join_cart_result(self):
        """定位添加购物车结果方法"""
        return self.find_element(self.join_cart_result)


class GoodsDetailHandle(BaseHandle):
    """商品详情-操作层"""

    def __init__(self):
        self.goods_detail_page = GoodsDetailPage()

    def click_join_cart_btn(self):
        """点击添加购物车按钮方法"""
        self.goods_detail_page.find_join_cart_btn().click()

    def get_join_cart_result(self):
        """获取添加购物车结果方法"""
        return self.goods_detail_page.find_join_cart_result().text


class GoodsDetailProxy(object):
    """商品详情-业务层"""

    def __init__(self):
        self.goods_detail_handle = GoodsDetailHandle()

    def join_goods_to_cart(self):
        """添加商品到购物车方法"""
        self.goods_detail_handle.click_join_cart_btn()

    def get_add_cart_result(self, expect):
        """获取添加购物车结果方法"""

        # 切换 frame 获取弹窗结果
        driver = DriverUtil.get_driver()
        driver.switch_to.frame(driver.find_element_by_css_selector('iframe'))

        result = self.goods_detail_handle.get_join_cart_result()
        return expect == result
