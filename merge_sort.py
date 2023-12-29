def merge_sort(list):
    """ 
    Sorts a list in ascending order
    Returns a new sorted list
    
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in the previous step
    
    Take O(k * log n)
    """
    if len(list) <= 1:
        return list
    
    """ Divide """
    left_half, right_half = split(list)
    
    """ Conquer """
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    """ Combine """
    return merge(left, right)

def split(list):
    """ 
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    
    Takes overall O(k * log n) time
    """
    
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    
    return left, right

def merge(left, right):
    """ 
    Merges two lists and sorts the process
    Returns a new merged list
    """
    
    l = []
    i = 0
    j = 0
    
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
            
    while i < len(left):
        l.append(left[i])
        i += 1
        
    while j < len(right):
        l.append(right[j])
        j += 1

    return l
        
alist = [54,26,93,2,5,3,99,57]
l = merge_sort(alist)
print(l)

def verify_sorted(list):
    n = len(list)
    
    if n == 0 or n == 1:
        return True
    
    """ 
    Returns the conidtion of if the first and second values are sorted for the entire list
    and also the condition of the first and second values of a list that does not contain the
    first value
    """
    return list[0] < list[1] and verify_sorted(list[1:])


blist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
l = merge_sort(blist)
print(verify_sorted(blist))
print(verify_sorted(l))