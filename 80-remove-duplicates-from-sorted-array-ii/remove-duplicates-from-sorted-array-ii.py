class Solution(object):
    def removeDuplicates(self, nums):
        cont = 1
        val_ant = float("inf") 
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] and nums[i] != val_ant: 
                cont = 1
            else: 
                cont += 1
                if cont > 2: 
                    val_ant = nums[i]
                    nums[i] = None
        while None in nums:
            nums.remove(None)