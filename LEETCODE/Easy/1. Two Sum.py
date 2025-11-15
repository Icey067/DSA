class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}

        for n,num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return (hashmap[complement], n)
            else:
                hashmap[num] = n

        