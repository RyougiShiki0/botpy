#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：botpy 
@File    ：demo_test.py.py
@IDE     ：PyCharm 
@Author  ：RyougiShiki
@Date    ：2025/4/15 下午5:09 
"""
import os

import botpy
from botpy import logging

from botpy.ext.cog_yaml import read

test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

_log = logging.get_logger()


class MyBot(botpy.Client):
    a = 10


if __name__ == '__main__':
    print(111)
