class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        for i in range(0, len(nodes) - 1, 2):
            nodes[i], nodes[i + 1] = nodes[i + 1], nodes[i]

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        nodes[-1].next = None

        return nodes[0]