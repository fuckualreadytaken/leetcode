#! /usr/bin/env python
# coding=utf-8

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # version1 Dynamic Programming
        ans = ""
        if len(s) != 0:
            ans = s[0]
        P = [[0 for a in range(len(s))] for b in range(len(s))]
        for i in range(len(s)):
            P[i][i] = 1
        for i in range(len(s)):
            if i + 1 == len(s):
                pass
            else:
                if s[i] == s[i + 1]:
                    P[i][i + 1] = 1
                    ans = s[i:i + 2]
                else:
                    P[i][i + 1] = 0
        i = 2
        while i < 1000:
            for j in range(len(s)):
                if j + i >= len(s):
                    pass
                else:
                    if s[j] == s[j + i] and P[j + 1][j + i - 1] == 1:
                        P[j][j + i] = 1
                        ans = s[j:j + i + 1]
                    else:
                        P[j][j + i] = 0
                # This part can be optimized
            i += 1
        # for i in P:
        #     print(i)
        return ans


if __name__ == "__main__":
    s = "acb"
    sl = Solution()
    print(sl.longestPalindrome(s))
