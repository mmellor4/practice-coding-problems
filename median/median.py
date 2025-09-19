def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1 += nums2
        nums1.sort()
        print(nums1)

        length = len(nums1)

        if length % 2 == 0:
            # even
            mid1 = nums1[(length // 2) - 1]
            mid2 = nums1[length // 2]
            median = (mid1 + mid2) / 2
        else:
            # odd
            median = nums1[(length // 2)]

        print(median)


findMedianSortedArrays([1,2], [3,4])
