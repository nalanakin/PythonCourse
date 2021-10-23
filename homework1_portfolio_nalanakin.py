from random import uniform

class Portfolio (object):

    def __init__ (self):
        self.Cash = 0
        self.Stock = {}
        self.MutualFund = {}
        self.Bond = {}
        self.History = []

    def addCash (self, amount):
        self.Cash += float(amount)
        log = f"You have {self.Cash}."
        self.History.append(log)
        print(log)
        return self.Cash

    def withdrawCash (self, amount):
        self.Cash -= float(amount)
        log = f"Cash remained at your portfolio {self.Cash}."
        self.History.append(log)
        print(log)
        return self.Cash

    def buyStock(self, amount, stock):
        self.Cash -= float(stock.price)*amount
        if stock.symbol in self.Stock:
            self.Stock[stock.symbol] += amount
        else:
            self.Stock[stock.symbol] = amount
        log = f"{amount} new stock {stock.symbol} added to the portfolio."
        self.History.append(log)
        print(log)

    def sellStock (self, stock, amount):
        cost = stock.pricetosell()
        self.Cash += cost*amount
        self.Stock[stock.symbol] -= amount
        log = f"{amount} stock {stock.symbol} was sold."
        self.History.append(log)
        print(log)

    def buyMutualFund(self, shares, mutualfund):
        self.Cash -= float(shares)
        if mutualfund.symbol in self.MutualFund:
            self.MutualFund[mutualFund.symbol] += shares
        else:
            self.MutualFund[mutualfund.symbol] = shares
        log = f"{shares} mutual fund {mutualfund.symbol} was added"
        self.History.append(log)
        print(log)

    def sellMutualFund(self, shares, mutualfund):
        self.Cash += shares
        self.MutualFund[mutualfund.symbol] -= shares
        log = f"{shares} mutual fund {mutualfund.symbol} was sold."
        self.History.append(log)
        print(log)

    def showhistory(self):
        hist = "\n".join(self.History)
        print(f"Your history: {hist}")

    def __str__ (self):
        return (f"""
        Cash:{self.Cash},
        Stock: {self.Stock},
        MutualFund: {self.MutualFund},
        Bond: {self.Bond}.""")

class Asset(object):
    def __init__(self, symbol, price=1):
        self.price = price
        self.symbol = symbol

class Stock(Asset):
    def pricetosell(self):
        s_pricetosell = uniform(.5, 1.5)*self.price #price'ı nasıl ekleyeceğim, bulmam gerek
        return s_pricetosell

class MutualFund(Asset):
    def pricetosell(self):
        mf_pricetosell = uniform(0.9, 1.2)
        return mf_pricetosell

class Bond(Asset):
    pass


#parantezin içi boş kalmalı
portfolio = Portfolio()

portfolio.addCash(300.50)

s = Stock("HFH", price=20)

portfolio.buyStock(5, s)
portfolio.sellStock(s, 1)

mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")

portfolio.buyMutualFund(10.3, mf1)
portfolio.sellMutualFund(3, mf1)
portfolio.buyMutualFund(2, mf2)

portfolio.withdrawCash(50)

print(str(portfolio))
print(portfolio.showhistory())
