cost=0
for i in range(3):
    quantity=int(input("enter a quantity"))
    price=int(input("enter a price"))
    total=quantity*price
    cost+=total
    print("total cost is ")
if cost>100 and cost <200:
    discount=cost*0.05
    total=cost-discount
    print("total amount is","total")n
elif cost>200:
    discount=cost*0.1
    total=cost-discount
    print("total amount is ","total")
    