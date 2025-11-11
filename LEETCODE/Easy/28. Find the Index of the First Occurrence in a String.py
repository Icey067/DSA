#first occurance



class Solution(object):
    def strStr(self, haystack, needle):
        
        a = len(haystack)
        b = len(needle)


        if a<b:
            return -1
        

        for i in range(a-b+1):
            if haystack[i:i+b] == needle:
                return i
                
        return -1