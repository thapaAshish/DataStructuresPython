

'''

 Minimum number of throws required to win snake game

'''

from collections import deque  
#to act like regual queue, one that supports first in last out  use popLeft() in conjunction with append


class edge:
    def __init__(self,source,dest):
        self.source = source
        self.dest = dest

class Node:
    def __init__(self,vertex,weight):
        self.vertex = vertex
        self.weight = weight



""" 
adjacency list used to represent graph
dictionary is used to represent adjacency list
and list is used for one dimensional use purpose
The graph is directed and unweighted
"""
class Graph:
    def __init__(self,edges,TotalElement):
        
        self.adjacencyList = dict()
        """
        creating empty lists for source element in edge to store all their destination links ; 
        i.e if my posiion is 0 then i should be able to 1,2,3,4,5,6 as my destination in my dict . btw these are dice roll cases
        """
        for i in range(0,TotalElement):
            self.adjacencyList[i] = list()  #not required but still allocating things explicitly makes this code easier to digest
        

        for i in range(0,len(edges)):
            source=edges[i].source
            dest=edges[i].dest
            
            '''
            btw there are around 94*6+5+4+3+2+1 -16*5 + 16 edges in total, why +16*5? because these are snake, or ladder. why -16 ? its edge would have been 6 items next to it but now there is only one
            '''
            self.adjacencyList[source].append(dest)
        

class SnakeAndLadder:
    
    #static method means no self required
    @staticmethod
    def Search(graph,source,N): 
        print("search called")
         #graph is graph object itself 
        Queue = deque()
        Discovered=[False]*(N+1)

        #first initialization should be done for logic of BFS to work
        Discovered[source] = True
        node = Node(source,0) #weight of 0
        Queue.append(node)

        while Queue != deque([]):
            node=Queue.popleft()
            if(node.vertex == N):
                print("solution found, The minimum amount of rolls needed is {}".format(node.weight))
                break
            for u in graph.adjacencyList[node.vertex]: #multidimensional array if confused
                if not Discovered[u]:
                    #mark this discovered and push the vertex to queue
                    Discovered[u]=True
                    n = Node(u,node.weight+1)
                    Queue.append(n)
     

    @staticmethod
    def Solution(ladder,snake):  #ladder and snake are dictionaries
        print('solution called')
        N = 10*10 #snake and ladder is 10 * 10 big matrix. Which also happens to be number of vertex in our graph

        edges = list()
        for i in range(N):
            for j in range(1,7):
                src=i
                if(i+j>100):
                    break

                """ 
                a dice roll has 6 possible outcome.
                Within these 6 possible outcomes is there a snake or ladder
                if there is then add to the edge
                """
                Ladder= ladder[i+j] if ladder.get(i+j) != None else 0
                Snake = snake[i+j] if snake.get(i+j) != None else 0

                if Ladder != 0 or Snake != 0:
                    dest = Ladder+Snake #can't be ladder and snake at same time. so one should always be zero
                else:
                    dest=i+j
                
                edges.append(edge(src,dest))
        
        graph = Graph(edges,N)
        SnakeAndLadder.Search(graph,0,N)



#main logic
ladderStart = [1,4,9,21,28,51,72,80]
ladderEnd = [38,14,31,42,84,67,91,99]

ladder = dict(zip(ladderStart,ladderEnd))

snakeHead = [17,54,62,64,87,93,95,98]
snakeTail =[7,34,19,60,36,73,75,79]

snake=dict(zip(snakeHead,snakeTail))

SnakeAndLadder.Solution(ladder,snake)


            








        


