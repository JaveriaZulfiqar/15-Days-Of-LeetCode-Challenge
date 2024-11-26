class Solution(object):
    def findDisappearedNumbers(self, nums):
        if not nums:  
            return [i for i in range(1, len(nums) + 1)]

        nums.sort()  
        l = 0
        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        
        
        missing_numbers = []
        expected = 1  
        
        for i in range(l + 1):
            while expected < nums[i]:
                missing_numbers.append(expected)
                expected += 1
            expected += 1  
        
        
        while expected <= len(nums):
            missing_numbers.append(expected)
            expected += 1
        
        return missing_numbers
