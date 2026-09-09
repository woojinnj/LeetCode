class Solution:
    def countCommas(self, n: int) -> int:
        answer=0
        for i in range(n+1):
            if i<=999:
                continue
            if 1000<=i<=100000:
                answer+=1
        return answer