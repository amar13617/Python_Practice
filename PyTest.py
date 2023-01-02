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
#print(Second_num)

#Write a program in Python to remove duplicate items from a list.
num = [2,3,4,5,2,6,3,2]
list1 = []
for i in num:
    if i not in list1:
        list1.append(i)

#print(list1)

#Write a program to check whether a given key exists in a dictionary or not.
dict = {'0':1, '1':2, '2':3, '4':5}
def check_key(dict1):
    for i in dict1:
        if i in dict:
            return True
        else:
            return False
#print(check_key('7'))

#Python program to remove a set of keys.
num = {0:"Value 1", 1:"Value 2", 2:"Value 3"}
keys = [0,1]
for k in keys:
    num.pop(k)
#print(num)

#Write a program to sum all the values of a dictionary.
dict1 = {'key 1': 200, 'key 2': 300}
sm = 0
for i in dict1:
    sm = sm + dict1[i]
#print(sm)

#Write a program to get the maximum and minimum value of dictionary.
dict1 = {'key 1': 200, 'key 2': 300}
max = 0
for i in dict1.values():
    if i > max:
        max = i
#print(max)

#Define a function in python that accepts 3 values and returns the maximum of three numbers.
def maximum(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
#print(maximum(4,2,6))

#Define a function which counts vowels and consonant in a word.
def count(word):
    const = 0
    vowel = 0
    for i in range(len(word)):
        if word[i] in ["a", "e", "i","o","u"]:
            vowel = vowel + 1
        else:
            const = const + 1
#print(count("google"))

#Define a function that returns Factorial of a number.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
#print(factorial(5))

#Define a function that accepts lowercase words and returns uppercase words.
def response(text):
    z = text.upper()
    return z
#print(response("Amar"))

#Write a program to reverse a string in python.
str = "amit"
str_reverse = []
for i in reversed(str):
    str_reverse.append(i)
text = "".join(str_reverse)
#print(text)

#Write a program to remove duplicates in a string.
str = "pythonlobby"
str_remove = []
for i in str:
    if i in str_remove:
        continue
    else:
        str_remove.append(i)

#print("".join(str_remove))




