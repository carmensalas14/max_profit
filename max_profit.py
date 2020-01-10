"""
list = [11,8,4,12,7,7]
stock_prices(list) == 8

stock_prices([8,31,4,8,30,5,6]) == 26

p-

e-
get_max_profit([120,100,90,21,12]) == -9

d-
arrays 
return integer 

a- 
loop over the array 
    for each element through each index to find largest difference 
-declare variable max_profit = list[1] - list[0]
-loop over list - list[i]
-for each element loop from the next index to the end of the list list[j]
if list [j] - list[i] > max profit 



"""
def get_max_profit(stock):
    
    max_difference = stock[1] - stock[0]
    for i in range(len(stock)):
        for j in range(i + 1, len(stock)):
             if stock[j] - stock[i] > max_difference:
                max_difference = stock[j] - stock[i]

    return max_difference
            
print(get_max_profit([120,100,90,21,12]))
print(get_max_profit([8,31,4,8,30,5,6]))