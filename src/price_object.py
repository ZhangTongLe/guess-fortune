#!获取金融信息
class Price_Object:
    #金融数据
    fGoldPrice = -1
    fDollarRate = -1
    #下一个类(职责链)
    classPriceNext = None

    def __init__(self):
        self.fGoldPrice = -1
        self.fDollarRate = -1

    #!获取最新美元汇率
    def getExChangeRate(self, moneyType):
        if self.fDollarRate == -1 and self.classPriceNext != None:
            return self.classPriceNext.getExChangeRate(moneyType)
        else:
            return self.fDollarRate

    #!获取最新贵金属价格
    def getMetalPrice(self, metalType):
        if self.fGoldPrice == -1 and self.classPriceNext != None:
            return self.classPriceNext.getMetalPrice(metalType)
        else:
            return self.fGoldPrice

    #!设置职责链的下一个指向类
    def SetNextPriceObject(self, price_object):
        self.classPriceNext = price_object
