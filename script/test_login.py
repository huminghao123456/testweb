# 登录测试
import time
import unittest
import json
import config
import logging

from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtil
from parameterized import parameterized


def build_login_data():
    # 初始化一个空列表
    login_data_list = list()
    with open(config.BASE_DIR + '/data/login_data.json', encoding='utf-8') as f:
        data = json.load(f)
        data_list = data.get('test_login')
        for item in data_list:
            # 列表添加获取的每一条数据
            login_data_list.append((item.get('username'),
                                    item.get('password'),
                                    item.get('code'),
                                    item.get('expect')))
        print(login_data_list)
        return login_data_list


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象

        cls.index_proxy = IndexProxy()  # 首页业务操作对象
        cls.login_proxy = LoginProxy()  # 登录业务操作对象

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setUp(self) -> None:
        # 打开首页
        self.driver.get('http://www.tpshop.com/')
        # 点击登录
        self.index_proxy.go_to_login()

    @parameterized.expand(build_login_data())
    def test_login(self, username, pwd, code, expect):
        """登录测试"""
        # print('username={} pwd={} code={} expect={}'.format(username, pwd, code, expect))

        # 通过日志模块的 info 级别日志输出替换原来的打印信息
        logging.info('username={} pwd={} code={} expect={}'.format(username, pwd, code, expect))

        # 登录
        self.login_proxy.login(username, pwd, code)

        # 设置睡眠,等待页面标题的加载
        time.sleep(2)
        # 获取页面标题
        title = self.driver.title

        # 断言判断测试结果
        self.assertIn(expect, title)
