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
    if number_squared > N - 1:
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

# additionally

mushroom_quantity = int(input('Введіть кількість грибів: '))
if mushroom_quantity == 1 or mushroom_quantity % 10 == 1 or mushroom_quantity % 100 == 1:
    print(f'Маша знайшла у лісі {mushroom_quantity} гриб')
# elif 1 < mushroom_quantity < 5 or 1 < mushroom_quantity % 10 < 5 or 1 < mushroom_quantity % 100 < 5:
#     print(f'Маша знайшла у лісі {mushroom_quantity} гриба')
elif 4 < mushroom_quantity < 20 or 4 < mushroom_quantity % 10 < 20 or 4 < mushroom_quantity % 100 < 20:
    print(f'Маша знайшла у лісі {mushroom_quantity} грибів')
elif  mushroom_quantity % 10 == 0 or mushroom_quantity % 100 == 0:
    print(f'Маша знайшла у лісі {mushroom_quantity} грибів')
else:
    print(f'Маша знайшла у лісі {mushroom_quantity} гриба')
