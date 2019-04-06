largest = None
small = None

while True:
    number = input("Type an integer: ")
    if number == "done":
        break
    try:
        bignumber = int(number)
        smallnumber = int(number)
    except:
        print('Invalid Input')     
    
    if largest is None:
        largest = bignumber
    elif small is None:
        small = smallnumber
    elif bignumber > largest:
        largest = bignumber
    elif smallnumber < small:
        small = smallnumber
        

            
print('Maximum is ', largest)
print('Minimum is ', small) 
         
        
        

