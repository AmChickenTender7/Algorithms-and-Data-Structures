def binarySearch(list, target):
    ''' Binary search will break down list into halves until point is reached '''
    ''' Binary search will only work if the list is sorted '''
    
    first = 0
    ''' First is 0 rather than 1 because we are going to base the function on subscripts rather than the english length of the list'''
    last = len(list)-1
    ''' Convert length of list to subscript value'''

    while first <= last:
        ''' Why '''
        
        midpoint = (first + last)//2
        ''' First step of binary search. // Divides and rounds down decimals so that the index value will be valid and not a decimal '''

        if list[midpoint] == target:
            ''' If it's the midpoint, return midpoint (Best case scenario) '''
            return midpoint
        
        elif list[midpoint] < target:
            ''' If the midpoint is less than the target (The target value is > the midpoint) bring the beggining of the range to the midpoint excluding the middle point '''
            first = midpoint + 1
        else:
            ''' If the midpoint is greater than the target (The target value is < the midpoint) then bring the end of the range to the midpoint excluding the middle point '''
            last = midpoint - 1
    
    return None

def verify(index):
    """ Test if it works and converts result to english """

    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binarySearch(numbers, 12)
verify(result)

result = binarySearch(numbers, 6)
verify(result)