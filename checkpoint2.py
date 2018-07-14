class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        n = A + (A-1)
        matrix = [[0]*n for i in range(n)]
        
        temp = 0
        ncopy = n
        while temp<ncopy:
            for i in range(temp, n):
                for j in range(temp, n):
                    if i == temp or j == temp or i == n-1 or j == n-1:
                        matrix[i][j] = A
            temp +=1
            n-=1
            A -=1
            
        return matrix
a = Solution()
print a.prettyPrint(4)
