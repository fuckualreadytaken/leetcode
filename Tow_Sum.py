#! /usr/bin/env python
# -*-coding:utf-8-*-
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # version 1 brute force
        # for (index1, n1) in enumerate(nums):
        #     index1 += 1
        #
        #     for (index2, n2) in enumerate(nums[index1:]):
        #         index2 += index1
        #         if n1 + n2 == target:
        #             res = [index1 - 1, index2]
        #
        # return res

        # version 2 hash table
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
