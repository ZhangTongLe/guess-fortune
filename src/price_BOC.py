#!/usr/bin/env python  
#encoding:utf-8  
"""price_BOC.py 获取中国银行最新的价格信息"""
from web_common import download

#!解析中国银行美元现汇买入价
def getBOCDollarExchangeRate(webpage):
    bFindFlag = False
    #!打开网页
    f = open(webpage, encoding='utf-8')
    lines = f.readlines()
    for eachLine in lines:
        #返回美元现汇买入价
        if bFindFlag:
            f.close()
            return float(eachLine.strip()[eachLine.strip().index('>') + 1 : eachLine.strip().rindex('<')])

        #找到美元信息列
        if '<td>美元</td>' in eachLine:
            bFindFlag = True

    f.close()
    return -1

#!获取中国银行金融信息
class Price_BOC:
    fDollarRate = 0

    #!获取最新美元汇率
    def getExChangeRate(self, moneyType):
        if moneyType == "DOLLAR":
            self.fDollarRate = download('http://www.boc.cn/sourcedb/whpj/index.html', getBOCDollarExchangeRate)
            return self.fDollarRate
