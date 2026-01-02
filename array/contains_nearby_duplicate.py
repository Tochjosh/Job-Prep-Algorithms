
def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    """
    Problem:
    Given an integer array `nums` and an integer `k`, return True if there are
    two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]`
    and `abs(i - j) <= k`.

    Examples:
    Example 1:
        Input: nums = [1, 2, 3, 1], k = 3
        Output: True

    Example 2:
        Input: nums = [1, 0, 1, 1], k = 1
        Output: True

    Example 3:
        Input: nums = [1, 2, 3, 1, 2, 3], k = 2
        Output: False

    Constraints:
        1 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
        0 <= k <= 10^5
    """

    seen = {}

    for ind, num in enumerate(nums):
        if num in seen and abs(seen[num] - ind) <= k:
            return True
        seen[num] = ind
    return False

print(contains_nearby_duplicate([1, 2, 3, 1], 3))
print(contains_nearby_duplicate([1, 0, 1, 1], 1))
print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))