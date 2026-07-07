nums = [5, 8, 12, 7, 2]
lar=nums[0]
for num in nums:
    if num%2==0:
        if lar<num:
            lar=num
print(lar)