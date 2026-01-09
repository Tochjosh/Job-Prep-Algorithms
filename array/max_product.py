# This is a dynamic programming problem


def max_product(nums: list[int]) -> int:
    """
    Problem:
    Given an integer array `nums`, find the contiguous subarray that has the
    largest product and return the product.

    The test cases are generated so that the answer will fit in a 32-bit
    integer.

    Note:
        The product of an array with a single element is the value of that
        element.

    Examples:
    Example 1:
        Input: nums = [2, 3, -2, 4]
        Output: 6
        Explanation:
            The subarray [2, 3] has the largest product of 6.

    Example 2:
        Input: nums = [-2, 0, -1]
        Output: 0
        Explanation:
            The result cannot be 2 because [-2, -1] is not a contiguous
            subarray.

    Constraints:
        1 <= nums.length <= 10^5
        -10 <= nums[i] <= 10
        The answer is guaranteed to fit in a 32-bit integer.
    """

    max_prod = min_prod = result = nums[0]

    for num in nums[1:]:
        # When the num is negative, the best product becomes the worst, and the worst becomes the best,
        # so we swap them before multiplying.
        if num < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)

        result = max(result, max_prod)

    return result



print(max_product([2, 3, -2, 4]))
print(max_product([-2, 0, -1]))