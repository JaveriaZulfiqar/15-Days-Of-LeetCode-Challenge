class Solution(object):
    def isPalindrome(self, s):
        lowercase = s.lower()
        alphanumeric = ''.join(char for char in lowercase if char in 'abcdefghijklmnopqrstuvwxyz0123456789')
        
        l, r = 0, len(alphanumeric) - 1
        
        while l < r:
            if alphanumeric[l] != alphanumeric[r]:
                return False
            
            l += 1
            r -= 1
        
        return True