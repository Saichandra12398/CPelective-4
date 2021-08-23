"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""



class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here
        if self.head:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_element
        else:
            self.head=new_element
            
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        count=1
        temp=self.head
        while temp.next:
            if count==position:
                return temp.value
            temp=temp.next
            count+=1
        if count==position:
            return temp.value
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        count=1
        temp=self.head
        while temp.next:
            if count==position-1:
                new_element.next=temp.next
                temp.next=new_element
            temp=temp.next
            count+=1
        

        pass
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        temp=self.head
        previous=None
        while(temp.value!=value and temp.next):
            previous=temp
            temp=temp.next
        if (temp.value==value):
            if(previous):
                previous.next=temp.next
            else:
                self.head=temp.next



e1 = Element(1)
e2 = Element(2)
e3 = Element(3)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
# print(ll.get_position(3))
# print(ll.get_position(2))
e4 = Element(4)
ll.insert(e4,3)
# ll.get_position(position)
# ll.insert(Element(5),4)
temp=ll.head
while temp.next:
    print(temp.value)
    temp=temp.next
print(temp.value) 