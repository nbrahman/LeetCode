import math
num = 623315
strNum = str (num)
lstNum=[]
for i in range (0, len(strNum)-1):
    sum = int (strNum[i]) + int (strNum[i+1])
    avg = int(math.ceil(sum/2.0))
    strNew=""
    for j in range (0,i):
        strNew = strNew + strNum[j]
    strNew = strNew + str(avg)
    for j in range (i+2,len(strNum)):
        strNew = strNew + strNum[j]
    intNewNum = int(strNew)
    lstNum.append(intNewNum)
print (max(lstNum))

