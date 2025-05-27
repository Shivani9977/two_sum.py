def sum_target(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j]==target:
                return [i,j]
num=[2,7,11,15]
target=9
sum_target(num,target)
