"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
  Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
  Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
  Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""


def isSubsequence(s: str, t: str) -> bool:

    # empty string is always substring
    if len(s) == 0:
        return True

    # check if characters in s exist also in t
    if not set(s) <= set(t):
        return False

    substring_index = 0
    for char in t:
        # deal with running out of bounds when checking the substring
        if substring_index < len(s):
            # we found a match, so we continue with the next substring character
            if char == s[substring_index]:
                substring_index += 1

    return substring_index == len(s)


test_input_1a = "abc"
test_input_1b = "ahbgdc"

test_input_2a = "axc"
test_input_2b = "ahbgdc"

assert isSubsequence(test_input_1a, test_input_1b) is True
assert isSubsequence(test_input_2a, test_input_2b) is False
