askuser = int(input('enter how many user are there: '))


user = []

for i in range(askuser):
    names = input('enter the users names: ')
    user.append(names)
    
computer = []


for i in range(askuser):
    comp = input('enter the comp names: ')
    computer.append(comp)
    
    
for i in range(0,len(user)):
    print(f'computer used by {user[i]} is {computer[i]}')
# =============================================================================
# Alternate method by .format 
# =============================================================================
askuser = int(input('enter how many user are there: '))


user = []

for i in range(askuser):
    names = input('enter the users names: ')
    user.append(names)
    
computer = []

for i in range(askuser):
    comp = input('enter the comp names: ')
    computer.append(comp)
    
for i in range(0,len(user)):
    template = 'computer used by {} is {} '.format(user[i], computer[i])
    
    print(template)
