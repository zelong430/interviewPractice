"""
***********************************************************************************************************************
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.
***********************************************************************************************************************

Example:
    longestPalindromicSubstring("abcdzdcab")
    -> cdzdc

"""

class Solution(object):
    def __init__(self):
        self.a = 0

    def longestPalindromicSubstringDP(self, s):
        """
        :param s: str
        :return: int
        """
        maxStr = ""
        paddedStr = "#"
        for char in s:
            paddedStr += char + "#"

        for index, center in enumerate(paddedStr):
            i = 0
            while index - i >= 0 and index + i < len(paddedStr) and paddedStr[index + i] == paddedStr[index - i]:
                temp = paddedStr[index - i: index + i + 1]
                if len(temp) > len(maxStr):
                    maxStr = temp
                i += 1

        return maxStr.replace("#", "")

def execute():
    sol = Solution()
    print(sol.longestPalindromicSubstringDP(""))
    assert sol.longestPalindromicSubstringDP("bb") == "bb"
    assert sol.longestPalindromicSubstringDP("abcdzdcab") == "cdzdc"

if __name__ == "__main__":
    execute()