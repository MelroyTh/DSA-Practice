nums = [1, 2, 3,1, 4, 5]
first=nums[0]
res=[]
for num in range(1,len(nums)):
        res.append(nums[num])

res.append(first)
print(res)
