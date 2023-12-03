class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_desc = sorted(nums, reverse=True)

        for i in range(1, len(sorted_desc)+1):
            if i == k:
                return sorted_desc[i-1]
                