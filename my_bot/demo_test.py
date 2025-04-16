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
from botpy.message import Message
from botpy import logging
from botpy.message import GroupMessage, Message

from botpy.ext.cog_yaml import read


test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

_log = logging.get_logger()


class MyClient(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 启动成功!")

    # 回复群聊信息
    async def on_group_at_message_create(self, message: GroupMessage):
        messageResult = await message._api.post_group_message(
            group_openid=message.group_openid,
            msg_type=0,
            msg_id=message.id,
            content=f"这里是初号机（测试版）:{message.content}")
        _log.info(messageResult)


if __name__ == '__main__':

    intents = botpy.Intents(public_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=test_config["appid"], secret=test_config["secret"])
