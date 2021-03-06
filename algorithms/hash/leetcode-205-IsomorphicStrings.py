
'''
205. 同构字符串
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。

205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # hash_map = {}
        # for i in range(len(s)):
        #     if s[i] not in hash_map.keys() and t[i] not in hash_map.values():
        #         hash_map[s[i]] = t[i]
        #     elif s[i] in hash_map:
        #         if hash_map[s[i]] != t[i]:
        #             return False
        #     elif t[i] in hash_map.values():
        #         return False
        # return True
        s_indexs = []
        t_indexs = []
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            if s[i] in s_map:
                s_indexs.append(s_map[s[i]])
            else:
                s_map[s[i]] = i
                s_indexs.append(i)
            if t[i] in t_map:
                t_indexs.append(t_map[t[i]])
            else:
                t_map[t[i]] = i
                t_indexs.append(i)
            if s_indexs != t_indexs:
                return False
        return True


