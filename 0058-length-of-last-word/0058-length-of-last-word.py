class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_array = s.split()
        
        return len(s_array[-1])