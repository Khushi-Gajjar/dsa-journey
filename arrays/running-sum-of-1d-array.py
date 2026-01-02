class Solution(object):
    def runningSum(self, nums):
        sum=[]
        curr_sum=0
        for i in nums:
            curr_sum+=i
            sum.append(curr_sum)
        return sum
        
obj=Solution()
print(obj.runningSum([1,2,3,4]))