def largestDivisibleSubset(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    list_rec = {-1: set()}
    count_i = 0
    nums = sorted(nums)
    max_list = []
    if len(nums) > 0:
        max_list = [nums[0]]
        nums_temp = sorted(nums)
        for i in nums_temp:
            nums2 = sorted([x for x in nums if x > i and x % i == 0])
            nums_temp = [x for x in nums_temp if x not in nums2]
            if not i in list_rec:
                list_rec[i] = [i] + largestDivisibleSubset(self, nums2)
            else:
                list_rec[i].append([i] + largestDivisibleSubset(self,nums2))
    return list(max(list_rec.values(),key = len))
