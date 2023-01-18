from random import shuffle, randint
from app.animation_manager import Animation_Manager

def main():
    data = list(range(1, 31))
    shuffle(data)
    random_k_digits = randint(1, len(data))
    animation_manager = Animation_Manager(data=data, k_digits=random_k_digits)
    animation_manager.visualize_bubble_sort()
    animation_manager.visualize_quick_sort()

if __name__ == "__main__":
    main()