'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''


# Solution 1: My solution with a pre-made set of the possible solutions.

def twoSum(nums, target):
    sol_set = set(map(lambda x: target-x, nums))
    for num in nums:
        if num in sol_set:
            # Only returns the two indices if they are different by checking the first and last indices of the solutions
            if nums.index(num) != len(nums) - nums[-1::-1].index(target - num) - 1:
                return [nums.index(num), len(nums) - nums[-1::-1].index(target - num) - 1]


# Solution 2: Solution where user creates the set as they iterate through the list.

def twoSum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]


print(twoSum([1, 2, 3, 4], 4))
print(twoSum2([1, 2, 3, 4], 4))
