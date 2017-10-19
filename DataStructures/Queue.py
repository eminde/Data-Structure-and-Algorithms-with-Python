#Queue.py
#20 Oct 2017
#Written By Amin Dehghan
#DS & Algorithms With Python

class Queue:
    def __init__(self):
        self.items=[]
        self.fronIdx=0
    
    
    def __compress(self):
        newlst=[]
        for i in range(self.frontIdx,len(self.items)):
            newlst.append(self.items[i])
            
        self.items=newlst
        self.frontIdx=0
        
        
    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to dequeue an empty queue")
        
        if self.froniIdx*2< len(self.items):
            self.__compress()
        
        item=self.items[self.frontIdx]
        self.frontIdx+=1
        return item
    
    def enqueue(self,val):
        self.items.append(val)
        
    def front(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to access front of empty queue")
        
        return self.items[frontIdx]
    
    def isEmpty(self):
        return len(self.items)==frontIdx
    
    