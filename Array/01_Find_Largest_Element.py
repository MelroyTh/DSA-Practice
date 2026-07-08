nums = [4, 8, 2, 10, 5]
lar=nums[0]
for num in nums:
    if lar<num:
        lar=num
print(lar)