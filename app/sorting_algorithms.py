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