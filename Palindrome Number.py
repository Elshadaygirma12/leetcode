class Solution:
    def isPalindrome(self, x: int) -> bool:
         if x < 0:
            return False
         else:
            str_x = str(x)
            return str_x == str_x[::-1]
        
        
