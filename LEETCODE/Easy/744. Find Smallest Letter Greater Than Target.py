class Solution(object):
    def nextGreatestLetter(self, letters, target):
        low = 0 
        high = len(letters) - 1

        while low<=high:
            mid = (low + high) / 2

            if letters[mid]>target:
                high = mid -1 

            else:
                low = mid+1
                
           #wrap-around cases:

        if low == len(letters):
            return letters[0]
        else:
            return letters[low]
        