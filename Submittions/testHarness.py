import stock, reader, tableformat

#test with TextTableFormatter()
""" 
portfolio = reader.read_csv_as_instance('Data/portfolio.csv', stock.Stock)
formatter = tableformat.TextTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter) 

"""
#test with CSVTableFormatter()

portfolio = reader.read_csv_as_instance('Data/portfolio.csv', stock.Stock)
formatter = tableformat.create_formatter('HTML')
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter) 

