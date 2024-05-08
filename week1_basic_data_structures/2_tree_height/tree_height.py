# python3

import sys
import threading

from collections import defaultdict


def compute_height(n, parents):
    # creating a dictionary for easily accessing
    # the children of a node in the tree
    children = defaultdict(list)
    root = -1
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            children[parent].append(i)

    # Using a stack to visit all nodes in the tree
    # and determine the height of the tree
    stack = [(root, 1)]
    maxhgt = 1
    while stack:
        node, height = stack.pop()
        maxhgt = max(maxhgt, height)
        for child in children[node]:
            stack.append((child, height + 1))
    return maxhgt


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
