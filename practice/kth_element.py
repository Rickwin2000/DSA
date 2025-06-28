import heapq



def kth_biggest_element():
    arr = [1, 4, 8, 2, 90, 3]
    heap = []
    k = 1

    if len(arr) <= k:
        return
    
    for val in arr:
        heapq.heappush(heap, val)

        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

def kth_smallest_element():
    arr = [1, 4, 8, 2, 90, 3]
    heap = []
    k = 2

    if len(arr) <= k:
        return

    heapq.heapify(arr)    
    
    for val in range(k):
        kth = heapq.heappop(arr)
    
    return kth
        

print(kth_biggest_element())
