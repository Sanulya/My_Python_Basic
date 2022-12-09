# task 1
n = int(input('Введіть кількість школярів: '))
k = int(input('Яка кількість яблук є в наявності? : '))
print(f'Кожному школяру дістанеться по {k // n} яблук, в корзинці залишиться {k % n} яблук')

# task 2

number_of_students_1 = int(input('Введіть кількість учнів в "А" класі: '))
number_of_students_2 = int(input('Введіть кількість учнів в "Б" класі: '))
number_of_students_3 = int(input('Введіть кількість учнів в "В" класі: '))
number_of_desks_1 = round(number_of_students_1 / 2)
number_of_desks_2 = round(number_of_students_2 / 2)
number_of_desks_3 = round(number_of_students_3 / 2)
print(f'Всього необхідно закупити {number_of_desks_1 + number_of_desks_2 + number_of_desks_3} парт')

# task 3

num = int(input('Введіть трьохзначне число: '))
digit_1 = str(num % 10)
digit_2 = str(num // 10 % 10)
digit_3 = str(num // 100)
num_2 = (digit_1 + digit_2 + digit_3)
print('Перевернуте число: ', int(num_2))
print(f'Перевірка: {int(num_2) * 2}')

# additionally

number = int(input('Введіть кількість секунд: '))
second = number % 60
hours = number // 3600
minutes = number // 60 % 60
print(hours, ':', minutes, ':', second)
