# Representing Simple Strings
'''
print(ord('H')) # ordinal on ASCII table
print(ord('e'))
print(ord('\n'))
'''
# Python strings to Bytes
# to receive data
'''
while True:
    data = mysock.recv(512) # is in BYTES
    if (len(data) < 1):
        break
    mystring = data.decode() # UNICODE -> UTF-8 OU ASCII
    print(mystring)
'''
 # to send data
 '''
 import socket

 mysock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 mysock.connect(('data.pr4e.org', 80))
 cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
 mysock.send(cmd)
 '''
 # Creating Classes (it is a template)
'''
 class PartyAnimal:
     x=0
     def __init__(self):
         print('I am constructed')

     def party(self):
         self.x = self.x +1
         print('So far', self.x)
     def __del__(self):
         print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
an = 42

print('Type', type(an))
print('Dir', dir(an))
'''
# 2 different instances
'''
class PartyAnimal: #
    x=0
    name = ''
    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

s = PartyAnimal('Sally')
s.party()

j = PartyAnimal('Jim')
j.party()
s.party()
'''
#inheritance (one template getting things from another template)
class PartyAnimal:
    x=0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

class FootballFan(PartyAnimal):
    points = 0
    def touchdowns(self):
        self.points = self.points + 7
        self.party()
        print(self.nae, 'points', self.points)

s = PartyAnimal('Sally')
s.party()

j = FootballFan('Jim')
j.party()
j.touchdowns()
