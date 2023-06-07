class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        i = n - 2
        br = -1
        while i >= 0:
            if nums[i] < nums[i + 1]:
                br = i
                break
            i -= 1

        i = n - 1
        if br == -1:
            reverse(nums, 0, n - 1)
            return

        while i > br:
            if nums[i] > nums[br]:
                nums[i], nums[br] = nums[br], nums[i]
                break
            i -= 1

        reverse(nums, br + 1, n - 1)
