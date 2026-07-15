# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head
        group_prev=dummy
        while True:
            kth_node=self.get_kth_node(group_prev,k)
            if not kth_node:
                break
            next_group=kth_node.next
            prev=next_group
            curr=group_prev.next
            for i in range(k):
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            temp=group_prev.next
            group_prev.next=kth_node
            group_prev=temp
        return dummy.next
    def get_kth_node(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr