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

# looping and counting
'''
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
'''

s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])

print(s[:4]) # ommits 0 but same thing
print(s[6:]) 
