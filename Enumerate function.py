# =============================================================================
# enumerate function 
# =============================================================================

a = ['azhar','ajju','kashif','rellick','monty','python']

i = 0 
for item in a:
    i += 1
    # print(i,item)

i = 0 
for item in a:
    i += 1
    if i%2 ==0:
        print(i,item)

'''lets do the same code with different method'''

for i, item in enumerate(a):
    i += 1
    print(i,item)    
    

for i, item in enumerate(a):
    if (i+1)%2 == 0:
        print(i+1,item)