# pcost.py
if __name__ == '__main__':

    def totalCost(filename):
        total_cost = 0.0
        with open(filename, 'r') as f:
            for line in f:
                try:
                    fields = line.split()
                    nshares = int(fields[1])
                    price = float(fields[2])
                    total_cost = total_cost + nshares * price
                except ValueError as e:
                    print("Couldn't parse line")
                    print("Reason: " , e)

        return total_cost

    print(totalCost('../../Data/portfolio3.dat'))
