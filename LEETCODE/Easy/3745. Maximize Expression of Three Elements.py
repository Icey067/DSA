class Solution(object):
    def maximizeExpressionOfThree(self, nums):
        
        nums.sort()

        sum = nums[-1] + nums[-2] - nums[0]

        return sum 