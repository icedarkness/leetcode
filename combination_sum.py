def combinationSum3(k , n, count=0,partial=[], listdict=[],numbers=[1,2,3,4,5,6,7,8,9],self=0):
    if not partial:
        s = 0
    else:
        s = sum(partial)
    if s == n:
        if len(partial) == k:
            listdict.append(partial)
    for i in range(len(numbers)):
        tempnum = numbers[i]
        remaining = numbers[i+1:]
        combinationSum3(k, n,count, partial+[tempnum],listdict,remaining)
    return listdict


# def combinationSum3(k,n):
#     finallist =  combinationSumRec(numbers,3,9)
#     return finallist

test =  combinationSum3(3,7)
print(test)
