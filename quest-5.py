src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
d = {}
for i in src:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
result = [idx for idx in src if d[idx] == 1]
print(result)
