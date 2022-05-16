input_list = [1,1,1,3,3,4,3,2,4,2]
# Return True if the list has any repetitions else return False


# Initial idea -
def check_duplicates1(nums):
    for i in range(len(nums)):
        num = nums[i]
        for j in range(i+1, len(nums)):
            if num == nums[j]:
                return True
    return False


# Using sets
def check_duplicates2(nums):
    # Sets do not allow duplicates
    # Converting the list to a set drops the duplicates
    # Compare the length of the set against the length of the list
    # if they match, then no duplicates else there are duplicates
    # We need to return True if there are duplicates and False if no duplicates, hence !=
    return len(set(nums)) != len(nums)


print(check_duplicates1(input_list))
print(check_duplicates2(input_list))
