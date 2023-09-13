# stock.py
import csv

class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, 
price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares     
   
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

if __name__ == '__main__':
    from reader import read_csv_as_instance
    import tableformat
    portfolio = read_csv_as_instance('Data/portfolio.csv', Stock)
    tableformat.print_table(portfolio, ['name','shares','price'])
    