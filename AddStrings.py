'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        lstRet = []
        i = len(num1)
        j = len(num2)
        intCF = 0
        while ((i>0) or (j>0)):
            intSum = intCF
            if (i>0):
                intSum += int(num1[i-1])
                i -= 1
            if (j>0):
                intSum += int(num2[j-1])
                j -= 1
            intCF = int(intSum / 10)
            intSum = int(intSum % 10)
            lstRet.insert(0,str(intSum))
        if intCF > 0:
            lstRet.insert(0,str(intCF))
        rtype = ''.join(lstRet)
        return rtype

if __name__ == '__main__':
    num1 = "98"
    num2 = "9"
    result = Solution().addStrings(num1, num2)
print (result)