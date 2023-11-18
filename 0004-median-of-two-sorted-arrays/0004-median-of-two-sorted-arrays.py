class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        con_list = nums1 + nums2
        sorted_list = sorted(con_list)

        if (len(sorted_list) % 2 != 0):
            m = len(sorted_list) // 2
            median = sorted_list[m]
            return median

        if (len(sorted_list) % 2 == 0):
            m = len(sorted_list) // 2
            median = (sorted_list[m] + sorted_list[m-1]) / 2
            return median
