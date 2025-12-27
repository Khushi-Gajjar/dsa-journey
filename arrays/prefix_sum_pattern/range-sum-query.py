class NumArray(object):

    def __init__(self, nums):
        self.prefix = [0] * (len(nums))
        self.prefix[0]=nums[0]
        for i in range(1,len(nums)):
           self.prefix[i]=self.prefix[i-1]+nums[i]
           
    def sumRange(self,left,right):
        if left==0:
            return self.prefix[right]
        else:
            return self.prefix[right]-self.prefix[left-1]
        
nums=[2,3,4,5,6,7]
numArray=NumArray(nums)
res=numArray.sumRange(1,5)      
print(res)