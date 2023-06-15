def merge_sort(arr):
    comparisons = 0
    if len(arr) > 1:
        mid = len(arr)//2
        
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0 # i index of left, j index of right, and k index of array
        
        #store the smallest elements in the array
        while i < len(left) and j < len(right):
            if left[i] <= right[j]: #if the left element is smaller we add it first
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j] #otherwise add the right first
                j+=1
            k+=1
            comparisons+=1
            
        #update the array with the remaining elements
        #remaining elements in the left array
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
            
        #remaining elements are in the right array
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
            
    return comparisons

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
# Driver Code
if __name__ == '__main__':
    arr = [5, 3, 10, 6, 9, 20, 1, 4, 3]
    print("Given array is", end="\n")
    printList(arr)
    comparisons = merge_sort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
    print("Number of comparisons:", comparisons)





