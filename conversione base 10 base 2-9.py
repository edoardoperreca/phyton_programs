n=int(input("inserisci numero intero: "))
b=int(input("inserisci base da 2 a 9: "))
m=n
s=""
if n==0:
    print(0)
else:
  while n>0:
    s=str(n%b)+s
    n=n//b

print("il numero",m,"in base b è",s)
