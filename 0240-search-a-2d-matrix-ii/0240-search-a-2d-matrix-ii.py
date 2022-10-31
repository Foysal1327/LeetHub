class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for item in matrix:
            if item[0] <= target:
                # print(item[0])
                for element in item:
                    # print(element)
                    if element == target:
                        return True
        return False