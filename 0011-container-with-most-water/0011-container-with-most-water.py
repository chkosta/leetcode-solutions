class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            a = right - left
            b = min(height[left], height[right])

            water = a * b
            max_water = max(water, max_water)

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return max_water
