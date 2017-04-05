class Solution():
    def countSort(self, nums):
        freq = [0] * (max(nums) + 1)
        for value in nums:
            freq[value] += 1

        writePos = 0
        for value, count in enumerate(freq):
            for i in range(count):
                nums[writePos] = value
                writePos += 1

        return nums

s = Solution()
a = [12, 34, 12, 3, 45, 65, 45]
print(s.countSort(a))
