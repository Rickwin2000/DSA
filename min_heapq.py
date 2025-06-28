import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        # Move last to root and bubble down
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return min_val

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)

    def _bubble_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        n = len(self.heap)

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def __str__(self):
        return str(self.heap)


def min_heapq():
    nums = [9, 5, 2, 11, 7]
    heapq.heapify(nums)

    heap = []
    heapq.heappush(heap, 5)
    heapq.heappush(heap, 90)
    heapq.heappush(heap, 1)
    # heapq.heappop(heap)

    print(heap[0])

min_heapq()