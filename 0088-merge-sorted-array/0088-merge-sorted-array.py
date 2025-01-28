class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr_1 = m -1
        ptr_2 = n -1


        

        while ptr_1 >=0 and ptr_2 >= 0:
            if nums1[ptr_1]> nums2[ptr_2]:
                nums1[ptr_1+ptr_2+1] = nums1[ptr_1]
                ptr_1 = ptr_1 - 1
            else:
                nums1[ptr_1+ptr_2+1] = nums2[ptr_2]
                ptr_2 = ptr_2 - 1
        
        while ptr_2>=0:
            nums1[ptr_1+ptr_2+1] = nums2[ptr_2]
            ptr_2 = ptr_2 - 1

