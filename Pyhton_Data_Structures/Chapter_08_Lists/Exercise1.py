s = ['1','2','3','4','5','6','7','8','9']

def chop(s):
    del s[0] 
    del s[len(s)-1]

def middle(s):
    return s[1:len(s)-1]

ns = middle(s)
print(ns)

