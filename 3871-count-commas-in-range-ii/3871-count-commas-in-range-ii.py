class Solution:
    def countCommas(self, n: int) -> int:
        answer=0
        if n<1000:
            return answer
        start=1000
        x=1
        while start*1000<=n:
            answer+=(start*1000-start)*x
            start=start*1000
            x+=1
        if start*1000>n:
            answer+=(n-start+1)*x
            
        return answer