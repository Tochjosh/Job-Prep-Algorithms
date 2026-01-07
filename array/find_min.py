# This is a binary search problem


def find_min(nums: list[int]) -> int:
    """
    Problem:
    Suppose an array of length `n` sorted in ascending order is rotated between
    1 and `n` times.

    For example, the array:
        nums = [0, 1, 2, 4, 5, 6, 7]
    might become:
        [4, 5, 6, 7, 0, 1, 2] if rotated 4 times
        [0, 1, 2, 4, 5, 6, 7] if rotated 7 times

    Note:
        Rotating an array [a0, a1, a2, ..., a(n-1)] one time results in:
        [a(n-1), a0, a1, a2, ..., a(n-2)]

    Given a sorted and rotated array `nums` containing unique elements, return
    the minimum element in the array.

    You must write an algorithm that runs in O(log n) time.

    Examples:
    Example 1:
        Input: nums = [3, 4, 5, 1, 2]
        Output: 1
        Explanation:
            The original array was [1, 2, 3, 4, 5] rotated 3 times.

    Example 2:
        Input: nums = [4, 5, 6, 7, 0, 1, 2]
        Output: 0
        Explanation:
            The original array was [0, 1, 2, 4, 5, 6, 7] rotated 4 times.

    Example 3:
        Input: nums = [11, 13, 15, 17]
        Output: 11
        Explanation:
            The original array was [11, 13, 15, 17] rotated 4 times.

    Constraints:
        n == nums.length
        1 <= n <= 5000
        -5000 <= nums[i] <= 5000
        All elements in nums are unique.
        nums is sorted and rotated between 1 and n times.
    """
    # get the start and end index
    left, right = 0, len(nums) - 1
    min_val = nums[left]

    while left < right:
        mid = (left + right) // 2
        # if the middle value is greater than the rightmost value, it means
        # the initial start point before rotation exist in between the mid and the rightmost value
        if nums[mid] > nums[right]:
            # switch the left index to start from the index of the element after the middle element
             left = mid + 1
        else:
            # switch the right the index to the middle index
            right = mid
        # assume the min val to be the leftmost value
        min_val = nums[left]

    return min_val



print(find_min([4, 5, 6, 7, 0, 1, 2]))
print(find_min([3, 4, 5, 1, 2]))