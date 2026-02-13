def even_odd(n: int) -> str:
   if n%2!=0:
      return "weired"
   elif 2<=n<=5:
      return "Not weired"
   elif 6<=n<=20:
      return "weired"
   else:
      return "Not weired"


if __name__ == '__main__':
    n = int(input())
    print(even_odd(n))
