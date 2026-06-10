class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax > rightMax:
                r -= 1
                rightMax = max(height[r], rightMax)
                res += rightMax - height[r]
            else:
                l += 1
                leftMax = max(height[l], leftMax)
                res += leftMax - height[l]

        return res
        