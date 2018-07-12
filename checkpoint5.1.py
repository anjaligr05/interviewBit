class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
         out = set()
         self.permuteRec(A, 0, len(A)-1, out)
         return list(out)
    def permuteRec(self, A, l, r, out):
        if l==r:
            out.add(tuple(A))
        else:
            for i in range(l, r+1):
                A[l], A[i] = A[i], A[l]
                self.permuteRec(A, l+1, r, out)
                A[l], A[i] = A[i], A[l]
a = Solution()
print a.permute([1,2,3])
