# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : integer
    # @return a list of TreeNode 
    def constructTree(self, start, end):
        bsts = []
        if start > end:
            bsts.append(None)
            return bsts
        for i in range(start, end+1):
            left = self.constructTree(start, i-1)
            right = self.constructTree(i+1, end)
            for j in range(len(left)):
                leftNode = left[j]
                for k in range(len(right)):
                    rightNode = right[k]
                    node = TreeNode(i)
                    node.left = leftNode
                    node.right = rightNode
                    bsts.append(node)
        return bsts
            
    def generateTrees(self, A):
        return self.constructTree(1, A)
a = Solution()
print a.generateTrees(3)       
        
        

