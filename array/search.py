


def search(nums: list[int], target: int):
    """
    Problem:
    There is an integer array `nums` sorted in ascending order with distinct
    values.

    Before being passed to your function, `nums` may be left-rotated at an
    unknown index `k` (1 <= k < len(nums)) such that the resulting array is:

        [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]

    For example:
        [0, 1, 2, 4, 5, 6, 7] left-rotated by 3 becomes [4, 5, 6, 7, 0, 1, 2].

    Given the rotated array `nums` and an integer `target`, return the index
    of `target` if it exists in `nums`, or -1 if it does not exist.

    You must write an algorithm with O(log n) runtime complexity.

    Examples:
    Example 1:
        Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
        Output: 4

    Example 2:
        Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
        Output: -1

    Example 3:
        Input: nums = [1], target = 0
        Output: -1

    Constraints:
        1 <= nums.length <= 5000
        -10^4 <= nums[i] <= 10^4
        All values in nums are unique.
        nums is an ascending array that is possibly rotated.
        -10^4 <= target <= 10^4
    """

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # the left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # the right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1



print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([1], 0))
print(search([4, 5, 6, 7, 0, 1, 2], 3))