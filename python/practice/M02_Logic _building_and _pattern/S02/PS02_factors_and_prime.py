'''
reverse of a integer?


n=int(input("enter a number:"))
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("reverse of a number is :",rev)


n=int(input())
if n>=0:
    print(str(n[::-1]))       
else:
    n=-1*n  
    print(str(n)[::-1])    

    

check wheather a number is prime or not?
'''

n=int(input("enter a number:"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not a prime number")
            break
        else:
            print("prime number")
        