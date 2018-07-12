class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        hashmap = set()
        for e in A:
            hashmap.add(e)
        res = 0
        for i in range(len(A)):
            if A[i]-1 not in hashmap:
                j = A[i]
                while j in hashmap:
                    j+=1
                res = max(res, j-A[i])
        return res
a = Solution()
print a.longestConsecutive([34,35,4,37,3,2,1])

