#Write a Python program to reverse the order of the items in the array
#main list = [1, 3, 5, 3, 7, 1, 9, 3]
#output: [3, 9, 1, 7, 3, 5, 3, 1]
list_1 = [1, 3, 5, 3, 7, 1, 9, 3]
reverse_list=[]
for i in range(7, -1, -1):
    x=list_1[i]
    reverse_list.append(x)

print(reverse_list)


