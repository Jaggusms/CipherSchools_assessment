#n=int(input())  #for dynamically
n=5
num=0
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+(num%26))+" ",end="")
        num +=1
    print()
