#Stack.py
# 20 Oct 2017
#written by Amin Dehghan
#DS & Algorithms With Python

class Stack:
    def __init__(self):
        self.items=[]
        
    def push(self,val):
        self.items.append(val)
        
    def isEmpty(self):
        return len(self.items)==0
    
    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Trying to pop an empty stack")
        
        topindex=len(self.items)-1
        pop=self.items[topindex]
        del self.items[topindex]
        return pop
    
    def top(self):
        if self.isEmpty():
            raise RuntimeError("Trying to reach the top of an empty stack")        
        
        return self.items[len(self.items)-1]
