class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lisst= {}
        for i in nums:
            if i in lisst:
                return True
            lisst[i] = 1
        return False
