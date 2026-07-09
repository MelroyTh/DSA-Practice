nums = [15, 3, 27, 9, 11, 16]

lar = nums[0]
sec = None

for num in nums:
    if num > lar:
        sec = lar
        lar = num
    elif num < lar and (sec is None or num > sec):
        sec = num

print("Largest:", lar)
print("Second Largest:", sec)