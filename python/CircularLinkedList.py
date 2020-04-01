""" This is implementation of circular linked list
Similar to linked list . Only difference is that last node is pointing to first node

constraints of this implementation
1.nothing to search for multiple occurences of same data

 """


# node can return data currenlty in storage, set next_node and return current node

class Node(object):
     
    def __init__(self,data=None,next_node=None):
         self.data = data
         self.next_node = next_node

    def get_data(self):
        return self.data
    
    def set_next_node(self,node_get):
        self.next_node = node_get

    def get_next(self):
        return self.next_node


class CircularLinkedList(object):
    def __init__(self,head=None):
        self.size = 0
        self.head = head

    #To insert items into node. First 
    def insert(self,data):
        
        if self.head==None:  #if this is initialized for first time
            self.head = Node(data)
            self.head.set_next_node(self.head)
            self.size+=1
        else:
            #first disconnect whatever is present in the node
            bufferFirstNode = self.head.get_next()  #store the first link
            newNode = Node(data) #define new node 
            self.head.set_next_node(newNode) #override previous node with new node
            self.head = self.head.get_next() #get to node that we currently inserted
            self.head.set_next_node(bufferFirstNode) #place first node as its last node
            self.size += 1
   

    def search(self,data):
        bufferHead = self.head
        self.head = self.head.get_next()
        while(self.head != bufferHead):  #loop until you don't reach the link  
            if self.head.get_data()==data:
                self.head = bufferHead
                return True
            self.head = self.head.get_next()
            
        self.head = bufferHead #redundant because it is already reached
        return False if self.head.get_data() != data else True

    
    def remove(self,data):
        bufferHead = self.head
        prevData = self.head
        self.head = self.head.get_next()
        while(self.head != bufferHead):
            if self.head.get_data()==data:
                prevData.set_next_node(self.head.get_next())     #this delinks the current node from previous nodes and sets it to next node 
                self.head = bufferHead
                self.size-=1
                return True
            else:
                prevData = self.head
                self.head = self.head.get_next()

        if(self.head.get_data() == data):
            prevData.set_next_node(self.head.get_next())
            self.size-=1
            return True
            
        return False


    def get_size(self):
        return self.size

    def __repr__(self):
        data='['
        bufferHead = self.head
        self.head = self.head.get_next()
        data = data + (f'{bufferHead.get_data()}')
        while(self.head != bufferHead):
            data =data+ (f',{self.head.get_data()}')
            self.head= self.head.get_next()
        return data+']'


        



            
            
        
                
            







circ = CircularLinkedList()
circ.insert(12)
circ.insert(14)
circ.insert(33)
circ.insert(332)
circ.insert(223)
circ.remove(12)
circ.insert(3233)

print(circ.search(3233))
circ.insert(22333)
print(circ)
