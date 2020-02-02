import math
A = []
for k in range(4):
    A.append([])
    for n in range(4):
        gn = (abs(math.cos((n + 1) / 2.7))) + (9.1 * math.sin(((1.2) * n + 1) + 1))
        fk = (12.4 * math.sin(abs((k + 1) / 2.1))) - (8.3 * math.cos(1.2 * (k + 1)))
        A[k].append(round(((n + 1) * fk) + (math.sin(k) * gn)))
        print(A[k][n],end="\t")
    print()
maxA = A[0][0]
minA = A[0][0]
for i in range(len(A)):
    for j in range(len(A[i])):
        if maxA <= A[i][j]:
            maxA = A[i][j]
            maxAi = i
            maxAj = j
        if minA >= A[i][j]:
            minA = A[i][j]
            minAi = i
            minAj = j
print(maxA,'Индексы максимального: ',maxAi,' ',maxAj)
print(minA,'Индексы максимального: ',minAi,' ',minAj)


