class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for el in nums:
            subsets += [entry + [el] for entry in subsets]

        return subsets
