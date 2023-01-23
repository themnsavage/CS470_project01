class Sorting_Algorithms:
    def __init__(self):
        pass
    
    def _swap(self,data, i, j):
        ''' description: helper function used in bubble sort to swap two items in a list
            data: input list
            i: type int used to index into the list and will swap with j
            j: type int used to index into the list and will swap with i
        '''
        data[i], data[j] = data[j], data[i]
  
    def bubble_sort(self, data, k_digits = 0):
        '''
            description: bubble sort algorithm used to sort the input list in O(n^2) time complexity
            data: input list to be sorted
            k_digits: input k type int which is used to determine how many elements will be sorted; if no input, default to 0
        '''
        swapped = True
        
        for i in range(k_digits): #for loop to check if list already sorted
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
        
        pivot = A[end]
        pivotIdx = start
        
        if start >= end:
            yield {'list': A, 'is_sorting_done': True, 'finish_index': [pivotIdx, end]}
            return

        for i in range(start, end):
            if A[i] >= pivot:
                self._swap(A, i, pivotIdx)
                pivotIdx += 1
            yield {'list': A, 'is_sorting_done': False, 'finish_index': None}
        self._swap(A, end, pivotIdx)
        if(k < pivotIdx):
            yield {'list': A, 'is_sorting_done': False, 'finish_index': [pivotIdx, end]}
            yield from self.quicksort(A, start, pivotIdx - 1, k)
        elif(k > pivotIdx):
            yield {'list': A, 'is_sorting_done': False, 'finish_index': None}
            yield from self.quicksort(A, pivotIdx + 1, end, k)
        else:
            yield {'list': A, 'is_sorting_done': True, 'finish_index': [pivotIdx, end]}
            return