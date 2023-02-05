
# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

import random

numOfGroups = random.randint(3, 6) # количество групп
columns = random.randint(20, 30) # количество учеников
students = [0] * numOfGroups
count = 0
scores = 0 # рейтинг
numGroups = 1
GPA = 0 # средний балл
bestGroup = 0

for i in range(len(students)):
     columns =  random.randint(20, 30)
     students[i] = list(0 for _ in range(columns))
     for j in range(columns):
         students[i][j] = random.randint(2, 5) # оценки
         count += students[i][j]
     scores = count / columns

     if GPA < scores:
         GPA = scores
         bestGroup = numGroups
     print (f'Средний балл группы {numGroups} - {scores}')
     count = 0
     numGroups += 1

print('\nТаблица оценок по группам:')
for row in students:
     print(row)

print(f'\nГруппа с лучшим средним баллом - №{bestGroup}')

# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы

import random

rows = columns = 5 # размер матрицы
sumDiagonal = 0
sumEl = 0
numbers = [0] * rows 
line = 1

for i in range(len(numbers)):
     numbers[i] = list(0 for _ in range(columns))

for i in range(rows):
     for j in range(columns):
         current_number = random.randint(0, 50)
         numbers[i][j] = random.randint(0, 50)
         if i == j:
             sumDiagonal += numbers[i][j]

print("\nKвадратная матрица, заполненная случайными числами:")
for row in numbers:
     print(row)

print(f'\nСуммa главной диагонали - {sumDiagonal}')  

for i in range(rows):
     for j in range(columns):
         sumEl += numbers[i][j]
     if sumEl > sumDiagonal:
         print(f'Сумма элементов {line} строки {sumEl}, превосходит сумму главной диагонали матрицы.')
     sumEl = 0
     line += 1


     # Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. 
     # Каждому месяцу соответствует своя строка.
     # Определите самый жаркий и самый холодный 7-дневный промежуток каждого месяца. Выведите их даты.


     import random

def monthName(month):
     if month == 1:
         month = 'Май'
     elif month == 2:
         month = 'Июнь'  
     elif month == 3:
         month = 'Июль' 
     elif month == 4:
         month = 'Август'
     elif month == 5:
         month = 'Сентябрь'
     return month

months = 5
days = 31
numbers = [0] * months
june = 2 
septemder = 5
count = 1
step = []

warm = 0
cold = 999
monthWarm = 0
monthCold = 0
warmIndex = 0
coldIndex = 0

for i in range(len(numbers)):
     if count == 2 or count == 5:
         days =  30
     numbers[i] = list(0 for _ in range(days))
     for j in range(days):
         numbers[i][j] = random.randint(10, 30)
     for n in range(days-6):
         step = numbers[i][n:n + 7:1]
         _ = sum(step)
         if warm < _:
             warm = _
             monthWarm = count
             warmIndex = numbers[i][n]
             warmIndex = numbers[i].index(warmIndex)
         if cold > _:
             cold = _
             monthCold = count
             coldIndex = numbers[i][n]
             coldIndex = numbers[i].index(coldIndex)
     count += 1
     days =  31

print()
for months in numbers:
     print(months)

print(f'\nСамый теплый месяц - это {monthName(monthWarm)} (с температурой от {warmIndex+1} до {warmIndex+7}), за неделю сумма градусов равна {warm}')
print(f'Самый холодный месяц - это {monthName(monthCold)} (с температурой от {coldIndex+1} до {coldIndex+7}), за неделю сумма градусов равна {cold}')
