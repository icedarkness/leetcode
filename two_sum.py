class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        y = 'a'
        output = [0,0]
        for j,element1 in enumerate(nums):
            temp_rec = [i for i, element2 in enumerate(nums) if element2 == target - element1 and i != j]
            # print temp_rec
            if  len(temp_rec)> 0:
                output = [j,temp_rec[0]]
                break
        return output
