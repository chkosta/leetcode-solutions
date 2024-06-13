class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        for index, value in enumerate(s):
            if freq[value] == 1:
                return index

        return -1
