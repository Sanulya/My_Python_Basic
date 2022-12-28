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
