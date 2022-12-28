# task_1
import random

my_List = [random.randint(1, 300) for i in range(30)]
for element in my_List:
    if element > 100:
        print(element, end=' ')
print()
print('my_List', my_List)

# task_2
my_results = []
for element in my_List:
    if element > 100:
        my_results.append(element)
print('my_results', my_results)

# task_3
n = int(input('Введіть число до 10: '))
my_List_1 = [random.randint(1, 100) for i in range(n)]
print(my_List_1)
if len(my_List_1) < 2:
    my_List_1.append(0)
else:
    my_List_1.append(my_List_1[-1] + my_List_1[-2])
print('my_List_1', my_List_1)
