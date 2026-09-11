class Solution:
    def removeNthFromEnd(self, head, n):
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        arr.pop(len(arr) - n)

        dummy = ListNode(0)
        curr = dummy

        for x in arr:
            curr.next = ListNode(x)
            curr = curr.next

        return dummy.next