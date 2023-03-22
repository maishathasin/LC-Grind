# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        val = {}
        while head != None:
            if head.next == None:
                return False
            else:
                if head in val:
                    return True
                else:
                    val[head] = 1
                    head = head.next
                
            
        