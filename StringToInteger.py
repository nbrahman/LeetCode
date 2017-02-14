'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.

spoilers alert... click to show requirements for atoi.
'''

import sys
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        rtype = 0
        str = str.lstrip(' ').rstrip(' ')
            #if (int(str)):
        i = 0
        strNew = ""
        if ((len(str)>0) or (str.isalnum()==True)):
            if (str[i]=="-") or (str[i]=="+"):
                i = 1
                strNew = str[0]
            while (i<len(str)):
                print ('str[i]',str[i])
                if (str[i].isnumeric()):
                    print ('inside 2')
                    strNew += str[i]
                    print ('strNew', strNew)
                    i += 1
                else:
                    i = len (str)
            i = len (strNew)-1
            print ('i', i, 'strNew', strNew)
            cnt = 0
            while (i>=0):
                print ('inside loop')
                if (strNew[i].isdigit()):
                    print ('Inside if','cnt',cnt)
                    print ('int(str[i])',int(strNew[i]),'pow(10, cnt)',pow(10, cnt),'int(str[i]) * pow(10, cnt)',int(strNew[i]) * pow(10, cnt))
                    temp = int(strNew[i]) * pow (10, cnt)
                    print ('temp', temp)
                    if (strNew[0]=="-"):
                        temp *= -1
                    print ('temp',temp)
                    rtype += temp
                print ('rtype',rtype)
                i -= 1
                cnt += 1
        if rtype > 2147483647:
            rtype = 2147483647
        elif rtype < -2147483648:
            rtype = -2147483648
        return rtype

if __name__ == '__main__':
    num1 = input ("enter the string for atoi: ")
    num2 = "9"
    result = Solution().myAtoi(num1)
print (result)