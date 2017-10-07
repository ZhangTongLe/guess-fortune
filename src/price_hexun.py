#!/usr/bin/env python  
#encoding:utf-8  
"""price_hexun.py 获取和讯网最新的价格信息"""

from web_common import download
from price_object import Price_Object

#!解析和讯网黄金价格
def getHexunGoldPrice(webpage):
    bFindFlag = False

    f = open(webpage)
    lines = f.readlines()
    for eachLine in lines:
        #返回黄金价格
        if bFindFlag:
            f.close()
            return float(eachLine.strip()[eachLine.strip().index('>') + 1 : eachLine.strip().rindex('<')])

        #找到上海黄金交易所行情的黄金，下一行是最新价格
        if '<span>Au(T+D)</span>' in eachLine:
            bFindFlag = True

    f.close()
    return -1

#!获取和讯网金融信息
class Price_HeXun(Price_Object):
    #!获取最新贵金属价格
    def getMetalPrice(self, metalType):
        if metalType == "GOLD":
            self.fGoldPrice = download('http://gold.hexun.com/hjxh/', getHexunGoldPrice)
            return self.fGoldPrice

