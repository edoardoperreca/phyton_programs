'''
def somma(n):
    if n==1:
        return 1
    else:
        return (n)+somma(n-1)
x=int(input('inserisci un numero naturale: '))
print('la somma dei primi ',x,'naturali è: ',somma(x))
###
def f(n):
    if n==0 or n==1:
        return 1
    else:
        return f(n-1)+f(n-2)
x=int(input('inserisci: '))
print(f(x))
'''
def somma(n):
    if n==2:
        return 2
    else:
        return (n)+somma(n-2)
x=int(input('inserisci un numero naturale pari: '))
print('la somma dei primi ',x,'pari è: ',somma(x))
