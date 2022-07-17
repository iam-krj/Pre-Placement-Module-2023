class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        if len(nums1)<len(nums2):
            
            for i,n in enumerate (nums1):
                if n in nums2:
                    a.append(n)
                    nums2.remove(n)
        else:
            
            for i,n in enumerate(nums2):
                if n in nums1:
                    a.append(n)
                    nums1.remove(n)
                    
        return a            