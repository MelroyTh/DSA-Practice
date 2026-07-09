nums = [1,2,3, 4, 10]
res=[]
for num in range(1,nums[len(nums)-1]):
    if num not in nums:
        print(num)
