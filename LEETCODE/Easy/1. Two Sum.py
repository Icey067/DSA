#Two Sum (hashmap)




class Solution(object):
    def twoSum(self, nums, target):
        
        prevMap = {}

        for i, num in enumerate(nums):
            complement = target - num 
            if complement in prevMap:
                return [prevMap[complement], i]

            prevMap[num] = i
        