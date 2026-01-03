

def product_except_self(nums: list[int]) -> list[int]:
    """
    Problem:
    Given an integer array `nums`, return an array `answer` such that
    `answer[i]` is equal to the product of all the elements of `nums`
    except `nums[i]`.

    The product of any prefix or suffix of `nums` is guaranteed to fit
    in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and does not use
    the division operation.

    Examples:
    Example 1:
        Input: nums = [1, 2, 3, 4]
        Output: [24, 12, 8, 6]

    Example 2:
        Input: nums = [-1, 1, 0, -3, 3]
        Output: [0, 0, 9, 0, 0]

    Constraints:
        2 <= nums.length <= 10^5
        -30 <= nums[i] <= 30
        The input is generated such that answer[i] is guaranteed to fit
        in a 32-bit integer.
    """
    length = len(nums)
    result = [1] * length
    pre_fix = 1
    post_fix = 1

    for i in range(length):
        result[i] = post_fix
        post_fix *= nums[i]

    for i in range(length - 1, -1, -1):
        result[i] *= pre_fix
        pre_fix *= nums[i]

    return result

print(product_except_self([1, 2, 3, 4]))
print(product_except_self([-1, 1, 0, -3, 3]))


