class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 1
        end = 2 if int(num/2)<= 1 else int(num/2)
        output = False
        while (end - start>= 1 and end>0 and start>0):
            if start**2 == num or end**2 == num:
                output = True
                print output
                break
            term1 = len(str(num-start**2))
            term2 = len(str(end**2-num))
            if int(term1/2) <= 2:
                start +=  1
            else:
                start += 10**(int(term1/2)-2)
            if int(term2/2) <= 2:
                end -=  1
            else:
                end -= 10**(int(term2/2)-2)
            print 'term',int(term2/2), int(term1/2)
            print 'start-end',start, end
        return output
            
