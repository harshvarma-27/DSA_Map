class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float("inf")
        n = len(nums)

        for k in range(l, r + 1):
            s = sum(nums[:k])

            if s > 0:
                ans = min(ans, s)

            for i in range(k, n):
                s += nums[i] - nums[i - k]

                if s > 0:
                    ans = min(ans, s)

        return -1 if ans == float("inf") else ans