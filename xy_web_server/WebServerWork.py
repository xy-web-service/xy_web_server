# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "WebServerWork"
"""
  * @File    :   WebServerWork.py
  * @Time    :   2023/04/25 23:03:56
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
"""

import xy_web_server
from .Work import Work
from .Settings.Settings import Settings


class WebServerWork(Work):
    settings: Settings | None = Settings()

    def __init__(self):
        self.prog = xy_web_server.__name__
        self.description = f""">>>>>>>>>>>> {xy_web_server.__name__} - v{xy_web_server.__version__} <<<<<<<<<<<<<"""
