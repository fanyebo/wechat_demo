#!/usr/bin/env python
# _*_ coding: utf8 _*_


MESSAGE_HANDLER_TYPE = {}


def handler_for_type(type):
    def register(f):
        MESSAGE_HANDLER_TYPE[type] = f
        return f

    return register


class BaseMessageHandler(object):
    def __init__(self, message):
        self.message = message


@handler_for_type("text")
class TextMessageHandler(BaseMessageHandler):
    def action(self):
        print self.message.content


@handler_for_type("subscribe")
class SubscribeMessageHandler(BaseMessageHandler):
    def action(self):
        print type(self.message.source)
        print self.message.source, "订阅了公众号"


@handler_for_type("unsubscribe")
class SubscribeMessageHandler(BaseMessageHandler):
    def action(self):
        print type(self.message.source)
        print self.message.source, "取消订阅"


@handler_for_type("image")
class ImageMessageHandler(BaseMessageHandler):
    def action(self):
        print self.message.picurl


@handler_for_type("location")
class LocationMessageHandler(BaseMessageHandler):
    def action(self):
        print self.message.label


@handler_for_type("voice")
class VoiceMessageHandler(BaseMessageHandler):
    def action(self):
        print self.message.media_id
