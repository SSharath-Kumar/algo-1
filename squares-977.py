# Given an array, return the squares sorted in ascending order

# Input
nums = [-4, -1, 0, 3, 10]

# Initial attempt - 5/15/22
output = []
for num in nums:
    output.append(num * num)

output.sort()
print(output)
# --------------------------
