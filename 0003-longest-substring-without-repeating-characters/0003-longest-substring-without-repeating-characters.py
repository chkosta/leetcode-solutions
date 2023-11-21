class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        mapping = {}
        start = 0
        max_len = 0

        for i in range(len(s)):
            if s[i] in mapping and mapping[s[i]] >= start:
                start = mapping[s[i]] + 1

            mapping[s[i]] = i
            max_len = max(max_len, i - start + 1)

        return max_len
    