#!/usr/bin/env python
# _*_ coding: utf8 _*_

import sys
import logging
import tornado.web

from urls import GLOBAL_URLS
from conf.base import BASE_SETTINGS, WECHAT_CONF

sys.path.append("../")
from wechat_sdk.core.conf import WechatConf


class ServerApplication(tornado.web.Application):
    def __init__(self, handlers=None, default_host="", transforms=None, **settings):
        super(ServerApplication, self).__init__(handlers=handlers, default_host=default_host, transforms=transforms,
                                                **settings)

        self.wechat_conf = WechatConf(**WECHAT_CONF)

        # 日志设置
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(message)s")
        handler.setFormatter(formatter)
        self.logger = logging.getLogger()
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    application = ServerApplication(GLOBAL_URLS, **BASE_SETTINGS)
    application.listen(8080, "0.0.0.0")
    application.logger.info("server starting at 0.0.0.0:8080...")
    tornado.ioloop.IOLoop.instance().start()
