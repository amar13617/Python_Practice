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

#Python program to count the occurrence of each character in a word.
word ="google"
dict = {}
for i in word:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

#print(dict)

a = [1,2,3,4,5,6,7,8]
print(a[2::2])

#Reversing string
str = 'My Name is Jessa'
str1 = []
for ele in reversed(str):
    str1.append(ele)
#print("".join(str1))

#Remove items from a list while iterating
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list1 = []
for ele in number_list:
    if ele <= 50:
        list1.append(ele)
#print(list1)

#Display all duplicate items from a list
sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
unique = []
duplicate = []
for ele in sample_list:
    if ele not in unique:
        unique.append(ele)
    else:
        duplicate.append(ele)
#print(duplicate)

#Filter dictionary to contain keys present in the given list

# Calculate the multiplication and sum of two numbers.
def calculation(a,b):
    if a * b >= 1000:
        return a+b
    else:
        return a*b
#print(calculation(2,8))

name = 'natalie'
name1 = name[::-1]
#print(name1)

name2 = []
for i in reversed(name):
    name2.append(i)
#print("".join(name2))

message = 'Hola Amigos'
message1 = 'J' + message[1:]
#print(message1)

string = "Python is fun"
#print(string.partition('fun'))

string = "Python is fun, isn't it"
print(string.partition('is'))

sentences = 'Time to master data science', 'amar', 'at'
for i in sentences:
    print(i)

#print('a' > 'b')
#print('a' < 'b')
#print('abc'> 'b')
#print('abd'>'abc')

a = 7/2
#print(a)
b = 7%2
#print(b)
c = 7//2
#print(c)

#Write a program to check whether a given key exists in a dictionary or not.
dict = {'0':1, '1':2, '2':3}
def check(x):
    if x in dict:
        return "yes"
    else:
        return "No"
#print(check('7'))

#Write a program to iterate over dictionary items using for loop.

#Python program to remove a set of keys.
dict1 = {0:"Value 1", 1:"Value 2", 2:"Value 3"}

keys = [0,1]
for k in keys:
    dict1.pop(k)
#print(dict1)

#Python program to sort dictionary by values (Ascending/ Descending).
dict = {'c': 2, 'd':4 , 'a' : 3, 'b' : 1}
list1  = list(dict.items())
list1.sort(reverse= True)
print(list1)
