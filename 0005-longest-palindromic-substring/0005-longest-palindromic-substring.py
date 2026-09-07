class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[1]*(n+1)
        max_word=""
        result=[]
        for i in range(1,n+1):
            for j in range(n-i+1):
                # print(i,j)
                part=s[j:j+i]
                if part==part[::-1]:
                    result.append(part)
    
        m=max(result,key=len)        
        return m