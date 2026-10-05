def find_average(numbers):
    """
      >>> find_average([5, 10])
      7.5
      >>> find_average([5, 10, 15])
      10.0
      >>> find_average((1, 2, 2, 3))
      2.0
      >>> find_average([19])
      19.0
    """
    total = sum(numbers)
    ave = total / len(numbers)
    print(ave)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

