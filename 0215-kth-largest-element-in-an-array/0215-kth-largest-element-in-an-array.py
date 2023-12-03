class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_list_desc = sorted(nums, reverse=True)

        for i in range(1, len(sorted_list_desc)+1):
            if i == k:
                return sorted_list_desc[i-1]
                