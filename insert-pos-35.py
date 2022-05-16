nums = [1, 3, 5, 6]
# target = 5
target = 2

# Initial submission - 5/15/22
idx = 0
for i in range(len(nums)):
    # print('Index:', i, 'Value:', nums[i])
    if nums[i] == target:
        idx = i
    elif target > nums[i]:
        idx = i+1
print('Output: ', idx)
# ------------------------------
