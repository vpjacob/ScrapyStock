# -*- coding: utf-8 -*-
import scrapy
import json

class XueqiuSpider(scrapy.Spider):
    name = 'xueqiu'
    # allowed_domains = ['xueqiu.com']
    allowed_domains = ['https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?size=1000&pid=-1&category=1']
    # start_urls = ['http://xueqiu.com/']

    def start_requests(self):
        cookie_str = 'Hm_lvt_1db88642e346389874251b5a1eded6e3=1582377654; device_id=24700f9f1986800ab4fcc880530dd0ed; cookiesu=641582377950631; remember=1; xq_a_token=ee5bf807d4594c3b362d4f0d97cf4eca28ff11db; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjEyMzIxNjQzMDYsImlzcyI6InVjIiwiZXhwIjoxNTgzODIxMDkxLCJjdG0iOjE1ODIzNzc5NzIzMTgsImNpZCI6ImQ5ZDBuNEFadXAifQ.ISWI0D3lCw3VGe8Cn-_fncfGY4z17hptJ_rabPdWql7-wjr6_u28TCn7-0wjizgTaUt7QFRDeKEManewP_LKPWrGAuxEIQOUus1AXIG8eeWIC0Ogr9oP2UNYkWbMR_X0lg94wmmgSth7ckZP8YMfSswmYFg8feAg0CFbj3b6oBjUhS7Pnzg1Pi_Px0YTxvV5GzpbuRfme3dXEf3n3WdKaAUSjx-9rg5bGC_eWjdA_mSaT8W8vkNc2JbAV2fJpN_wvPqkpH-B6yEyQhN0e3x5QrTHzJHM6jt7J0XLrQtKh8PN_wBNPvopxJuwMp_xoxfk6nV87V0JK9GpCGQcsxzgFw; xqat=ee5bf807d4594c3b362d4f0d97cf4eca28ff11db; xq_r_token=b5a54d51375325302b59a6bd81c74cd0ebbfd39c; xq_is_login=1; u=1232164306; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1582377975'
        cookies = {}

        for cookie in cookie_str.split(';'):
            key,value = cookie.split('=',1)
            cookies[key.strip()] = value.strip()

        yield scrapy.Request('https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?size=1000&pid=-1&category=1',cookies=cookies,callback=self.parse)



    def parse(self, response):
        stockes = json.loads(response.text)['data']['stocks']
        print(stockes)
