class Sorting_Algorithms:
    def __init__(self):
        pass
    
    def _swap(self,data, i, j):
        data[i], data[j] = data[j], data[i]
  
    def bubble_sort(self, data):
        swapped = True
        
        for i in range(len(data) - 1):
            if not swapped:
                yield {'list': data, 'is_sorting_done': True} # returning dictionary to return current data and indicator that sorting is done
                return
            swapped = False
            
            for j in range(len(data) - 1 - i):
                if data[j] > data[j + 1]:
                    self._swap(data, j, j + 1)
                    swapped = True
                yield {'list': data, 'is_sorting_done': False} # returning dictionary to return current data and indicator that sorting is done
    

    def quicksort(self, A, start, end, k):
        if start >= end:
            return

        pivot = A[end]
        pivotIdx = start

        for i in range(start, end):
            if A[i] > pivot:
                self._swap(A, i, pivotIdx)
                pivotIdx += 1
            yield {'list': A, 'is_sorting_done': False}
        self._swap(A, end, pivotIdx)

        if(k - 1< pivotIdx):
            yield {'list': A, 'is_sorting_done': False}
            yield from self.quicksort(A, start, pivotIdx - 1, k)
        elif(k > pivotIdx):
            yield {'list': A, 'is_sorting_done': False}
            yield from self.quicksort(A, pivotIdx + 1, end, k)
        else:
            print('done in sorting method') 
            yield {'list': A, 'is_sorting_done': True}
            return