class Solution(object):
    def searchRange(self, nums, target):
        def find_start(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def find_end(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        start = find_start(nums, target)
        end = find_end(nums, target)
        

        if start <= end and start < len(nums) and nums[start] == target:
            return [start, end]
        else:
            return [-1, -1]
