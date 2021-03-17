nums = [1,0,40,8,0,9,0,22]
j=0
for num in nums:
    if num != 0:
        nums[j] = num
        j+=1

for i in range(j,len(nums)):
    nums[j] = 0
    j+=1
print(nums)

