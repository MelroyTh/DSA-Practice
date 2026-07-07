nums = [4, 8, 2, 10, 5]
target =int(input("Enter the target value : "))
flag=False
for num in nums:
    if num==target:
        flag=True
        break
    
if flag:
     print("target found")
else:
     print("target not found")