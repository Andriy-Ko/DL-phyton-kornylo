n=26
fibo=[0,1]
for x in range(2,n):
    fibo.append(fibo[x-1]+fibo[x-2])
m=int(input('Введіть ціле число:  '))
print('Число належить до ФІбочисел, оцінка 5') if m in fibo else print('Число не належить до фібочисел, оцінка 1')
      
#print(*fibo)
#print(len(fibo))
