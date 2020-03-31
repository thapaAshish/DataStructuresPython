""" We initialize a Node class that extends object"""
class Node(object):
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self,new_next):
        self.next_node = new_next
    
    

""" 
Features of linked list

insert -->insert item to linked list
size --> size of the linked list. 
search --> whether the value we need is present in the list or not
Delete --> if elements are found then delete it else raise error. which means learn to define errors.

 """

 
class LinkedList(object):
    
    def __init__(self,head=None):
        self.siz = 0
        self.head=head
        

    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head=new_node
        self.siz += 1
        

    def size(self):
        return self.siz

    def search(self,data,ret=False):
        bufferHead =self.head
        #start from the last node and check recurively till the node ends . when node ends the value is 
        while(self.head.get_next() != None):
            if self.head.get_data() == data:
                self.head = bufferHead
                return True
            print(self.head)
            self.head = self.head.get_next()
        self.head = bufferHead 
        return False


    """ 
    first variable stores what is linked to next object 
    second variable stores what is linked to first variable
    while second variables point to None
    keep on looking for data. if data is found then make first variable refer whatever second variable next link is

    """
    def delete(self,data):
        bufferHead = self.head
        prevData = None
        while(self.head != None):
            
            if self.head.get_data()==data:
                try:
                    prevData.set_next(self.head.get_next())
                except AttributeError:
                    self.head = self.head.get_next() 
                    self.siz -= 1
                    return True
                self.head = bufferHead
                self.siz -= 1
                return True
            else:
                prevData = self.head
                self.head = self.head.get_next()
                
        self.head = bufferHead
        return False

    def __str__(self): 
        klist =[]
        while(self.head != None):
            klist.append(self.head.get_data())
            self.head = self.head.get_next()

        return str(klist)






ll = LinkedList()


ll.insert(1)
ll.insert(23)
ll.insert(44)
ll.insert(2233)
ll.insert(28)
print(ll.search(23))
ll.delete(28)
print(ll.size())
print(ll)




            
        
            