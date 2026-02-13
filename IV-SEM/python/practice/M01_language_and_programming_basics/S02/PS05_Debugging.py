'''''
bug=error
debugging --> finding and fixing of errors
typess of errors:
1.syntax error
2.logical error
3.runtime error  

syntax error: misssing of the colon,misssing of indentation  
runtime error: divison by zero  
logical error: missing of logics     

debugging techniques:
1.print()
2.try-except
3.using python debugger(pdb)
 pdb-->python debugger

 purpose:
 1.pause the exection code  2.inspect the variable values 
 3.to run the code line by line  

 pdb command:
1.n --> to execute the output in a nextline
2.p variable --> to get the value of a variable 
3.l --> list near by code 
4.c--> continue the execution 
5.s-->to start afunction 
6.r-->return from the functiion 
7.h-->help
8.q-->quit the execution



'''''
'''''
try:
    a=int(input("enter a number:"))
    print(10/a)
except ZeroDivisionError:
    print("you cannot divide by zero")
except ValueError:
    print("invalid input  ")    
'''
import pdb
def  add (a,b):
    pdb.set_trace()
    return a+b  
a=int(input("enter a number:"))
b=int(input("enter b number:"))
print(add(a,b))