import random
from app.animation_manager import Animation_Manager

def main():
    data = list(range(1, 31))
    random.shuffle(data)

    animation_manager = Animation_Manager(data=data)
    animation_manager.visualize_bubble_sort()

if __name__ == "__main__":
    main()