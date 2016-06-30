class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self,nums):
        numlist= {}
        i=0
        while i<len(nums):
            tempnum=nums[i]
            if tempnum in numlist:
                return True
                break
            tempnumdic={tempnum:tempnum}
            numlist.update(tempnumdic)
            i+=1
        return False
