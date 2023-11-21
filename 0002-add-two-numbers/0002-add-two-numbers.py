# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        while(l1):
            num1 = str(l1.val) + num1
            l1 = l1.next

        while(l2):
            num2 = str(l2.val) + num2
            l2 = l2.next

        sum = str(int(num1) + int(num2))
        
        result = None
        for i in range(len(sum)):
            result = ListNode(int(sum[i]), result)

        return result
    