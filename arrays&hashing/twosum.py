class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # doing a HASHMAP, which involves a (value : key)
        prevMatch = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in prevMatch:
                # how you will get the first index 
                return [prevMatch[diff], index]
            
            prevMatch[value] = index

        return[]
            
            