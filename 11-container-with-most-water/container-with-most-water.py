class Solution(object):
    def maxArea(self, height):
        area = 0
        best = 0
        left = 0
        right = len(height) - 1

        while left < right:
            if height[left] >= height[right]:
                area = height[right] * (right - left)
                right -= 1          
            else:
                area = height[left] * (right - left)
                left += 1           

            if area > best:
                best = area

        return best