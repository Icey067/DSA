class Solution(object):
    def search(self, nums, target):

        low = 0
        high = len(nums) - 1

        while low<= high:
            mid = (low + high) / 2
            guess = nums[mid]

            if guess == target:
                return mid
            
            elif guess > target:
                high = mid - 1

            else:
                low = mid + 1

        return -1
        