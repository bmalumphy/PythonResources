class Solution(object):
    class Solution(object):
    
        def longestPalindrome(self, s):
            def expandAroundCenter(s, left, right):
                L = left
                R = right
                while(L >= 0 and R < len(s) and s[L] == s[R]):
                    L-=1
                    R+=1
                return R-L-1
            
            if(s == None or len(s) < 1):
                return ""
            start, end = 0, 0

            for i in range(0, len(s)):
                len1 = expandAroundCenter(s, i, i)
                len2 = expandAroundCenter(s,i, i+1)
                length = max(len1, len2)
                if(length > end-start):
                    start = i-(length-1)/2
                    end = i + length/2
            return s[start:end+1]
    
        
            
            
        