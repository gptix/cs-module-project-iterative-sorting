# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    
    out_of_range = len(arr)
    
    for i in range(out_of_range):
        current_index = i
        index_of_smallest_so_far = current_index       

        # find next smallest element
        for is_this_smaller in range(current_index+1, out_of_range):
            if arr[is_this_smaller] < arr[index_of_smallest_so_far]:
                index_of_smallest_so_far = is_this_smaller
                
        # swap
        hold_a_sec = arr[current_index]
        arr[current_index] = arr[index_of_smallest_so_far]
        arr[index_of_smallest_so_far] = hold_a_sec
        
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    out_of_range = len(arr)
    for left in range(out_of_range - 1): # no point in comparing the last element to itself
        for right in range(left + 1, out_of_range):
            if arr[left] > arr[right]:
                hold_a_sec = arr[left]
                arr[left] = arr[right]
                arr[right] = hold_a_sec
    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
