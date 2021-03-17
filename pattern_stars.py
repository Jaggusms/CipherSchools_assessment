
#n=int(input()) # dynaminc in nature
n=5
for i in range(1,n+1):
    print(str(("* "*i)).rjust(2*n))




""" 


print("Enter Your budget :",end=" ")
Budget=int(input())
product=[]
quantity=[]
price=[]
left=0
def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]
while(Budget > 0):
    print("1.Add an item \n2.Exit \nEnter your choice :",end=" ")
    choice=int(input())
    if choice==1:
        print("Enter product :",end=" ")
        p=input()
        print("Enter quantity :",end=" ")
        q=input()
        print("Enter Price :",end=" ")
        A=int(input())
        left=Budget-A
        if(Budget <A):
            print("Can't Buy the product ###(because budget left is {}))".format(Budget))
            continue
        else:
            product.append(p)
            quantity.append(q)
            price.append(A)
            print("Amoutn left : {}".format(left))
        Budget -= A
    else:
        if left in price:
            l=duplicates(price, left)
            for i in l:
                print("Amount left can buy you "+product[i])
        Budget=0
        

print("GROCERY LIST is: \nProduct name  Quantity   Price:")
for i in range(len(product)):
    print(f"{product[i] : <15}{quantity[i] : ^10}{price[i] : ^10}")
    
        
            
"""      
            

