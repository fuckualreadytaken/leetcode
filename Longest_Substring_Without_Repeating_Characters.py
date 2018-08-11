#! /usr/bin/env python
# -*-coding:utf-8-*-

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # version1, bad slid window , it is too slow
        # start = 0
        # end = 0
        # longest = end - start + 1
        # while end != len(s) - 1:
        #     end += 1
        #     if len(list(s[start:end])) != len(set(s[start:end])):
        #         start += 1
        #     if end - start > longest:
        #         longest = end - start
        #     print(start, end)
        # return longest

        # version2 slid window and hash table
        ans = 0
        dic = {}
        i = 0
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i)
            dic[s[j]] = j + 1
            ans = max(ans, j - i + 1)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))
