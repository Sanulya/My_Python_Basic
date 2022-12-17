# task 1
operand_1 = int(input('Введіть операнд 1: '))
operand_2 = int(input('Введіть операнд 2: '))
operation = input('Введіть операцію, яку треба провести "+", "-", "/", "*", "**" : ')
if operation == '+':
    print(f'{operand_1} {operation} {operand_2} = {operand_1 + operand_2}')
elif operation == '-':
    print(f'{operand_1} {operation} {operand_2} = {operand_1 - operand_2}')
elif operation == '/':
    print(f'{operand_1} {operation} {operand_2} = {operand_1 / operand_2}')
elif operation == '*':
    print(f'{operand_1} {operation} {operand_2} = {operand_1 * operand_2}')
elif operation == '**':
    print(f'{operand_1} {operation} {operand_2} = {operand_1 ** operand_2}')
else:
    print('Введіть коректно операцію над числами')

# task 2
N = int(input('Введіть число: '))
for i in range(1, N):
    number_squared = i ** 2
    if number_squared > N:
        break
    print(number_squared, end=' ')

# task 3
number = int(input('\nВведіть число: '))
count_n = 0
for i in range(1, number + 1):
    if number % i == 0:
        count_n += 1
if count_n == 2:
    print(f'Число {number} є простим числом')
else:
    print(f'Число {number} не є простим числом')
