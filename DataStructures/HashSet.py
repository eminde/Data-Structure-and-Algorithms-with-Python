#HashSet.py
#3 Nov 2017
#written by Amin Dehghan 
#DS & Algorithms With Python


class  HashSet:

    def __init__ (self,contents=[]) :
        self.items = [None] * 10 
        self.numItems = 0
        
        for item in contents :
            self.add(item)



    def __add(items,item):
        
        index = hash(item)%len(items)
        loc = -1
        
        
        while items[index]!=None:
            if items[index]==item:
                #item exists in set 
                return False
            
            if loc <0 and type(items[index])==HashSet.__placeholder:
                loc = index
            
            index = (index+1)%len(items)

        if loc <0 :
            loc = index
        
        items[loc]=item

        return True

    def __rehash (oldlist ,newlist):
        
        for x in oldlist:
            if x!= None and type(x)!= self.__placeholder:
                HashSet.__add(newlist,x)
        
        return newlist

    def add(self , item):
        if HashSet.__add(self.items,item):
            self.numItems+=1
            load = numItems/len(self.items)
            if load> 0.75:
               self.items= HashSet.__rehash(self.items,[None]*2*len(self.items))

    class __placeholder:
        def __init__(self):
            pass

        def __eq__(set,other):
            return False

    

    def __remove (items , item ):
        idx = hash(item)%len(items)

        while items[idx]=! None:
            if items[idx]==item:
                nextidx = (idx+1)%len(items)
                if nextidx == None :
                    items[idx] = None 
                else:
                     items[idx]=HashSet.__placeholder
            
                return True
            idx=(idx+1)%len(items)

        return False 


    def remove(self , item):
        if self.__remove(self.items,item):
            numItems-=1
            load = numItems/len(self.items)
            if load<0.25:
                self.items = HashSet.__rehash(self.items,[None]*len(self.items)//2)

        else:
            raise KeyError("item is not in the set ")



    def __contain__(self , item):
        idx = hash(item)/len(self.items)

        while self.items[idx]!=None :
            if self.items[idx]==item:
                return True 

             idx=(idx+1)%len(self.items)

        return False 

    def __iter__(self):
        for x in self.items:
            if x!=None and type(x)!=HashSet.__placeholder:
                yield x 

        
        