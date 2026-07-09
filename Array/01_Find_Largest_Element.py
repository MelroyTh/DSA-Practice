nums = [15, 3, 27, 9, 11]
lar=nums[0]
for num in nums:
    if lar<num:
        lar=num
print(lar)