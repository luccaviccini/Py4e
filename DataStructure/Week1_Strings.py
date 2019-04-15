'''str1 = 'Hello'
str2 = 'there'
bob = str1 + str2
print(bob)

## if one of the strings is a number, first convert into float or integer.
## samething from input function

str3 = '123'
str3 = int(str3)
midge = 1 + str3
print(midge)
'''
# looking inside strings -  index operator
'''
fruit = 'banana'
print(len(fruit)) # prints number of characters in string
letter = fruit[1]
print(letter)
x = 3
w = fruit[x-1]
print(w)
'''
# looping through strings (indeterminate loop)
'''
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# looping through determinate loop (if you dont need to know index)
fruit = 'banana'
for letter in fruit:
    print(letter)
'''

# looping and counting (searching for a determinate letter in a string)
'''
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
'''
# more thing with strings indexes
'''
s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])

print(s[:4]) # ommits 0 but same thing
print(s[6:])
'''
# string concatenation
'''
a = 'Hello'
b =  a +'There' #string concatenation does not add space

c = a + ' ' + 'There'
'''

# using 'in' as a Logical operator
'''
fruit = 'banana'

'n' in fruit
'nan' in fruit

if 'a' in fruit:
    print('There is an a')
'''

# string library

greet = 'Hello Bob'
zap = greet.lower() # will return the string in lowercase

# functions -> look online for methods of class strigs

newstr = greet.replace('Bob', 'Jane')
boolean = greet.startswith('Hello')

# looks for substring of a bigger strings

fruit = 'banana'
pos = fruit.find('na') # returns position of first letter of substring

# if the method find does not find the substring, then returns -1
