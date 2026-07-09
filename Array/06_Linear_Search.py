nums = [12, 5, 9, 18, 7]
target = 12
flag=False
for num in range(len(nums)):
    if nums[num]==target:
        flag=True
        break
       
if flag:
    print("Found at",num,"location")
else:
    print("Not found")