'''
squares of a number

li =[1,2,3,4,5]
square=[x**2 for x in li]
print(square)

li=[1,2,3,4,5,6]
square=[x**2 for x in li if x%2!= 0]
print(square)


concatenation of a String


li=['a','b','c']
for x in li:
    print(x,end="")
    
li=['a','b','c']
res=""
for x in li:
    res=res+li[x]
    print(res)
print("".join(li))    


diamond pattern

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)


pyramid pattern using numbers  
'''
n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")   
    print()         

