# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 20:08
# @Author  : xuetong1
# @Email   : 857417740@qq.com
# @File    : test___init__.py
from unittest import TestCase
from quota_demo.obj import event as e
from quota_demo import callback as cb


def _order(order: e.Order):
    print("order:", order)


def _trade(trade: e.Trade):
    print("trade:", trade)


# @Software: PyCharm
class TestCallBack(TestCase):
    def test_demo(self):
        x = cb.CallBack()
        x.bind(e.Order.cls_key(), _order)
        x.bind(e.Trade.cls_key(), _trade)
        x.route(e.Order())
        x.route(e.Trade())
        x.unbind(e.Order.cls_key(), _order)
        x.route(e.Order())
        x.route(e.Trade())
    pass


if __name__ == '__main__':
    print(e.Order.cls_key())
    pass



