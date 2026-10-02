class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        s = 0
        for f in range(len(nums)):
            if nums[f] != 0 and nums[s] == 0:
                nums[s], nums[f] = nums[f], nums[s]

            if nums[s] != 0:
                s += 1