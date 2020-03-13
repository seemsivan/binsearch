import typing as tp
from bisect import bisect_left

def find_value(nums, value):
    mid = len(nums) // 2
    left = 0
    right = len(nums) - 1
    while left <= right:
        if value == nums[mid]:
            return True
        elif value > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2
    return False