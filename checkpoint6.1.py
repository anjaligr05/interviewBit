class Solution:
    # @param A : list of integers
    # @return an integer
    def invcount(self, arr, count):
        mid = len(arr) / 2
        larr = arr[:mid]
        rarr = arr[mid:]
        if len(arr) > 1:
            # Divid and conquer with recursive calls
            # to left and right arrays similar to
            # merge sort algorithm
            self.invcount(larr, count)
            self.invcount(rarr, count)
            
            # Merge sorted sub-arrays and keep
            # count of split inversions
            i, j = 0, 0
            a = larr
            b = rarr
            for k in range(len(a) + len(b) + 1):
                if a[i] <= b[j]:
                    arr[k] = a[i]
                    i += 1
                    if i == len(a) and j != len(b):
                        while j != len(b):
                            k +=1
                            arr[k] = b[j]
                            j += 1
                        break
                elif a[i] > b[j]:
                    arr[k] = b[j]
                    count[0] += (len(a) - i)
                    j += 1
                    if j == len(b) and i != len(a):
                        while i != len(a):
                            k+= 1
                            arr[k] = a[i]
                            i += 1                    
                        break    
        return arr
     
    def countInversions(self, A):
        count = [0]
        self.invcount(A, count)
        return count[0]
a = Solution()
print a.countInversions([3,4,1,2,4]) 
