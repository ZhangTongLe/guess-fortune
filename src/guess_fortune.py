from price_BOC import Price_BOC
from price_hexun import Price_HeXun

if __name__ == '__main__':
    BOC_price = Price_BOC()
    hexun_price = Price_HeXun()

    BOC_price.SetNextPriceObject(hexun_price)

    print(BOC_price.getExChangeRate("DOLLAR"))
    print(BOC_price.getMetalPrice("GOLD"))

    #print(hexun_price.getExChangeRate("DOLLAR"))
    #print(hexun_price.getMetalPrice("GOLD"))

    
