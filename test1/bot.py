#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter
from nonebot import on_command,on_regex
# Custom your logger
# 
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init()
#nonebot.load_plugins("test1/plugins/nonebot2-plugins")
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

nonebot.load_builtin_plugins("echo")

# Please DO NOT modify this file unless you know what you are doing!
# As an alternative, you should use command `nb` or modify `pyproject.toml` to load plugins
#nonebot.load_from_toml("pyproject.toml")
#nonebot.load_plugin("nonebot_plugin_heisi")
nonebot.load_plugin("nonebot_plugin_covid19_news")
nonebot.load_plugin("nonebot_plugin_picsearcher")
#nonebot.load_plugin("nonebot_plugin_vf")
nonebot.load_plugin("nonebot_plugin_lolmatch")
nonebot.load_plugins("test1/plugins")
nonebot.load_plugin("nonebot_plugin_heweather")
# nonebot_plugin_epicfree/__init__.py#L27


# nonebot_plugin_epicfree/__init__.py#L34
# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...
setcity = on_command('广州')
on_regex('(.*)天气|气温|多少度|几度')
on_regex('(.*)是?(星期|周)几')

if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
