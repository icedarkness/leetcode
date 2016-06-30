# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        digit = ListNode(0)
        count_i = 0
        l3 = []
        while (l1 != None or l2 != None or (l1 == None and digit!= None and digit.val != 0)):
            if l1 != None and l2 == None:
                l2 = ListNode(0)
            elif l2 != None and l1 == None:
                l1 = ListNode(0)
            if l1 != None:
                digit.next = ListNode(int((l1.val+l2.val+digit.val)/10))
                temp_value = (l1.val+l2.val)%10
            else: 
                digit.next = None
                temp_value = 0
            l3.append(ListNode((temp_value+digit.val)%10))
            if count_i >= 1:
                l3[count_i-1].next = l3[count_i]
            count_i += 1
            digit = digit.next
            if l1 != None:
                l1 = l1.next
                l2 = l2.next
        return l3[0]
