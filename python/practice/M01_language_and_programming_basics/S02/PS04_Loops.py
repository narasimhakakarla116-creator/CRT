'''
#n=int(input("Enter a number: "))
#for i in range(1,n+1):
   #print(i ,end=" ")

#i=1
#while i<=n:
  # print(i ,end="  ")   
  # i+=1
#name="Naidu"
#for i in range(len(name)):
#   print(name[i] ,end=" ")


#n=input("enter a name:")
#i=0
#while i < len(n):
    #print(n[i])
    #i+=1

n=input("enter a name:")
i=len(n)-1
while i >=0:
    print(n[i])
    i-=1      

'''
n=input("enter a name:")
for i in range(1, n+1):
    if i==5:
        break
    print(i)