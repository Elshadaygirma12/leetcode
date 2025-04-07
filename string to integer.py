class Solution:
    def myAtoi(self, s):
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        
        s = s.lstrip()
        if not s:
            return 0


        sign = 1
        index = 0
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1

        
        num = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + digit
            index += 1

        return sign * num
