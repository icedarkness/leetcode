class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        count_i = 0
        nums = []
        nums1_count = 0
        nums2_count = 0
        while (count_i <=(len(nums1)+len(nums2))/2):
            if nums1_count < len(nums1) and nums2_count < len(nums2):
                if nums1[nums1_count] > nums2[nums2_count]:
                    nums.append(nums2[nums2_count])
                    nums2_count += 1
                else:
                    nums.append(nums1[nums1_count])
                    nums1_count += 1
            elif nums1_count >= len(nums1) and nums2_count < len(nums2):
                nums.append(nums2[nums2_count])
                nums2_count += 1
            elif nums2_count >= len(nums2) and nums1_count < len(nums1):
                nums.append(nums1[nums1_count])
                nums1_count += 1
            count_i += 1 
        if (len(nums1)+len(nums2))%2 != 0:
            return nums[count_i-1]
        else:
            return float(nums[count_i-1]+nums[count_i-2])/2
