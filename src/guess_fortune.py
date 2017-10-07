from price_BOC import Price_BOC
from price_hexun import Price_HeXun

if __name__ == '__main__':
    BOC_price = Price_BOC()
    print(BOC_price.getExChangeRate("DOLLAR"))
    print(BOC_price.getMetalPrice("GOLD"))

    hexun_price = Price_HeXun()
    print(hexun_price.getExChangeRate("DOLLAR"))
    print(hexun_price.getMetalPrice("GOLD"))
