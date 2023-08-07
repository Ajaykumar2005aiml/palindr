class Solution:
    def isPalindrome(self, x: int) -> bool:
        c=[]
        d=[]
        ci=len(str(x))
        if x>0:
            while ci>0:
                c.append(x%10)
                d.append(x%10)
                x=x//10
                ci=ci-1
            d.reverse()
            if c==d:
                return 'true'
            else:
                return 'false'
        else:
            return 'false'
