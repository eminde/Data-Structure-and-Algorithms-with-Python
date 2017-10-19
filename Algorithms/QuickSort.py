#QuickSort.py
# 20 Oct 2017
#written by Amin dehghan
#DS & Algorithms With Python
  

def partition(seq,start,stop):
    i=start+1
    j=stop-1
    
    while i<=j:
        
        while seq[i]<seq[start] and i<=j:
            i+=1
        while seq[j]>seq[start] and i<=j:
            j-=1
        if i<j:
            temp=seq[i]
            seq[i]=seq[j]
            seq[j]=temp
            i+=1
            j-=1
            
    temp=seq[start]
    seq[start]=seq[j]
    seq[j]=temp
    
    return j
    
def quickrecursion(seq,start,stop):
    
    if start>=stop-1:
        return
    
    pivotIndex=partition(seq,start,stop)
    
    quickrecursion(seq,start,pivotIndex)
    quickrecursion(seq,pivotIndex+1,stop)
    
    
def quickSort(seq):
    quickrecursion(seq,0,len(seq))

def main():
    seq=[11,2,21,8,3,54,23,12,6,9]
    quickSort(seq)
    print(seq)
    
if __name__=="__main__":
    main()
