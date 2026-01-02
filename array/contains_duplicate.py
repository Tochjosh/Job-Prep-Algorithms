
def contains_duplicate(nums: list[int]) -> bool:
    """
    Problem:
    Given an integer array `nums`, return True if any value appears at least
    twice in the array, and return False if every element is distinct.

    Examples:
    Example 1:
        Input: nums = [1, 2, 3, 1]
        Output: True
        Explanation:
            The element 1 occurs at indices 0 and 3.

    Example 2:
        Input: nums = [1, 2, 3, 4]
        Output: False
        Explanation:
            All elements are distinct.

    Example 3:
        Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        Output: True

    Constraints:
        1 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
    """
    # seen = defaultdict(int)
    #
    # for num in nums:
    #     seen[num] += 1
    #     print(seen)
    #     if seen[num] > 1:
    #         return True
    # return False

    return len(set(nums)) != len(nums)

print(contains_duplicate([1,2,3,4]))
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))