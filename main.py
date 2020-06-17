x=int(input("Choose a value of x for f(x)=x! "))
if x<0:
  print("You can't take the factorial of a negative number!")
elif x==0:
  print(1)
else:
  y=input("Choose a factorial, 1 (front) or 2(back) ")
  if y==1:
    def Frontfactorial(x):
      z=1
      for i in range(1,x+1):
        z*=i
      return z
    print(Frontfactorial(x))
  else:
    def Backfactorial(x):
      for i in range(x-1,0,-1):
        x*=i
      return x
    print(Backfactorial(x))