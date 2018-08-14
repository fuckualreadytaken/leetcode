#! /usr/bin/env python
# coding=utf-8

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        li = nums1 + nums2
        li.sort()
        length = len(li)
        if length % 2:
            mid = li[length / 2]
        else:
            mid = (li[int(length / 2) - 1] + li[int(length / 2)]) * 0.5
        return mid


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    solve = Solution()
    print(solve.findMedianSortedArrays(nums1, nums2))
