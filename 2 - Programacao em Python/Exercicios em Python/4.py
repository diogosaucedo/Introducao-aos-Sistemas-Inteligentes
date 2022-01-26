"""
4) Crie um programa que gere 100 valores aleatórios entre 1 e 10. Mostre qual número que menos apareceu e qual o que mais
apareceu, com suas respectivas frequências.
"""

import random
from collections import Counter

# generating values
random_values = [random.randint(1, 10) for i in range(100)]

# Counting and Ordering Recurrence
recurring_values = Counter(random_values).most_common()
# showing recurrence
print(recurring_values)
print("Most repeated: value = ", recurring_values[0][0], ", recurrence = ", recurring_values[0][1])
print("Less repeated: value = ", recurring_values[-1][0], ", recurrence = ", recurring_values[-1][1])
