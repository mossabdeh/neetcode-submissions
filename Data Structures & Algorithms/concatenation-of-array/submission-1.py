class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # brute force
        # init a empty array with size of 2n
        ans = [0] * (len(nums) * 2)
        # loop through it one pass
        for i in range(len(nums)):
            ans[i] = ans[i + len(nums)] = nums[i]
        return ans
            


        