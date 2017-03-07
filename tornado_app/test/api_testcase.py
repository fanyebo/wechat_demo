#!/usr/bin/env python
# _*_ coding: utf8 _*_

import requests
import time


def main():
    template = ("<xml>"
                "<ToUserName>oKzzyt8fCLyYYIMExtW8Cemj_MQM</ToUserName>"
                "<FromUserName>gh_3ba39059148b</FromUserName>"
                "<CreateTime>%s</CreateTime>"
                "<MsgType>text</MsgType>"
                "<Content>send a text message to server</Content>"
                "<MsgId>1234567890123456</MsgId>"
                "</xml>")
    data = template % str(int(time.time()))
    result = requests.post("http://127.0.0.1:8080", data=data)
    print result.text


if __name__ == '__main__':
    main()
