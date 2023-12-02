def recursiveBinarySearch(list, target):
    ''' Does target exist or not'''
    
    ''' If it's empty '''
    if len(list) == 0:
        return False
    else:
        ''' If it's not empty find midpoint '''
        midpoint = (len(list))//2

    ''' If value at midpoint is the target your done. Return true '''
    if list[midpoint] == target:
        return True
    else:
        """ If target is greater than midpoint """
        if list[midpoint] < target:
            """ Restart function decleration with the range modified to be greater than the midpoint """
            return recursiveBinarySearch(list[midpoint+1:], target)
        else:
            """ Restart function decleration with the range modified to be less than the midpoint """
            return recursiveBinarySearch(list[:midpoint], target)

def verify(result):
    print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8]
result = recursiveBinarySearch(numbers, 12)
verify(result)

result = result = recursiveBinarySearch(numbers, 6)
verify(result)