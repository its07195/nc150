class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashm=set()
        for n in nums:
            if n in hashm:
                return True
            hashm.add(n)
        return False
#Time O(n) Space O(n)
