# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook


class StockPipeline(object):

    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append([
            '股票名称',
            '代码',
            '加入etf时间',
            'etf板块名称',
            '股票网址'
        ])

    def process_item(self, item, spider):
        line = [
            item['name'],
            item['daima'],
            item['join_date'],
            item['type'],
            item['stock_url']
        ]
        self.ws.append(line)

        return item

    def close_spider(self, spider):
        self.wb.save('etf.xlsx')  # 保存xlsx文件
