#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import WebpageBook

def getBook():
    return Guancha3

class Guancha3(WebpageBook):
    title                 = u'观察者网测试2'
    description           = u'嘤嘤嘤'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile = "mh_default.gif"
    coverfile = "cv_default.jpg"
    oldest_article        = 7
    feeds = [
            (u'毛', 'https://www.guancha.cn/MaoKeJi')
           ]