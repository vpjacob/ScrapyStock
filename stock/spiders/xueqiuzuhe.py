# -*- coding: utf-8 -*-
import scrapy
import re


class XueqiuzuheSpider(scrapy.Spider):
    name = 'xueqiuzuhe'
    allowed_domains = ['xueqiu.com']
    urls = []


    def start_requests(self):

        for item in ['ZH1885214', 'ZH2033319', 'ZH119095', 'ZH000782', 'ZH247586', 'ZH187065', 'ZH813520', 'ZH088330',
                     'ZH001659', 'ZH013867', 'ZH187068', 'ZH142207', 'ZH2088035', 'ZH477034', 'ZH078352', 'ZH232330',
                     'ZH500270', 'ZH221395', 'ZH563897', 'ZH374379', 'ZH693860', ]:
            yield scrapy.Request('https://xueqiu.com/P/' + item, callback=self.parse_url)



    def parse_url(self,response):
        res_str = response.text
        last_rb_id = re.findall(r"\"last_rb_id\"\:(.+?),", res_str)
        '693860'
        symbol = re.findall(r"var symbol = \'ZH(.+?)\'\;", res_str)

        new_urls = 'https://xueqiu.com/cubes/rebalancing/show_origin.json?rb_id={}&cube_symbol=ZH{}'.format(
            last_rb_id[0], symbol[0])
        print(symbol,last_rb_id,new_urls)
        # self.parse_body(new_urls)



