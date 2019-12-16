# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 20:04
# @Author  : xuetong1
# @Email   : 857417740@qq.com
# @File    : __init__.py.py
# @Software: PyCharm
import typing as t
from quota_demo.obj import event as e
from collections import defaultdict

KeyType = t.TypeVar(name="KeyType", bound=int)
EventType = t.TypeVar(name="EventType", bound=e.Event)
CallBackType = t.Callable[[], None]


class CallBack(object):
    """
    manage the callbacks and event
    """
    _callbacks: t.Dict[KeyType, t.List[CallBackType]]

    def __init__(self):
        self._callbacks = defaultdict(list)
        pass

    def bind(self, key: KeyType, callback: CallBackType):
        call_back_list = self._callbacks[key]
        if callback not in call_back_list:
            call_back_list.append(callback)
        else:
            raise ValueError("call back function only be promised register once.")
        pass

    def unbind(self, key: KeyType, callback: CallBackType):
        call_back_list = self._callbacks[key]
        if callback in call_back_list:
            call_back_list.remove(callback)
        else:
            raise ValueError("call back function only be promised register once.")
        pass

    def route(self, event: EventType):
        if event.key in self._callbacks:
            for cb in self._callbacks:
                cb(event)
        pass

    pass


if __name__ == '__main__':
    KeyType = "helo"
    print(KeyType)
    pass
