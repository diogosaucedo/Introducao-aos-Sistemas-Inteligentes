"""
1) Dada duas listas, uma com a idade e outra com o peso das pessoas, faça uma função que retorne quantas pessoas com
mais de 40 anos possuem peso superior a média dos pesos dessas pessoas.
"""

import random

# age between 18 and 100 for 100 people
age = [random.randint(18, 100) for i in range(100)]

# weight between 50 and 120 for 100 people. (integer values only)
weight = [random.randint(50, 120) for i in range(100)]

weight_average = sum(weight) / len(weight)

peoples = 0  # number of people who meet the condition
# find people who meet the condition
for i in range(100):
    if age[i] >= 40 and weight[i] > weight_average:
        peoples += 1
print(str(peoples) + " peoples are above weight average (" + str(weight_average) + " Kg)")
