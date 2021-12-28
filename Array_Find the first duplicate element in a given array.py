# Find the first duplicate element in a given array of integers.
# Bangla- akta khali array nibo r akta given array, given array te loop chalabo
# jodi given array r element khali array te na thake tahole add kore nibo then next elements check korbo.
# jodi kono oirokom same element na thake then -1 return korbo.
x = [1, 1, 2, 3, 3, 2, 2]
y = []
get = False
for i in x:
    if y.count(i) > 0:
        print(i)
        get = True
        break
    else:
        y.append(i)
if get == False:
    print('-1')
