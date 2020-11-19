list1 = ['chalk','duster','board','pen']

'''

output should be like 
chalk and duster and board and pen 

'''

for i in list1:
    if i != 'pen':
        print(i + ' and ', end='')
        
    else:
        print(i)

# =============================================================================
# Alternate method
# introduced .join 

# =============================================================================

print(" and ".join(list1))