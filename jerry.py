
# LEETCODE SOLUTION TO JUMP GAME II

class Solution:
    def jump(self, nums: list[int]) -> int:
        
        dp = [float('inf') for _ in range(len(nums))]
        visited = set()
        dp[-1] = 0

        # for i in range(len(nums)-2,-1,-1):
        #     for j in range(1,nums[i]+1):
        #         if i + j >= len(nums):
        #             break

        #         dp[i] = min(dp[i+j]+1, dp[i])         

        # return dp[0]

        def dfs(i):
            nonlocal dp
            if i == len(nums)-1:
                return 0

            if nums[i] == 0 or dp[i] == -1:
                return float('inf')

            if i in visited:
                return dp[i]

            for j in range(1,nums[i]+1):
                if i+j >= len(nums):
                    break
                dp[i] = min(dfs(i+j), dp[i])
            
            dp[i] += 1
            
            visited.add(i)
            return dp[i]

        dfs(0)
        return dp[0]