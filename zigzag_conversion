class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        sdict = {0:[]}
        if numRows == 1:
            sdict[1] = [s]
        else:
            for i in range(len(s)):
                if numRows-1-abs(numRows-1-i % (2*numRows-2)) in sdict.keys():
                    sdict[numRows-1-abs(numRows-1-i % (2*numRows-2))].append(s[i])
                else:
                    sdict[numRows-1-abs(numRows-1-i % (2*numRows-2))] = [s[i]]
        return ''.join([''.join(v) for k,v in sdict.iteritems()])
