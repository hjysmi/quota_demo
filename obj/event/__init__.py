# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 20:07
# @Author  : xuetong1
# @Email   : 857417740@qq.com
# @File    : __init__.py.py
# @Software: PyCharm
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Event(object):
    """
    所有事件数据对象的父类
    """

    @classmethod
    def cls_key(cls) -> int:
        return hash(cls)

    def __post_init__(self):
        self._key = self.cls_key()

    @property
    def key(self) -> int:
        return self._key


@dataclass
class Order(Event):
    pass


@dataclass
class Cancel(Event):
    pass


@dataclass
class Trade(Event):
    pass


@dataclass
class Tick(Event):
    pass


@dataclass
class OrderBook(Event):
    pass


@dataclass
class Kline(Event):
    pass
