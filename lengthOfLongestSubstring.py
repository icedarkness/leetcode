class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_list = 0
        list_rec = []
        for i in range(len(s)):
            if s[i] not in list_rec:
                list_rec.append(s[i])
            else:
                # print list_rec.index(s[i])
                if list_rec.index(s[i]) != len(list_rec)-1:
                    list_rec = list_rec[list_rec.index(s[i])+1:]
                else:
                    list_rec = []
                list_rec.append(s[i])
            # print list_rec
            if len(list_rec)> max_list:
                max_list = len(list_rec)
        return max_list
