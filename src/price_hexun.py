#!/usr/bin/env python  
#encoding:utf-8  
"""price_hexun.py 获取和讯网最新的价格信息"""

from urllib.request import urlretrieve

#!抓取网页数据
def download(url, process):  
    try:
        retval = urlretrieve(url)[0]
    except IOError as error:
        print(error)
        retval = None
        return -1

    if retval:
        return process(retval)  

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

#!解析和讯网黄金价格
def getHexunDollarExchangeRate(webpage):
    f = open(webpage)
    lines = f.readlines()
    for eachLine in lines:
        print(eachLine)

    f.close()
    return -1

#!获取最新贵金属价格
def getMetalPrice(metalType):
    if metalType == "GOLD":
        return download('http://gold.hexun.com/hjxh/', getHexunGoldPrice)

#!获取最新美元汇率
def getExChangeRate(moneyType):
    if moneyType == "DOLLAR":
        return download('http://forex.hexun.com/rmbhl/', getHexunDollarExchangeRate)

if __name__ == '__main__':  
    print(getMetalPrice("GOLD"))
    #print(getExChangeRate("DOLLAR"))