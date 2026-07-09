nums = [15, 3, 27, 9, 11]
small=None

for num in nums:
    if small is None:
        small=num
    elif small>num:
        small=num
print(small)