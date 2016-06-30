class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        if s.strip() != "" and len(s.strip(' ').split(' ')) != 1:
            a = (' '.join(s.split())).split()
            print len(a)
            b = ['a']*len(a)
            for i in range(len(a)):
                print b[len(a)-i-1]
                print a[i]
                b[len(a)-i-1] = a[i]
            return ' '.join(b)
        else: 
            return ' '.join(s.split())
