file = "mbox-short.txt"

fh = open(file,'r')
dic = dict()
for line in fh:
    if not line.startswith('From'): continue
    line_list = line.split()
    if len(line_list) < 3: continue ## coisa do formato do arquivo
    ## we want line_list[1] -> email of sender
    email = line_list[1]
    dic[email] = dic.get(email, 0) + 1

number = None
email  = None
for cemail,cnumber in dic.items():
    if number is None or cnumber > number:
        number = cnumber
        email = cemail

print(email,number)        






