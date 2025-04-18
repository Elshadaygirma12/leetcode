class Solution(object):
    def divide(self, dividend, divisor):
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX  
        

        negative = (dividend < 0) != (divisor < 0)  
        
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            
            temp, multiple = divisor, 1
            
        
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            
            dividend -= temp
            quotient += multiple
        
        
        if negative:
            quotient = -quotient
        
        
        return max(INT_MIN, min(quotient, INT_MAX))
