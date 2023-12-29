class Node:
    """ An object for storing a single node of a linked list """
    """ Models two attributes - data and the link to the next node in the list """
    data = None
    next_node = None
    
    """ Constructor for the variable type """
    def __init__(self, data):
        self.data = data
        
    def __repr__(self):
        return "<Node data: %s>" % self.data
    
""" 
    Start Repl environment
    Console Input: python -i linked_list.py
    
    Use Constructor
    N1 = Node(10)
    
    Call N1 using repr method
    N1
    <Node data: 10>
    
    Use Constructor
    N2 = Node(20)
    
    Use Constructor to make New Variable
    N1.next_node = N2
    
    Call N1.next_node
    N1.next_node
    <Node data: 20>
    
    Nodes are the Building Blocks for Lists
"""

class LinkedList:
    """ Singly linked list """
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def size(self):
        """ Returns the number of nodes in the list (Takes O(n) Time) """
        current = self.head
        count = 0
        
        """ while current != None: """
        while current:
            count += 1
            current = current.next_node
            
        return count
    
    """ 
        Initialize l as part a LinkedList()
        l = LinkedList()
        
        Initialize a node as N1
        N1 = Node(10)
        
        Initialize the head of the linked list
        l.head = N1
        
        Utilize the size method we created
        l.size()
        
        Output of the size method
        1
    """

    def add(self, data):
        """ Adds new node containing data at the head of the list (Takes 0(1) Time) """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    """ 
        Initialize list
        l = LinkedList()
        
        Utilize add method
        l.add(1)
        l.size()
        1
        
        Utilize add method
        l.add(2)
        l.add(3)
        l.size()
        3
        
    """
    def search(self, key):
        """ Search for first node that contains data that matches the key """
        """ Returns the node or "None" if not found """
        """ Takes O(n) time """
        
        """ First node constructor """
        current = self.head
        
        """ While current is not equal to None """
        while current:
            """ If the value at the iteration is the one being searched for return it """
            if current.data == key:
                return current
            else:
                """ Otherwise reestablish current as the next node and repeat the loop because node """
                """ has not been found and there is still more values in the Linked List """
                current = current.next_node
        return None
        
    def insert(self, data, index):
        """ Takes overall O(n) """
        
        """ If we want to insert the data at the front of the list the add method already does this """
        if index == 0:
            self.add(data)
        
        """ If the data is not at the front of the list """
        if index > 0:
            """ Create new, temporary node """
            new = Node(data)
            
            """ Loop values """
            position = index
            current = self.head
            
            while position > 1:
                current = new.next_node
                position -= 1
                
                prev_node = current
                next_node = current.next_node
                
                prev_node.next_node = new
                new.next_node = next_node
            
    def remove(self, key):
        """ Removes Node containin data that matches the key """
        """ Returns the node or None if key doesn't exist """
        """ Takes O(n) time """
        current = self.head
        previous = None
        found = False
        
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
                
        return current
    
    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            
            while position < index:
                current = current.next_node
                position += 1
            
            return current
    
    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return  '-> '.join(nodes)