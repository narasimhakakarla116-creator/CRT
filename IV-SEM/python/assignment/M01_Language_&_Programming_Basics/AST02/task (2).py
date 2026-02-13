def even_odd(n: int) -> str:
   if n%2!=0:
       return "weired"
   else:
       if 2<=n<=5:
           return "not weired"
       elif 6<=n<=20:
           return "weired"
       else:
           return "not weired"
       


if __name__ == '__main__':
    n = int(input())
    print(even_odd(n))
