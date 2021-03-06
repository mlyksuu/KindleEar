#!/usr/bin/env python
# -*- coding:utf-8 -*-
#抓取传送门网站http://chuansongme.com/的特定微信公众号文章列表，
#将title/description/feeds稍加修改后即可用于其他公众号
#feeds里也可以直接增加几个账号
import datetime
from bs4 import BeautifulSoup
from lib.urlopener import URLOpener
from base import BaseFeedBook,string_of_tag

def getBook():
    return Guancha2

class Guancha2(BaseFeedBook):
    title                 = u'观察者网测试2'
    description           = u'嘤嘤嘤'
    language              = 'zh-cn' #TED中英文双语，为en则能英文查词
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    network_timeout       = 60
    oldest_article        = 7
    #设置为True排版也很好（往往能更好的剔除不相关内容），
    #除了缺少标题下的第一幅图
    fulltext_by_readability = False
    keep_only_tags = [dict(name='div', attrs={'id':'page-content'})]
    remove_classes = ['page-toolbar']

    feeds = [
        (u'毛', 'https://www.guancha.cn/MaoKeJi'),
        (u'余粮', 'https://www.guancha.cn/YuLiang'),
    ]

    def ParseFeedUrls(self):
        """ return list like [(section,title,url,desc),..] """
        urls = []
        for feed in self.feeds:
            feedtitle,url = feed[0],feed[1]
            opener = URLOpener(self.host, timeout=self.timeout)
            result = opener.open(url)
            if result.status_code != 200 or not result.content:
                self.log.warn('fetch webpage failed(%d):%s.' % (result.status_code, url))
                continue

            if self.feed_encoding:
                try:
                    content = result.content.decode(self.feed_encoding)
                except UnicodeDecodeError:
                    content = AutoDecoder(False).decode(result.content,opener.realurl,result.headers)
            else:
                content = AutoDecoder(False).decode(result.content,opener.realurl,result.headers)

            soup = BeautifulSoup(content, 'lxml')
            for article in soup.find_all('li', attrs={'style':'height: 215px;'}):
				orz = article.find_all('h4', attrs={'class':'module-title'})
                title = orz.find(name='a').string # 获取文章标题
                if not title:
                    continue

                #获取发布时间
                pubdate = article.find(name='span').string
                if not pubdate:
                    continue
                try:
                    pubdate = datetime.datetime.strptime(pubdate.string, '%Y-%m-%d %H:%M:%S')
                except Exception as e:
                    self.log.warn('parse pubdate failed for [%s] : %s'%(url,str(e)))
                    continue

                #确定文章是否需要推送，时区固定为北京时间
                tnow = datetime.datetime.utcnow()+datetime.timedelta(hours=8)
                delta = tnow - pubdate
                if self.oldest_article > 0 and delta.days > self.oldest_article:
                    continue

                href = title['href'] if title['href'].startswith('http') else self.urljoin(url,title['href'])

                urls.append((feedtitle,string_of_tag(title),href,None))

        return urls