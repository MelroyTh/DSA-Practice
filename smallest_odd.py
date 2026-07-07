nums = [8, 14, 17, 19]
smallest=None
for num in nums:
    if num%2!=0:
        if smallest is None :
            smallest=num
        elif num < smallest:
            smallest=num
print(smallest)
        