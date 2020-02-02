import random

assessments = [random.randint(2,5) for i in range(20)]
print(assessments)
d = 0
c = 0
b = 0
a = 0
for i in range(len(assessments)):
    if assessments[i] == 2:
        d += 1
    if assessments[i] == 3:
        c += 1
    if assessments[i] == 4:
        b += 1
    if assessments[i] == 5:
        a += 1
print('Двоек:',d)
print('Троек:',c)
print('Четвёрок:',b)
print('Пятёрок:',a)
print('Успеваемость:',((d+c+b+a)/len(assessments))*100,'%')
print('Повышенные оценки:',((b+a)/len(assessments))*100,'%')
