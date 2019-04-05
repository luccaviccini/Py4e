'''n=5
while n>0:
    print(n)
    n = n-1
print('Blastoff')'''

'''while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!!!')'''

'''while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print("Done!!!")'''


#finding the niggest number
'''
largest_number = 0
A = [9, 41, 12, 3, 74, 15]
size = len(A)
for thing in range(0,size,1):
    if A[thing] > largest_number:
        largest_number = A[thing]
    else:
        continue
    
    #print(thing)
print(largest_number)
'''
#finding the biggest number
'''
largest = 0
print('Before', largest)
for num in [9, 41, 12, 3, 74, 15]:
    if num > largest:
        largest = num
    print(largest, num)
print("After", largest)'''


# counting the number of times a loop is executed
'''
counter = 0
print('Before', counter)
for num in [9, 41, 12, 3, 74, 15]:
    counter = counter + 1
    print(counter, num)
print("After", counter)
'''

# adding all the values in the list

'''
counter = 0
print('Before', counter)
for num in [9, 41, 12, 3, 74, 15]:
    counter = counter + num 
    print(counter, num)
print("After", counter)
'''

# finding the average of a list
'''
counter = 0
soma = 0
print('Before', counter, soma)
for value in [9, 41, 12, 3, 74, 15]:
    counter = counter + 1
    soma = soma + value
    print(counter, soma, value)
print('After', counter, soma, soma/counter)    
'''

# filter something (the 'if' acts as a filter)
'''
print('Before', counter, soma)
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('Large numer', value)
print('After')
'''

# search using a boolean variable and how many iterations it took

'''found = False
print('Before', found)
counter = 0
for value in [9, 41, 12, 3, 74, 15]:
    counter = counter + 1
    if value == 3:
        found = True
        print(found, value)
        print('number of iterations: ', counter)
        
print('After', found)

'''

# smallest value of a list with counter
'''
small = 1000
print('Before', small)
i=0
for num in [9, 41, 12, 3, 74, 15]:
    i = i + 1
    if num < small:
        small = num
    print(small, num)
print("After, the smallest number is: ", small)
print("Number of iterations: ", i)

'''
# using None Variable
        
small = None
print('Before', small)
i=0
for num in [9, 41, 12, 3, 74, 15]:
    i = i + 1
    if small is None: # its only going to run 1st time
        small = num
        
    elif num < small:
        small = num
        
    print(small, num)
print("After, the smallest number is: ", small)
print("Number of iterations: ", i)

## End of Introduction to Python














    
    




















        
