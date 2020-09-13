file = "mbox-short.txt"

fh = open(file,'r')
dic = dict()
for line in fh:
    if not line.startswith('From'): continue
    line_list = line.split(":")
    if len(line_list) < 3: continue
    temp = line_list[0]
    hour = temp[len(temp) -2:]
    dic[hour] = dic.get(hour, 0) + 1

'''x=  sorted([(k,v) for k,v in dic.items()])
print(x)

lst = list()
for k,v in dic.items():
    tup = (k,v)
    lst.append(tup)
lst = sorted(lst)
for k,v in lst:
    print(k,v)    
##### ORRRR ######
'''
for k,v in sorted([(k,v) for k,v in dic.items()]):  print(k,v)
   
    
    