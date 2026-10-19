def keep_only_evens(nums):
    """
      >>> some_nums = [3, 8, 5, 4, 12, 7, 2]
      >>> keep_only_evens(some_nums)
      >>> some_nums
      [8, 4, 12, 2]
    """
    for num in nums:
        if num % 2 != 0:
            nums.remove(num)
    return nums


if __name__ == '__main__':
    import doctest
    doctest.testmod()
