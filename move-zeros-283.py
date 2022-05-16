nums = [0,1,0,3,12]

# External Approach
zero_list = []
non_zero_list = []

for num in nums:
    if num == 0:
        zero_list.append(num)
    else:
        non_zero_list.append(num)

# non_zero_list.append(zero_list)
print(non_zero_list + zero_list)

# In-place Approach - SUBMITTED(5/16/22)
for num in nums:
    if num == 0:
        nums.remove(num)
        nums.append(num)
print('INPLACE MOVEMENT:',nums)