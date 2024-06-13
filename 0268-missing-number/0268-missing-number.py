class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        count = 0
        for i in range(len(sorted_nums)):
            if sorted_nums[i] != count:
                return sorted_nums[i] - 1
            elif i == len(sorted_nums)-1:
                return sorted_nums[i] + 1

            count += 1
        