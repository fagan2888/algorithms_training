
'''
5386. 检查一个字符串是否可以打破另一个字符串
给你两个字符串 s1 和 s2 ，它们长度相等，请你检查是否存在一个 s1  的排列可以打破 s2 的一个排列，或者是否存在一个 s2 的排列可以打破 s1 的一个排列。

字符串 x 可以打破字符串 y （两者长度都为 n ）需满足对于所有 i（在 0 到 n - 1 之间）都有 x[i] >= y[i]（字典序意义下的顺序）。



示例 1：

输入：s1 = "abc", s2 = "xya"
输出：true
解释："ayx" 是 s2="xya" 的一个排列，"abc" 是字符串 s1="abc" 的一个排列，且 "ayx" 可以打破 "abc" 。
示例 2：

输入：s1 = "abe", s2 = "acd"
输出：false
解释：s1="abe" 的所有排列包括："abe"，"aeb"，"bae"，"bea"，"eab" 和 "eba" ，s2="acd" 的所有排列包括："acd"，"adc"，"cad"，"cda"，"dac" 和 "dca"。然而没有任何 s1 的排列可以打破 s2 的排列。也没有 s2 的排列能打破 s1 的排列。
示例 3：

输入：s1 = "leetcodee", s2 = "interview"
输出：true


提示：

s1.length == n
s2.length == n
1 <= n <= 10^5
所有字符串都只包含小写英文字母。

5386. Check If a String Can Break Another String
Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa (in other words s2 can break s1).

A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.



Example 1:

Input: s1 = "abc", s2 = "xya"
Output: true
Explanation: "ayx" is a permutation of s2="xya" which can break to string "abc" which is a permutation of s1="abc".
Example 2:

Input: s1 = "abe", s2 = "acd"
Output: false
Explanation: All permutations for s1="abe" are: "abe", "aeb", "bae", "bea", "eab" and "eba" and all permutation for s2="acd" are: "acd", "adc", "cad", "cda", "dac" and "dca". However, there is not any permutation from s1 which can break some permutation from s2 and vice-versa.
Example 3:

Input: s1 = "leetcodee", s2 = "interview"
Output: true


Constraints:

s1.length == n
s2.length == n
1 <= n <= 10^5
All strings consist of lowercase English letters.
'''


# Sort both strings and then check if one of them can break the other.
class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_list = sorted(list(s1))
        s2_list = sorted(list(s2))
        count = 0
        # print(s1_list, s2_list)
        for i in range(len(s1)):
            c = 0
            if s1_list[i] > s2_list[i]:
                c = 1
            elif s1_list[i] < s2_list[i]:
                c = -1
            # print(count, c)
            if count > 0 and c == -1 or (count < 0 and c == 1):
                return False
            count += c
        return True

#             s1, s2 = sorted(list(s1)), sorted(list(s2))
#         check = zip(*((a >= b, a <= b) for a, b in zip(s1, s2)))
#         return any(map(all, check))

if __name__ == '__main__':
    demo = Solution()
    cases = [("abe", "acd"), ("leetcodee", "interview"), ("abc", "xya")]
    for s1, s2 in cases:
        res = demo.checkIfCanBreak(s1, s2)
        print(res)