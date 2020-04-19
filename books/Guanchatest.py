#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import WebpageBook # 继承基类BaseFeedBook

# 返回此脚本定义的类名
def getBook():
    return Guanchatest

# 继承基类BaseFeedBook
class Guanchatest(WebpageBook):
    # 设定生成电子书的元数据
    title = u'观察者网测试版' # 设定标题
    __author__ = u'观察者' # 设定作者
    description = u'测试中 ' # 设定简介
    language = 'zh-cn' # 设定语言

    # 指定要提取的包含文章列表的主题页面链接
    # 每个主题是包含主题名和主题页面链接的元组
    feeds = [
        (u'毛', 'https://www.guancha.cn/MaoKeJi'),
        (u'余粮', 'https://www.guancha.cn/YuLiang'),
    ]