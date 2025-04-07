class Solution(object):
    def reverse(self, x):
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        
        sign = -1 if x < 0 else 1
        x *= sign  
        
        
        reversed_num = 0
        while x != 0:
            digit = x % 10  
            x //= 10  
            
            if reversed_num > (INT_MAX - digit) // 10:
                return 0  
            reversed_num = reversed_num * 10 + digit
        
        return sign * reversed_num 
