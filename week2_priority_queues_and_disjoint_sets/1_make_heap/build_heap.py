# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following implementation does a siftdown procedure for all elements in the input array
    # starting from the (n/2)th element up to the first one.
    def sift_down(i):
        swap = True
        swaps = list()
        while swap:
            child1 = 2*i
            child2 = 2*i+1
            min_ = i
            if child1 < len(data):
                if data[child1] < data[min_]:
                    min_ = child1
            if child2 < len(data):
                if data[child2] < data[min_]:
                    min_ = child2
            if min_ != i:
                data[min_], data[i] = data[i], data[min_] # swap the two elements
                swaps.append((min_, i))
            else:
                swap = False
        return swaps

    swaps = []
    for i in range(int(len(data)/2), -1, -1):
        swaps.extend(sift_down(i))
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
