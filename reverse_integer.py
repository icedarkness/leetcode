class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = []
        if x < 0:
            s = str(x)[1:]
            sign = -1
        else:
            s = str(x)
            sign = 1
        for i in range(len(s)):
            reverse.append(s[len(s)-i-1])
        result = sign*int(''.join(reverse))
        if x < -2**31 or x> 2**31-1 or result < -2**31 or result > 2**31-1:
            result = 0
        return result
