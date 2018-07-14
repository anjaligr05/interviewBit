# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        temp = A
        totLen = 0
        
        while temp:
            temp = temp.next
            totLen +=1
            
        n = int(totLen/2)
        newN = n
        temp = A
        for l in range(0, n):
            prev = temp
            temp = temp.next
            
        if totLen%2==0:
            revstart = temp
        else:
            prev = temp
            revstart = temp.next
        prevNode = None
        firstRev = revstart
        while revstart:
            node = revstart.next
            revstart.next = prevNode
            prevNode = revstart
            revstart = node
        prev.next = prevNode
        
        ptr = prevNode
        head = A
        for i in range(n):
           head.val = ptr.val-head.val
           head = head.next
           ptr=ptr.next
        
        
        newPrev = None
        revstart = prevNode
        while revstart:
            node = revstart.next
            revstart.next = newPrev
            newPrev = revstart
            revstart = node
        prev.next = newPrev
        return A

