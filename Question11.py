def pushme(stock, item):
    stock = stock.append(item)


def popme(stock):
    stock = stock.pop()


stk = []
item = "item"
pushme(stk, item)
popme(stk)
