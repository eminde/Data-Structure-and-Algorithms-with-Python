#PyList.py
# 20 Oct 2017
#written by Amin dehghan
#DS & Algorithms With Python
#

class PyList:
    def __init__(self,contents=[],size=10):
        self.items=[None]*size
        self.numItems=0
        self.size=size
        
        for item in contents:
            self.append(item)
    def __getitem__(self,index):
        if index<numItems and index>=0:
            return self.items[index]
        raise IndexError("Pylist index out of range.")

    def __setitem__(self,index,val):
        if index>=0 and index<numItems:
            self.items[index]= val  
            return
        raise IndexError("PyList index out of range.")
    
    def __add__(self, other):
        result = PyList(size=self.numItems+other.numItems)
        for i in range(self.numItems):
            result.append(self.items[i])
            
        for i in range(other.numItems):
            result.append(other.items[i])
            
        return result
    
    def __makeroom (self):
        newlen = size+size/4
        newlist=[None]*newlen
        
        for i in range(self.numItems):
            newlist[i]=self.items[i]
        
        self.items=newlist
        self.size=newlen
        
    def append(self,val):
        if self.numItems==self.size:
            self.__makeroom()
          
        self.items[numItems]=val  
        self.numItems+=1
        
    def insert(self,index, val):
        if self.numItems==self.size:
            self.__makeroom()
        
        if index<self.numItems:
            for j in range(self.numItems-1,index-1,-1):
                self.items[j+1]=self.items[j]
            
            self.items[index]=val
            self.numItems+=1
        else:
            self.append(val)
            
    def delete (self, index):
        for i in range(index,self.numItems-1):
            self.items[i]=self.items[i+1]
        numItems-=1
            
    def __eq__(self,other):
        
        if type(self)!=type(other):
            return False
        
        if self.numItems!=other.numItems:
            return False
        
        for i in range(self.numItems):
            if self.items[i]!= other.items[i]:
                return False
            
        return True
    
    def __iter__(self):
        for i in range(self.numItems):
            yield self.items[i]
            
    def __len__(self):
        return self.numItems
    
    def __contains__ (self, e):
        for i in range(self.numItem):
            if self.items[i]==e:
                return 
            
        return False
    
    def __str__(self):
        s='['
        for i in range (self.numItems):
            s= s+ repr(self.items[i])
            if i<self.numItems-1:
                s+=','
        s+=']'
        return s
    
    def __repr__(self):
        s='Pylist(['
        for i in range (self.numItems):
            s= s+ repr(self.items[i])
            if i<self.numItems-1:
                s+=','
        s+= '])'
        return s
    
    
        
        
        
        
