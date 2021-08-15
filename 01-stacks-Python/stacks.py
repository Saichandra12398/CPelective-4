"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        ele=Element(new_element)
        current=self.head
        ele.next=current
        self.head=ele
        

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        if self.head==None:
            return None
        if self.head.next==None:
            ele=self.head
            self.head=None
            return ele.value
        else:
            current=self.head
            self.head=current.next
            current.next=None
            return current.value

        pass

class stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)
        pass

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()
        pass


# e1 = Element(1)
# e2 = Element(2)
# e3 = Element(3)
# e4 = Element(4)
# st = stack(e1)
# st.push(e2)
# st.push(e3)
# print(st.ll.head.value)
# print(st.pop())
# print(st.pop())
# print(st.pop())
    
st=stack(Element(1))
print(st.pop())
print(st.pop())
