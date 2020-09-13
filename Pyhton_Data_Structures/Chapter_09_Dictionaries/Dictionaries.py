'''
 - in a dictionary, you give each item a key
 - inside of a dict everything has to have a label
 - general name for all programming languages is 
 associative array(perl/php);
 properties/map/hashmap (java)
 Property bag (C#/.NET)
 - are Pythons most powerful data collection
 - allows us to do fast database-like operations 


purse = {'1':'Janeiro','2':'Fevereiro','3':'Março','4':'Abril','5':'Maio','6':'Junho','7':'Julho','8':'Agosto','9':'Setembro','10':'Outubro','11':'Novembro','12':'Dezembro'}
purse['12'] = 'money'
purse['candy'] = 3
purse['tissues'] = 75

number = str(6)
val = purse[number]
print(type(val))
'''
ls = ['lucca', 'mariana','lais','lucca','mariana','lais','lais','silayne','lucca','lucca','mariana']
c  = dict()

for name in ls:
    if name not in c:
        c[name] = 1
    else:
        c[name] = c[name] + 1
        
print(c)       

'''
name = 'words.txt'
h = open(name, 'r')

dic =  dict()
for line in h:
    wordsl = line.split()
    for word in wordsl:
        dic[word] = dic.get(word,0) + 1 ## create histogram, .get method looks into dictionary and sees if it has
                                        ## the key word if not return zero and if 1 returns the corresponding value
bigcount = None
bigword = None
for word,count in dic.items(): # dic.items returns a list of tuples,  corresponding to the key, value pair of the dictionary
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)                
'''