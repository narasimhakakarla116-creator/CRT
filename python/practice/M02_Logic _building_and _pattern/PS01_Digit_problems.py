''''
write a python code to count the digits of a number? 

n=int(input("enter a number:"))
count=0
while n>0:
    n=n//10
    count+=1
print("number of digits are:",count)    

'''
'''
sum of the digits of anumber?

n=int(input("enter  a number:"))
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
print("sum of digits is:",sum)




reverse of a number?


n=int(input("enter a number :"))
rev=0
while n>0:
    rem =n%10
    rev=rev*10+rem
    n=n//10
print("reverse of a number:",rev)    


count no of even and odd digits in a number?


n=int(input("enter a number:"))
even=0
odd=0
while n>0:
    rem=n%10
    if rem%2==0:
        even+=1
    else:
        odd+=1
    n=n//10
print("even digits are:",even)  
print("odd digits are:",odd)          

print largest digit of a number?

'''
n=int(input("enter a number:"))
maxd=0
while n>0:
    rem=n%10
    if rem>maxd:
        maxd=rem
    n=n//10
print("largest of number:",maxd)        
