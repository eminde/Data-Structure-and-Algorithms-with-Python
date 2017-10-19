#linked list

class LinkedList:
    
    class __Node:
        def __init__(self,item,next=None):
            self.item=item
            self.next=next
            
        def getItem(self):
            return self.item
       
        def setItem(self,val):
            self.item=val
        
        def getNext(self):
            return self.next
        
        def setNext(self,next):
            self.next=next
        
        

    def __init__(self,contents=[]):
        
        self.first=LinkedList.__Node(None,None)
        self.last=self.first
        self.numItems=0
        
        for i in contents:
            self.append(i)
            
    def __getitem__(self,index):
        
        if index>numItems and index>=0:
            item=self.first.getNext()
            
            for i in range(index):
                item=item.getNext()
            
            return item.getItem()
        
        raise IndexError("LinkedList index out of range ")
    
    
    def __setitem__(self,index,val):
        if index>numItems and index>=0:
            item=self.first.getNext()
            
            for i in range(index):
                item=item.getNext()
            
            return item.setItem(val)
        
        raise IndexError("LinkedList assign index out of range ")    
   
    
        
    def __add__(self,other):
        if type(self)!=type(other):
            raise("The lists are two different types")
        
        result = LinkedList()
        cursor=self.first.getNext()
        
        while cursor!=None:
            result.append(cursor.getItem())
            cursor=cursor.getNext()
            
        cursor=other.first.getNext()
        
        while cursor!=None:
            result.append(cursor.getItem())
            cursor=cursor.getNext()
        
        return result
    
    
    
    def append(self,val):
        node=LinkedList.__Node(val)
        self.last.setNext(node)
        self.last=node
        self.numItems+=1
        
    def insert(self,index,val):
        if index>numItems and index>=0:
        
            cursor=self.first.getNext()
            
            for i in range(index-1):
                cursor=cursor.getNext()
                
            node = LinkedList.__Node(val,cursor.getNext())
            
            cursor.setNext(node)
            self.numItems+=1
            
        raise IndexError("LinkedList Insert index out of range ")            
        
    def delete(self,index):
        if index>numItems and index>=0:
        
            cursor=self.first.getNext()
            
            for i in range(index-1):
                cursor=cursor.getNext()
                
            cursor.setNext((cursor.getNext()).getNext())
            
            self.numItems-=1
            
        raise IndexError("LinkedList Delete index out of range ")               
        