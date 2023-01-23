class Sorting_Algorithms:
    '''
    Description: this class encompasses all of the necessary functions for sorting in the program.
    _swap() does what it says on the tin. it swaps two values.
    bubble_sort() also does what it says on the tin. it's a standard bubble sort algorithm that sorts it lowest on the left and highest on the right.
    quicksort() is a version of quicksort used to find the top k values quicker than a normal quicksort. Instead of sorting the entire array, it goes left or right after the partition step, then compares k until the partition index = k.
    '''
    
    def __init__(self):
        pass
    
    def _swap(self,data, i, j):
        data[i], data[j] = data[j], data[i]
  
    def bubble_sort(self, data, k_digits = 0):
        swapped = True
        
        for i in range(k_digits):
            if not swapped:
                yield {'list': data, 'is_sorting_done': True} # returning dictionary to return current data and indicator that sorting is done
                return
            swapped = False
            
            for j in range(len(data) - 1 - i):
                if data[j] > data[j + 1]:
                    self._swap(data, j, j + 1)
                    swapped = True
                yield {'list': data, 'is_sorting_done': False} # returning dictionary to return current data and indicator that sorting is done

        yield {'list': data, 'is_sorting_done': True} # returning dictionary to return current data and indicator that sorting is done
        return

    def quicksort(self, A, start, end, k):
        '''
        Description: runs a modified version of quicksort that only returns the top k values of an array.
        self: refers to itself
        A(array): the array where we try to find the top k values
        start(int): the start index used in the function
        end(int): the end index used in the function
        k(int): the threshold number, the target number of top numbers we want to find
        '''
        
        # set up pivot as the last item of the array
        pivot = A[end]
        pivotIdx = start
        
        # Base Case no. 1
        if start >= end:
            yield {'list': A, 'is_sorting_done': True, 'finish_index': [pivotIdx, end]}
            return
        
        
        # pivot step
        for i in range(start, end):
            if A[i] >= pivot:
                self._swap(A, i, pivotIdx)
                pivotIdx += 1
            yield {'list': A, 'is_sorting_done': False, 'finish_index': None}
        self._swap(A, end, pivotIdx)
        
        # recursive step/base case no.2
        if(k < pivotIdx): # if k is less than pivot, go left
            yield {'list': A, 'is_sorting_done': False, 'finish_index': [pivotIdx, end]}
            yield from self.quicksort(A, start, pivotIdx - 1, k)
        elif(k > pivotIdx): # if k is greater than pivot, go right
            yield {'list': A, 'is_sorting_done': False, 'finish_index': None}
            yield from self.quicksort(A, pivotIdx + 1, end, k)
        else: # if k is equal to the pivot, we've found the top values.
            yield {'list': A, 'is_sorting_done': True, 'finish_index': [pivotIdx, end]}
            return
