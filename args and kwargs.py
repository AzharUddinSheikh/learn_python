'''*args and **kwargs or * and ** is imp not their names
type 0f *args tuple
type of **kwards dict'''


def function(name,age,rollno):
    print("the name is",name,"and age is",age,"whose roll no is",rollno)


# function('azhar',26,'12')
    
    

def function1(*args):
    print("the name is",args[0],"and age is",args[1],"whose roll no is",args[2])


# function1('sheikh',23,11)

list1 = ['azhar',23,11]

# function(list1) # Error agrs[0] will takes whole list1 as its valeue

# function(*list1)

'''*arg takes no of variable
value of sheikh ,23, and 11 stores in *agrs and 
we didnt provide no of parameter in function1()
'''

# function1('sheikh',23) # error you provide args[2] and not provided it
  

#if someone provided only 2 parameter 

def function2(*args):
    if len(args) == 3:
        print("the name is",args[0],"and age is",args[1],"whose roll no is",args[2])
    else:
        print("the name is",args[0],"and age is",args[1])
        

# function2('ajju',27)

# **kwargs
'''.items() is dict function its provide pair key values'''

def printmark(**kwargs):
    for key,i in kwargs.items():
        print(key,i)
    
    
marklist = {'azhar':33,'uddin':23,'sheikh':44,'ajju':45,'valar':80,'honey':44}    
# printmark(**marklist)

'''benefit lets update marklist by .update or insert method or just 
write directly and feed one more key and value (honey and 44 respectively 
so by adding honey and 44 we didnt cahnge any argument up there

*arg doing the same but there we have only one value'''


def master(normal,*arg,**kwargs):
    print(normal)
    for i in arg:
        print(i)
    for key,value in kwargs.items():
        print(key,value)
        

list1 = ['azhar',23,44]
marklist = {'azhar':33,'uddin':23,'sheikh':44,'ajju':45,'valar':80,'honey':44}

# master("normal", *list1, **marklist)
