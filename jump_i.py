class Solution:
    def canJump(self, nums: list[int]) -> bool:
        que = {}
        def helper(index):
            if index in que:
                return que[index]
            if index >= len(nums):
                que[index] = False
                return False
            # if index == len(nums)-1:
            #     return True
            max_step = nums[index]
            if len(nums) - 1 <= index + max_step:
                que[index] = True
                return True
            for i in range(1, max_step+1):
                if helper(index + i):
                    que[index] = True
                    que[index+i] = True
                    return True
            que[index] = False
            return False
        return helper(0)