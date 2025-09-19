class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret_val = []
        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(i+1,len(nums)):
                num2 = nums[j]
                if num1 + num2 == target:
                    ret_val = [i, j]

        return ret_val

        
