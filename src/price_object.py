#!获取中国银行金融信息
class Price_Object:
    fGoldPrice = -1
    fDollarRate = -1

    def __init__(self):
        self.fGoldPrice = -1
        self.fDollarRate = -1

    #!获取最新美元汇率
    def getExChangeRate(self, moneyType):
        return self.fDollarRate

    #!获取最新贵金属价格
    def getMetalPrice(self, metalType):
        return self.fGoldPrice
