# -*- coding: utf-8 -*-
import scrapy


class A50etfesSpider(scrapy.Spider):
    name = '50etfes'
    allowed_domains = ['http://vip.stock.finance.sina.com.cn']
    start_urls = [
        'http://vip.stock.finance.sina.com.cn/corp/go.php/vII_NewestComponent/indexid/399285.phtml',  # 物联网50
        "http://vip.stock.finance.sina.com.cn/corp/go.php/vII_NewestComponent/indexid/399284.phtml",  # AI 50
        'http://vip.stock.finance.sina.com.cn/corp/go.php/vII_NewestComponent/indexid/399283.phtml',  # 机器人50
        'http://vip.stock.finance.sina.com.cn/corp/go.php/vII_NewestComponent/indexid/399088.phtml',  # 深创100
        'http://vip.stock.finance.sina.com.cn/corp/go.php/vII_NewestComponent/indexid/399282.phtml',  # 大数据50
    ]

    def parse(self, response):
        daima_date = response.xpath('//tr/td/div/text()').extract()
        names = response.xpath('//tr/td/div/a/text()').extract()
        stock_urls = response.xpath('//tr/td/div/a/@href').extract()

        daimas = []
        join_dates = []
        type = ''

        '',  # 物联网50
        "",  # AI 50
        '',  # 机器人50
        '',  # 深创100
        '',  # 大数据50


        if response.url == 'http://vip.stock.finance.sina.com.cn/corp/go.php/vII_NewestComponent/indexid/399285.phtml':
            type = '物联网50'
        elif response.url == 'http://vip.stock.finance.sina.com.cn/corp/go.php/vII_NewestComponent/indexid/399284.phtml':
            type = 'AI 50'
        elif response.url == 'http://vip.stock.finance.sina.com.cn/corp/go.php/vII_NewestComponent/indexid/399283.phtml':
            type = '机器人50'
        elif response.url == 'http://vip.stock.finance.sina.com.cn/corp/go.php/vII_NewestComponent/indexid/399088.phtml':
            type = '深创100'
        elif response.url == 'http://vip.stock.finance.sina.com.cn/corp/go.php/vII_NewestComponent/indexid/399282.phtml':
            type = '大数据50'

        for idx, item in enumerate(daima_date):

            if idx % 2 == 0:
                daimas.append(item)
            else:
                join_dates.append(item)

        for name, stock_url, daima, join_date in zip(names, stock_urls, daimas, join_dates):
            yield {
                "daima": daima,
                "name": name,
                "stock_url": stock_url,
                "join_date": join_date,
                "type":type,
            }
