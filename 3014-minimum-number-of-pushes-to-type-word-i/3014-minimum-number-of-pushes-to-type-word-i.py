class Solution:

    def minimumPushes(self, word: str) -> int:
        push_map = {}

        for i, char in enumerate(word):
            push_map[char] = (i // 8) + 1

        total_pushes = 0
        for char in word:
            total_pushes += push_map[char]

        return total_pushes