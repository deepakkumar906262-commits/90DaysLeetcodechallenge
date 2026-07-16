# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a=[]
        temp=head
        while temp:
            a.append(temp.val)
            temp=temp.next
        
        a.sort()
        temp=head
        i=0
        while temp:
            temp.val=a[i]
            i+=1
            temp=temp.next
        return head