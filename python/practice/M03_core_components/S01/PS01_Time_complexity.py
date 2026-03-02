'''
time complexity:
defination : time complextiy can be measured based upon the input
ex:
n=10
print(n)
  o(1)->constant time complexity
  o(n)->single loop
  o(n^2)->nested loop or two loops
  o(log n)->binary search  
  o(n log n)-> linearithmetic time complexity



  print(time complexity)  #o(1)  
  arr=[1,2,3,,3]
  for i in range():
  


arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")


'''
n=input("enter a string:")
t=input("enter a string:")
if sorted(n)==sorted(t):
    print("anagram")
else:
    print("not anagram")    
