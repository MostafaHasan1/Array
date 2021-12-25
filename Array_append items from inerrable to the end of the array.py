# if we are using list as an array, the following methods can used to add elements to it:
#- By using append() function: It adds elements to the end of the array.
#- By using insert() function: It inserts the elements at the given index.
#- By using extedn() function: It elongates the list by appending elements from both the lists.
x = [1, 3, 5, 7, 9]
y = [1, 3, 5, 7, 9]
x.extend(y)
print(x)
# print(x.extend(x),x)
