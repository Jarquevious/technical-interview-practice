# Given an array of integers, return indices of the two numbers 
# such that they add up to a specific target.
# You may assume that each input would
# have exactly one solution, and you may not
# use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].



# Create an array with arbitrary numbers
arr = [2,15,11,7, 100, 1000, 234, 76, 4, 2, 9]
# Target created
target = 6
# Created a function called two sum to find two sum, give it two parmeter the array and the target
def two_sum(arr, target):
# Inserted a for loop that searches the entire length of the array to find the first number that equals the target
    for i in range(len(arr)-1):
# Inserted a another for loop to find the second number that equals the target
        for j in range(i+1, len(arr)):
# Created a math formula to verify numbers equal the target
            if arr[i] +arr[j] == target:
# Print both arr[i] and arr[j] as an ordered par
                print(arr[i], arr[j])
# Inserted a 'return True' statement if the values equal target
                return True
# Inserted a 'return False' statement if values does not equal target
    return False
# Call the function with parameters for it to run
print(two_sum(arr, target))



