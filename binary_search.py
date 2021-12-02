def binary_search(nums: list[int], target: int) -> int:
    '''
    Return the index of a value in a sorted array. If not found, it returns -1

    Time complexity is log(n)
    '''
    upper_bound = len(nums) - 1
    lower_bound = 0
    while lower_bound <= upper_bound:
        mid_point = (upper_bound + lower_bound) // 2
        if nums[mid_point] == target:
            return mid_point
        elif nums[mid_point] > target:
            upper_bound = mid_point - 1
            mid_point = (upper_bound + lower_bound) // 2
        else:
            lower_bound = mid_point + 1
            mid_point = (upper_bound + lower_bound) // 2
    return -1