class Solution(object):
    def movezero(self,nums):
        left=0
        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
        return nums
                
obj=Solution()
print(obj.movezero([0,0,1,2,3,0,0,4,0,5]))