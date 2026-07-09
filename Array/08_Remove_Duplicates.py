nums = [1, 2, 2, 3, 4, 4, 5]
res=[]
for num in nums:
    if num not in res:
        res.append(num)
print(res)