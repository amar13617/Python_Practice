#Write a program to get the maximum number from a list.
num = [23,55,7,8,9]
max1 = num[0]
for index in num:
    if index > max1:
        max1 = index
#print(max1)
#Write a program to get the second maximum number from a list.
num = [23,55,7,8,9]
Largest_num = num[0]
Second_num = num[0]
for index in num:
    if index > Largest_num:
        Largest_num = index
        for index in num:
            if index > Second_num and index != Largest_num:
                Second_num  = index
print(Second_num)

