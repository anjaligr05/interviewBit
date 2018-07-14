import heapq
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        h = []
        for i in range(len(A)):
            heapq.heappush(h, A[i])
        j = 0
        while j<B-1:
            heapq.heappop(h)
            j += 1
        return heapq.heappop(h)

