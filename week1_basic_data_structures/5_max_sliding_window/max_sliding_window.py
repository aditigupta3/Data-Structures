# python3
from heapq import heappush, heappop

def max_sliding_window_naive(sequence, m):
    """
    This problem can be solved easily using a max heap
    """
    if len(sequence) < m:
        return []
    
    heap = list()
    ans = list()
    # Pushing the first m elements into the heap
    for i in range(m):
        heappush(heap, (-sequence[i], i))
    # The element at the top of the heap is the maximum element
    ans.append(-heap[0][0])

    for i in range(m, len(sequence)):
        # Push ith element into the heap
        heappush(heap, (-sequence[i], i))
        # Keep popping the top if the top element lies before the window
        while heap[0][1] <= i-m:
            heappop(heap)
        # The element at the top of the heap is the maximum element
        ans.append(-heap[0][0])
    return ans

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

