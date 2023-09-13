# reader.py

import csv
import collections.abc

class Data(collections.abc.Sequence):
    def __init__(self):
        # Each value is a list with all of the values (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []
        
    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        return { 'route': self.routes[index],
                 'date': self.dates[index],
                 'daytype': self.daytypes[index],
                 'rides': self.numrides[index] }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])

def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file into a list of dicts with column type conversion
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = { name: func(val) for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records

def read_csv_as_columns(filename, types):
    myData = Data()
    dicts = read_csv_as_dicts(filename, types)
    for dict in dicts:
        myData.append(dict)
    return myData

def read_csv_as_instance(filename, cls):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records



    