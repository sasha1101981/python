# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

N = int(input('Введите количество монет '))
avers = 0
resvers = 0
for i in range(N):
    x = int(input('Орел(1) или решка(0)? '))
    if x == 1:
        avers += 1
    else:
        resvers += 1
if avers < resvers:
    print(f'Переверните {avers} монет с орла на решку, их меньше всего')
elif avers == resvers:
    print(f'Количество орлов и решек одинаково, по {avers} штук')
else:
    print((f'Переверните {resvers} монет с решки на орла, их меньше всего'))