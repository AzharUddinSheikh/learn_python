'''When an error occurs, or exception as we call it, Python will normally stop
and generate an error message
Without the try block, the program will crash and raise an error

to avoid this we use try and except it code inside try have an error except
ll run without crashing the program and further proceed some example ll clear
the concept.'''

try:
    open('file.txt')
    
except:
    print('file does not exist')
print("is program alive yessss")

try:
    open('file.txt')

except Exception as e:
    print(e)
    print("file doesnot exist")
    

'''here print(e) print exception of an error to check what is it 
just run the program with only 2 line you ll see '''


try:
    open('file.txt')
    
except:
    pass

print("program is alive")


#Multiple Exception 
'''
if you enter alphabe try ll crash and it ll run value error exception
if you enter numeric value file not found error ll crash try and 
except ll run '''

try:
    a=2
    b=3
    int(input("enter the numerical value"))
    open('file.txt')

except ValueError:
        print("invalid value")
        
except FileNotFoundError:
    print("file doesnot exist")

finally:    
    print(a+b)
    
'''what is the use of finally for example 
 provided value error and file not found exception if user hit such code
like EOF or synax  error so try and except ll blow off and program crash again
and ll not execute further so we introduced finally so even if try and except 
crash then alos finally code ll run '''

# else 
'''else ll run when except ll not execute means try run without error '''

try:
    a = int(input('enter the value:>> '))
    b = int(input('enter the value:>> '))
except:
    print('not a valid value')
else:
    print(a+b)
finally:
    print('it ll print in very case')