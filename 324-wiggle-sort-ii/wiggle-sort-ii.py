class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)

        half = (n+1) //2
        small = nums[:half][::-1]   #reverse smaller half
        large = nums[half:][::-1]   #reverse larger half

        i=j=0

        for k in range(n):
            if k%2 == 0:
                nums[k] = small[i]
                i+=1
            else:
                nums[k]= large[j]
                j+=1

