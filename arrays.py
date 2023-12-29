""" Values not stored in array. Pointers are saved """
""" Index error is caused by accessing index not in array.
    The array will look at address and not be able to read it """
new_list = [1,2,3]
result = new_list[0]

if 1 in new_list: print(True)

""" Linear Search """
""" Binary search could be used but is suboptimal because the list must be sorted """
for n in new_list:
    if n == 1:
        print(True)
        
        break
    
numbers = []
numbers.append(2)
numbers.append(200)
numbers.extend([4,5,6])
print(numbers)