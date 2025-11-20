class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quad(x):
            return a*x*x + b*x + c
        n = len(nums)
        l,r = 0, n-1
        result = [0] * n

        #determine fill direction
        index = n-1 if a>=0 else 0

        while l <= r:
            left = quad(nums[l])
            right = quad(nums[r])

            if a >= 0:
                if left > right:
                    result[index] = left
                    l += 1
                else:
                    result[index] = right
                    r -= 1
                index -= 1
            else:
                if left < right:
                    result[index] = left
                    l += 1
                else:
                    result[index] = right
                    r -= 1
                index += 1
        return result

        