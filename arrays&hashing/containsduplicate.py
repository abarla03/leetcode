class ContainsDuplicates(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        previous_values = set()
        increment = 0

        for x in nums:
            if x in previous_values:
                increment += 1
            
            previous_values.add(x)

        if increment > 0:
            return True
        else:
            return False
        

    @classmethod
    def test_method(cls, nums):
        contains_duplicates = cls()  # Create an instance of the class
        result = contains_duplicates.containsDuplicate(nums)
        print("Contains duplicates:", result)


ContainsDuplicates.test_method([1, 2, 1, 5])
