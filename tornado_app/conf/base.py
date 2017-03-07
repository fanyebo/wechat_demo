#!/usr/bin/env python
# _*_ coding: utf8 _*_

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

WECHAT_CONF = {
    "appid": "wxe02fbc376f978ba6",
    "appsecret": "06cb5cdc4cb02ae8a1275bddeb620ac5",
    "token": "fanyebofkdls",
    "encrypt_mode": "normal"
}

BASE_SETTINGS = {
    "debug": False,

    "COOKIE_SECRET": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",

    # 模板目录
    "template_path": os.path.join(BASE_DIR, "templates"),

    # 静态文件目录
    "static_path": os.path.join(BASE_DIR, "static"),

}
