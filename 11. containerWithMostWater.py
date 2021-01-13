'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
'''

def maxArea(height):

    def area(height, start, end):
        return height * (end - start)

    true_max = 0

    i, j = 0, len(height) - 1

    while i != j:
        true_max = max(true_max, area(min(height[i], height[j]), i, j))
        if height[i] < height[j]:
            i = i + 1
        else:
            j = j - 1

    return true_max
    
print(maxArea([1,8,6,2,5,4,8,3,7]))