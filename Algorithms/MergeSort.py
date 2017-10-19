#MergeSort.py
# 20 Oct 2017
#written by Amin dehghan
#DS & Algorithms With Python

def merge(seq,start,mid,stop):
    lst=[]
    i=start
    j=mid
    
    while i<mid and j<stop:
        if seq[i]<seq[j]:
            lst.append(seq[i])
            i+=1
        else:
            lst.append(seq[j])
            j+=1
        
    while i<mid:
        lst.append(seq[i])
        i+=1
    
    for i in range(len(lst)):
        seq[start+i]=lst[i]
    
        
        



def mergerecursion(seq,start,stop):
    
    if start>stop-1:
        return 
    
    mid = (start+stop)//2
    
    mergerecursion(seq,start,mid)
    mergerecursion(seq,mid,stop)
    
    merge(seq,start,mid,stop)
    
    
    

def mergeSort(seq):
    
    mergerecursion(seq,0,len(seq))
    
