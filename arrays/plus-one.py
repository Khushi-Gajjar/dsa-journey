class Solution(object):
    def plusone(self,digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            else:
                digits[i]=0
        
obj=Solution()
print(obj.plusone([1,2,9,0]))