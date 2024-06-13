class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # NOT CONSTANT SPACE SOLUTION
        # freq = {}

        # for num in nums:
        #     if num in freq:
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1

        # for key, value in freq.items():
        #     if value == 1:
        #         return key

        res = 0
        for num in nums:
            res ^= num

        return res
        