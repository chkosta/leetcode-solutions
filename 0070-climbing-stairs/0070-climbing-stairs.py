class Solution:
    def climbStairs(self, n: int) -> int:
        step = 3
        sum1 = 1
        sum2 = 2
        next_sum = 0

        if n == 1 or n == 2:
            return n

        while step <= n:
            next_sum = sum1 + sum2
            sum1 = sum2
            sum2 = next_sum
            step = step + 1

        return next_sum
