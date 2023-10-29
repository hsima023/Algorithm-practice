#Two Sum
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkDiff = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in checkDiff:
                return (i,checkDiff[nums[i]])
            else:
                checkDiff[diff] = i