'''fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 1    : continue
    if wds[0] != 'From': continue
    print(wds[1])
         
    count += 1

print("There were", count, "lines in the file with From as the first word")
'''
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    #line = line.rstrip()
    
    if line.startswith('From'): 
        nline = line.split()
        if len(nline) < 3: continue
        print(nline[1])
         
        count += 1

print("There were", count, "lines in the file with From as the first word")
