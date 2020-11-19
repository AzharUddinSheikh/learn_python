# =============================================================================
# BISECT AND INSORT 

'''If you want to insert a new number in a sorted list so that it ll be sorted
after inserting the number '''
# =============================================================================

import bisect 

a = [1,4,5,8,9,55,66,89,90,100]

number = 40

# print(bisect.bisect(a, number))
#output is 5 is shows you an index number not inserted yet

bisect.insort(a, number)
# print(a)
# insort method add the number in a index so that the list still sorted 


'''list is not sorted   '''

b = [1,6,70,7,13,10]

number  = 11

print(bisect.bisect(b, number))
#its show you the index number which is 2 (hence 6<11<70)

bisect.insort(b,number)
print(b)