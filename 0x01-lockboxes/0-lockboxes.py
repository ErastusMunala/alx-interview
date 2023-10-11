#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False  # No boxes, can't unlock any

    n = len(boxes)  # Total number of boxes
    unlocked = set()  # Set to track unlocked boxes

    # Initially, the first box (box 0) is unlocked
    unlocked.add(0)

    queue = [0]  # Initialize a queue for BFS with box 0

    while queue:
        current_box = queue.pop(0)  # Get the first box in the queue

        for key in boxes[current_box]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                queue.append(key)

    # If all boxes have been unlocked, return True
    return len(unlocked) == n
