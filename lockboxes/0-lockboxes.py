#!/usr/bin/python3
"""Lockboxes module."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened."""
    opened = {0}
    to_check = [0]

    while to_check:
        box = to_check.pop()

        for key in boxes[box]:
            if key < len(boxes) and key not in opened:
                opened.add(key)
                to_check.append(key)

    return len(opened) == len(boxes)
