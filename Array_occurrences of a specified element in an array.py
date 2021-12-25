x = []
y = int(input())
max_value = 0
max_occ = 0
for i in range(y):
    elements = int(input())
    x.append(elements)
for j in x:
    if max_occ < x.count(j):
        max_occ = x.count(j)
        max_value = j


print(max_value, 'occured', max_occ, 'times')
