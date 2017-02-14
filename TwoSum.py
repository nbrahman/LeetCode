class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rtype = []
        temp = []
        for i in range (0, len(nums)):
            try:
                ind = temp.index(target-nums[i])
                rtype.append (ind)
                rtype.append (i)
                rtype.sort()
            except ValueError:
                p=0
            temp.append(nums[i])
        if len(rtype)<=0:
            print ("No matching elements found")
        return rtype