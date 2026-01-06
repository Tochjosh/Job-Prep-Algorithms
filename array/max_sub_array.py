

def max_sub_array(nums: list[int]) -> int:
    """
    Problem:
    Given an integer array `nums`, find the contiguous subarray with the
    largest sum and return its sum.

    Examples:
    Example 1:
        Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        Output: 6
        Explanation:
            The subarray [4, -1, 2, 1] has the largest sum of 6.

    Example 2:
        Input: nums = [1]
        Output: 1
        Explanation:
            The subarray [1] has the largest sum of 1.

    Example 3:
        Input: nums = [5, 4, -1, 7, 8]
        Output: 23
        Explanation:
            The subarray [5, 4, -1, 7, 8] has the largest sum of 23.

    Constraints:
        1 <= nums.length <= 10^5
        -10^4 <= nums[i] <= 10^4

    Follow-up:
        If you have figured out the O(n) solution, try coding another
        solution using the divide and conquer approach.
    """
    max_so_far = nums[0]
    cur_sum = 0

    for num in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += num
        if cur_sum > max_so_far:
            max_so_far = cur_sum

    return max_so_far


print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sub_array([1]))
print(max_sub_array([5, 4, -1, 7, 8]))

