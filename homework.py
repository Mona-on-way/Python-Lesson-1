#Задачи на циклы и оператор условия

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована
'''
print('Задача 1')
i = 1
while i < 6:
    print(i, '0000000000000000000')
    i = i + 1
    if i == 6: break

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
print('Задача 2')
count = 0
num = int(input('Введите 10 цифр'))
while num > 0:
    if num%10 == 5:
        count+=1
    num = num//10
print(count)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
print('Задача 3')
sum = 0
for i in range(1,101):
    sum+=i
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
print('Задача 4')
prod = 1
for i in range(1,11):
    prod*=i
print(prod)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
print('Задача 5')
integer_number = 2129
while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
print('Задача 6')
sum = 0
num = 468237
while num>0:
    sum += num%10
    num//=10
print(sum)

'''
Задача 7
Найти произведение цифр числа.
'''
print('Задача 7')
prod = 1
num = 5413
while num>0:
    prod *= num%10
    num//=10
print(prod)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
print('Задача 8')
integer_number = 213586
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
print('Задача 9')
num = 213586
max_num = 0
while num>0:
    if num%10 > max_num:
        max_num = num%10
    num//=10
print(max_num)

'''
Задача 10
Найти количество цифр 5 в числе
'''
print('Задача 10')
count = 0
num = 1548656
while num>0:
    if num%10 == 5:
        count = count+1
    num = num//10
print(count)