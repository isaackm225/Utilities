# Merge sort implementation in Python
# Note that python offers the .sort() method
#L
def merge_sort(A: list)-> None:
    """sorts a list in place"""
    #check for extreme case where list len is 1
    if len(A)>1:
        # find midpoint
        mid = len(A)//2
        #slice list in 2
        L = A[:mid]
        R = A[mid:]
        #call recursion
        merge_sort(L)
        merge_sort(R)
        #initialize indexes
        i=0
        j=0
        k=0
        #while L and R have unsorted elem:
        while i<len(L) and j<len(R):
            #Compare L[i] and R[j] and smaller goes to A[k] whoever has the smaller elem takes +1 to its index
            if L[i]<R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
            '''elif R[j]<L[i]:
                A[k] = R[j]
                j += 1
                k += 1
            '''
        #Dump remainder into A 
        while i< len(L):
            A[k] = L[i]
            i+=1
            k+=1
        while j< len(R):
            A[k] = R[j]
            j+=1
            k+=1
        

if __name__=="__main__":
    a = [4,7,8,3,1,6]
    merge_sort(a)
    print(a)