from random import shuffle, randint
from app.animation_manager import Animation_Manager

def main():
    #creating a list of data
    data = list(range(1, 31)) 
    #randomizing the list
    shuffle(data)
    #choosing a random k value that is within the data set
    random_k_digits = randint(1, len(data)) 
    #sending data to Animation_Manager for generating the plots
    animation_manager = Animation_Manager(data=data, k_digits=random_k_digits)
    #creating the plots for each sorting algorithm
    animation_manager.visualize_bubble_sort()
    animation_manager.visualize_quick_sort()

if __name__ == "__main__":
    main()