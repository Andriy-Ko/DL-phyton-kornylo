def fact(n):
    if n==1 or n==0:
       return 1
    else: return n*fact(n-1)

print("програма обчислює фікторіали всіх чисел в діапазоні [A:B], з кроком С")
print()
a=int(input('введіть, будь ласка, ціле число А:  '))
b=int(input('введіть, будь ласка, ціле число B:  '))
c=int(input('введіть, будь ласка, ціле число C:  '))
print('  ****  ')

for i in range(a,b+1,c):
    print('число:',i,'  його факторіал: ',fact(i))
