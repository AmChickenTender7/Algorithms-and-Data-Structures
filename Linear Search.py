def linearSearch(list, target):
    '''Returns index postition of the target if found, else returns None'''
    '''In a true implimentation of linear search we look for index rather than value'''

    for i in range(0, len(list)):
        """ Iterate over the values of the list with i being the iteration rather than the value of the iteration """

        if list[i] == target:
            """ list[i] is subscript notation """
            """ this if statement checks the value of each value at the iteration and returns the index of the iteration for the target value """

            return i
    
    ''' Return None if the value is not found in the list '''
    return None

def verify(index):
    ''' This is mainly to convert the answer to english '''
    if index is not None:
        ''' If the index has a value '''
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linearSearch(numbers, 6)
verify(result)