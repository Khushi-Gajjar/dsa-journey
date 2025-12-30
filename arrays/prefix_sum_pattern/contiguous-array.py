class Solution(object):
    def findmaxlen(self,nums):
        prefix_sum=0
        max_len=0
        mp={0:-1}
        for i,value in enumerate(nums):
            if value==0:
                prefix_sum-=1
            else:
                prefix_sum+=1
            if prefix_sum in mp:
                max_len=max(max_len,i-mp[prefix_sum])
            else:
                mp[prefix_sum]=i
        return max_len
obj=Solution()
print(obj.findmaxlen([1,0,1,0,1,1]))

            