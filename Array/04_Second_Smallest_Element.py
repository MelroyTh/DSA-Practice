nums = [15, 3, 27, 9, 11, 2]
small=nums[0]
sec=None
for num in nums:
    if small>num:
        sec=small
        small=num
    elif sec>small and (sec is None or sec<small):
        sec=num
    
print(sec)