from random import shuffle
from app.animation_manager import Animation_Manager

def main():
    data = list(range(1, 31))
    shuffle(data)

    animation_manager = Animation_Manager(data=data, k_digits=5)
    # animation_manager.visualize_bubble_sort()
    animation_manager.visualize_quick_sort()

if __name__ == "__main__":
    main()