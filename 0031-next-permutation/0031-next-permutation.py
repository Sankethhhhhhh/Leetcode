class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2

        # Find first decreasing element
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1

            # Find next greater element
            while nums[j] <= nums[i]:
                j -= 1

            # Swap
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the suffix
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1