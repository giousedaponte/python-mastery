# stock.py
import csv

class Stock:
    __slots__ = ('name', '_shares', '_price')
    _types = (str, int, float)
    def __init__(self, name, shares, 
price):
        self.name = name
        self.shares = shares
        self.price = price
    
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    
    @property
    def cost(self):
        return self.shares * self.price
    
    @property
    def shares(self):
        return self._shares
    @shares.setter
    def shares(self, value,):
        if not isinstance(value, self._types[1]):
            raise TypeError('Expected type: %s' % (self._types[1].__name__))
        if value < 0:
            raise ValueError('shares must be >= 0')
        self._shares = value

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError('Expected type: %s' % (self._types[2].__name__))
        if value < 0:
            raise ValueError('price must be >= 0')
        else:
            self._price = value

    def sell(self, nshares):
        self.shares -= nshares     
   
if __name__ == '__main__':
    from decimal import Decimal
    # from reader import read_csv_as_instance
    # import tableformat
    # portfolio = read_csv_as_instance('Data/portfolio.csv', Stock)
    # tableformat.print_table(portfolio, ['name','shares','price'])
    s = Stock('GOOG', 100, 490.1)
    print(s.cost)

    class DStock(Stock):
        _types = (str, int, Decimal)

    d = DStock('IBM', 100, Decimal('91.2'))
    
