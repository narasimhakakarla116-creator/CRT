''''
import numpy as np
arr=np.array([10,20,30])
print(arr)
print(np.max(arr))
print(np.min(arr))
print(np.sum(arr))
print(np.mean(arr))
print("Even numbers listis :",np.arange(2,10,2))
print("odd numbers list is:",np.arange(1,10,2))


n=int(input("enter a size : "))6
ele=list(map(int,input("enter ele :").split()))
print("array ele are:",np.array(ele))


n=int(input("enter a ele:"))
m=int(input("enter a ele:"))
print("sum is:",n+m)


nums=list(map((int,input("enter  a nums:").split())))
if len(set(nums))>=3:
    print(sorted(set(nums))[-3])
else:
    print(max(nums))    

'''
n=list(map(int,input("enter a nums:").split()))
inc =True
dec=False
for i in range(1,len(n)):
    if n[i]>n[i-1]:
        inc=False
    if n[i]<n[i-1]:
        dec=False
if inc or dec:
    print("monotonic")
else:
    print("not monotonic")    
        


