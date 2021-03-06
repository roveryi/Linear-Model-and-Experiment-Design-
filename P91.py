'''
91. Decode Ways
Medium

2816

2929

Add to List

Share
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Accepted
412,741
Submissions
1,672,709
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == "0" or len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
        
        dp = [0]*len(s)
        dp[0] = 1
        if s[1] == "0":
            if int(s[0]) <= 2:
                dp[1] = 1
            else:
                return 0
        else:
            if int(s[0:2]) <= 26:
                dp[1] = 2
            else:
                dp[1] = 1
        
        for i in range(2, len(s)):
            if s[i-1:i+1] == "00":
                return 0
            
            if s[i] == "0":
                if int(s[i-1]) <= 2:
                    dp[i] = dp[i-2]
                else:
                    return 0
            else:
                if int(s[i-1:i+1]) > 26:
                    dp[i] = dp[i-1]
                    
                else:
                    if s[i-1] != "0":
                        dp[i] = dp[i-1] + dp[i-2]
                    else:
                        dp[i] = dp[i-1]
        
        return dp[-1]