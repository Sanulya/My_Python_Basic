# task_1
import random

Li = [random.randint(1, 300) for i in range(30)]
for element in Li:
    if element > 100:
        print(element, end=' ')
print()
print(Li)
