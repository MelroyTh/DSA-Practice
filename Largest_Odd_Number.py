nums = [4, 11, 7, 18, 9]
lar=0
for num in nums:
    if num%2!=0:
        if lar<num:
            lar=num
print(lar)