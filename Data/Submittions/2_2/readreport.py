import csv
import readrides
from collections import Counter

data = readrides.read_rides_as_dicts('ctabus.csv')

for s in data:
    totalRidersPerRoute2011 = Counter()
    date = s['date'].split("/")
    print(date)
    year = data[2]
    if year == "2001":
        totalRidersPerRoute2011[s['route']] += s['rides']

print(totalRidersPerRoute2011)