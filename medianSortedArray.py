def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    mid_element = (len(nums1) + len(nums2)) / 2.0
    if mid_element == 0:
        return 0
    newlist = []
    for i in range(0, int(mid_element) + 1):
        if not nums1:
            newlist.append(nums2.pop(0))
        elif not nums2:
            newlist.append(nums1.pop(0))
        else:
            if nums1[0] < nums2[0]:
                newlist.append(nums1.pop(0))
            else:
                newlist.append(nums2.pop(0))

    if mid_element != round(mid_element):
        return newlist[-1]
    return (newlist[-1] + newlist[-2]) / 2.0


def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        return median(B, A)
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    while imin <= imax:
        i = int((imin + imax) / 2)
        j = int(half_len - i)
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0:
                max_of_left = B[j-1]
            elif j == 0:
                max_of_left = A[i-1]
            else:
                max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = B[j]
            elif j == n:
                min_of_right = A[i]
            else:
                min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0


print(findMedianSortedArrays([1, 3], [2]))
print(median([1, 3], [2]))
