'''
 Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''


class Solution(object):
    intRemainder = 0
    intDivisor = 0
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        intQuotient = 1
        if (divisor==dividend):
            intRemainder = 0
            return 1
        elif (dividend < divisor):
            intRemainder = dividend
            return 0
        divisor = divisor << 1
        print ('divisor',divisor)
        intQuotient = intQuotient << 1
        print ('intQuotient',intQuotient)
        while (divisor <= dividend):
            divisor = divisor << 1
            print ('divisor',divisor)
            intQuotient = intQuotient << 1
            print ('intQuotient',intQuotient)
        intQuotient = intQuotient + self.divide(dividend - divisor, self.intDivisor)
        intQuotient = intQuotient >> 1
        rtype = intQuotient
        print (rtype)
        return rtype

if __name__ == '__main__':
    num1 = input ("enter the numerator: ")
    num2 = input ("enter the denominator: ")
    result = Solution().divide(int(num1), int(num2))
print (result)
