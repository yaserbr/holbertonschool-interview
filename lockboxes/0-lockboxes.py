#!/usr/bin/python3
"""Lockboxes module."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, otherwise False."""
    opened = set()

    def open_box(box_index):
        """Recursively open reachable boxes."""
        if box_index in opened:
            return

        if box_index < 0 or box_index >= len(boxes):
            return

        opened.add(box_index)

        for key in boxes[box_index]:
            open_box(key)

    open_box(0)

    return len(opened) == len(boxes)
