'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strNum = str(x)
        intMult = 1
        if (strNum[0]=="-"):
            strFinalNum = strNum[1:len(strNum)]
            intMult = -1
        else:
            strFinalNum = strNum
        strRevNum = strFinalNum[::-1]
        print (strRevNum)
        rtype = 0
        if (int(strRevNum)<=2147483647) and (int(strRevNum)>=-2147483648):
            rtype = intMult * int(strRevNum)
        return rtype

if __name__ == '__main__':
    num1 = input ("enter the string for atoi: ")
    num2 = "9"
    result = Solution().reverse(num1)
print (result)