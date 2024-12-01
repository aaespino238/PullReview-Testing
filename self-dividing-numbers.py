class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def divide(n):
            for i in str(n):
                if i=='0':
                    return False
                if n%(int(i))!=0:
                    return False
            return True
        res=[]
        for i in range(left,right+1):
            if divide(i):
                res.append(i)
        return res
        
        return res