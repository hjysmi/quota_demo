# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 19:20
# @Author  : xuetong1
# @Email   : 857417740@qq.com
# @File    : __init__.py.py
# @Software: PyCharm


class DataCenter(object):
    """
    数据接收，存储读取中心
    """

    def re_x(self):
        """
        请求函数
        """
        pass

    def on_x(self):
        """
        监听/回调函数
        """
        pass


class GeteWay(object):
    """
    中间网关、代理交易，对接行情和交易
    """

    def re_x(self):
        """
        请求
        """
        pass

    def on_x(self):
        """
        回调函数
        """
        pass

class Broker(object):
    """
    客户维护，交易，行情
    """
    def re_x(self):
        """
        请求
        """
        pass

    def on_x(self):
        """
        回调函数
        """
        pass


class Simulation(object):
    """
    模拟交易所，产生行情和交易撮合
    """


if __name__ == '__main__':
    pass
