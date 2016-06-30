#Given an array of integers, every element appears twice except for one. Find that single one
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dic = {}
        for i in nums:
            if i in nums_dic:
                nums_dic[i] = nums_dic[i] + 1
            else:
                nums_dic[i] = 1
        return [k for k, v in nums_dic.iteritems() if v==1][0]
