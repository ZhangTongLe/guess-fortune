from price_BOC import Price_BOC
from price_hexun import Price_HeXun

if __name__ == '__main__':
    dollar_price = Price_BOC()
    print(dollar_price.getExChangeRate("DOLLAR"))

    gold_price = Price_HeXun()
    print(gold_price.getMetalPrice("GOLD"))
