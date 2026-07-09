nums = [0, 1, 0, 3, 12]
res=[]

for num in nums:
    if num!=0:
        res.append(num)
dif=len(nums)-len(res)
for i in range(dif):
    res.append(0)
print(res)
    

    