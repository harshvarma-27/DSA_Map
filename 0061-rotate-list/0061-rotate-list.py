class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        values = []
        curr = head

        while curr:
            values.append(curr.val)
            curr = curr.next

        k %= len(values)
        values = values[-k:] + values[:-k]

        curr = head
        for val in values:
            curr.val = val
            curr = curr.next

        return head