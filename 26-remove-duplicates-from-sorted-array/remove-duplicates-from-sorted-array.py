class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        l = 0
        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        
        for i in range(l + 1, len(nums)):
            nums[i] = '_'
        
        return l + 1