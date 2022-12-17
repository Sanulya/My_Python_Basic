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
