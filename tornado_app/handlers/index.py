#!/usr/bin/env python
# _*_ coding: utf8 _*_

import tornado.web

from wechat_sdk.exceptions import ParseError, OfficialAPIError
from wechat_sdk.basic import WechatBasic
from wechat_sdk.messages import EventMessage, WechatMessage


class IndexHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(IndexHandler, self).__init__(application, request, **kwargs)
        self.logger = self.application.logger
        self.wechat_api = WechatBasic(conf=self.application.wechat_conf)

    def get(self):
        signature = self.get_argument("signature", "")
        timestamp = self.get_argument("timestamp", "")
        nonce = self.get_argument("nonce", "")
        echostr = self.get_argument("echostr", "")
        if self.wechat_api.check_signature(signature, timestamp, nonce):
            self.finish(echostr)
        self.finish("")

    def post(self):
        """
        接收微信推送消息
        :return:
        """
        # 收到消息后直接回复，防止微信多次推送
        self.finish("")
        try:
            self.wechat_api.parse_data(self.request.body)
        except ParseError, e:
            self.logger.error(e.message)
            return
        try:
            message = self.wechat_api.message
            if message.type == "subscribe":
                self.wechat_api.send_text_message(message.source, u"欢迎关注！")
                # TODO: 将微信openId与userId绑定
            elif message.type == "unsubscribe":
                # TODO: 删除微信openId与userId绑定关系
                pass
            elif message.type == "text":
                print message.content
        except OfficialAPIError, e:
            self.logger.error(e.errcode, e.errmsg)
