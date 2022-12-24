# task_1
my_string = '0123456789'
for i in range(len(my_string)):
    for n in range(len(my_string)):
        print(int(my_string[i] + my_string[n]))

# task_2
height = int(input('Введіть висоту фігури: '))
for h in range(height + 1):
    print(' ' * (height - h) + '*' * h + '*' * (h - 1))
for h in range(1, height + 1):
    if h == 1:
        print(' ' * (height - h) + '*')
    elif h == height:
        print('*' * (2 * height - 1))
    else:
        print(' ' * (height - h) + '*' + ' ' * (2 * h - 3) + '*')
for h in range(height + 1):
    print(' ' * (height - h) + '*' * h + '*' * (h - 1))
for h in range(1, height + 1):
    if h == height:
        print(' ' * (h - 1) + '*')
    else:
        print(' ' * (h - 1) + '*' + ' ' * (2 * height - 2 * h - 1) + '*')
for h in range(height + 1):
    print(' ' * (height - h) + '*' * h + '*' * (h - 1))
for h in range(1, height + 1):
    if h == height:
        print(' ' * (h - 1) + '*')
    else:
        print(' ' * (h - 1) + '*' + ' ' * (height - 1 - h) + '*' + ' ' * (height - h - 1) + '*')
