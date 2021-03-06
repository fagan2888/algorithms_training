'''
1461. 检查一个字符串是否包含所有长度为 K 的二进制子串
给你一个二进制字符串 s 和一个整数 k 。

如果所有长度为 k 的二进制字符串都是 s 的子串，请返回 True ，否则请返回 False 。



示例 1：

输入：s = "00110110", k = 2
输出：true
解释：长度为 2 的二进制串包括 "00"，"01"，"10" 和 "11"。它们分别是 s 中下标为 0，1，3，2 开始的长度为 2 的子串。
示例 2：

输入：s = "00110", k = 2
输出：true
示例 3：

输入：s = "0110", k = 1
输出：true
解释：长度为 1 的二进制串包括 "0" 和 "1"，显然它们都是 s 的子串。
示例 4：

输入：s = "0110", k = 2
输出：false
解释：长度为 2 的二进制串 "00" 没有出现在 s 中。
示例 5：

输入：s = "0000000001011100", k = 4
输出：false


提示：

1 <= s.length <= 5 * 10^5
s 中只含 0 和 1 。
1 <= k <= 20

1461. Check If a String Contains All Binary Codes of Size K
Given a binary string s and an integer k.

Return True if all binary codes of length k is a substring of s. Otherwise, return False.



Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.
Example 2:

Input: s = "00110", k = 2
Output: true
Example 3:

Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.
Example 4:

Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and doesn't exist in the array.
Example 5:

Input: s = "0000000001011100", k = 4
Output: false


Constraints:

1 <= s.length <= 5 * 10^5
s consists of 0's and 1's only.
1 <= k <= 20
'''





class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        # for i in range(2**k):
        #     # print(bin(i)[2:].ljust(k, "0"))
        #     ch = bin(i)[2:].ljust(k, "0")
        #     if ch not in s:
        #         return False
        # return True
        n = 2**k
        all_sub_s = set()
        for i in range(len(s)-k+1):
            all_sub_s.add(s[i:i+k])

        # print(all_sub_s)

        return len(all_sub_s) == n


# golang solutions

'''
func hasAllCodes(s string, k int) bool {
	maxVal := int(math.Pow(2, float64(k)))

	for i := 0; i < maxVal; i++ {
		binaryVal := strconv.FormatInt(int64(i), 2)
		fmt.Println(binaryVal)
		// strings.
		if len(binaryVal) < k {
			binaryVal = strings.Repeat("0", k-len(binaryVal)) + binaryVal
		}
		fmt.Println(binaryVal)
		fmt.Println(fmt.Sprintf("%b", i))
		if !strings.Contains(s, binaryVal) {
			return false
		}
	}

	return true
}
'''

# tips

# We need only to check all sub-strings of length k.

# The number of distinct sub-strings should be exactly 2^k.