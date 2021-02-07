#Merge sort practice 
#Sort which works on divide and conquer
#Splits and recurses over split arrays until single element arrays are created
#Compare, sort and merge arrays

def mergesort(arr):
  if len(arr)>1:
    mid = len(arr)//2
    L=arr[:mid]
    R=arr[mid:]
    mergesort(L)
    mergesort(R)
    i = j = k = 0 
#Compare and sort values in main array
    while i<len(L) and j<len(R):
      
      if L[i] < R[j]:
        arr[k] = L[i]
        i+=1
        
      else:
        arr[k] = R[j]
        j+=1

      k+=1
  #Add remaining values to array   
    while i < len(L):
      arr[k] = L[i]
      i+=1
      k+=1
      
#Add remaining values to array 
    while j < len(R):
      arr[k] = R[j]
      j+=1
      k+=1
  
  return arr


z=[1,14,5,3,9]
y=mergesort(z)
print(y)