"""
  >>> tricky[4]
  'this'
  >>> tricky[8]
  42
  >>> type(tricky[7])
  <class 'tuple'>
  >>> type(tricky[0])
  <class 'list'>
  >>> len(tricky)
  12
"""

# Put your solutions here:
cat = ["stroke", "meow", "hiss"]
dog = (4, 5, 6)
tricky = [cat, 42, 42, 42, "this", 42, 42, dog, 42, 42, 42, 42]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
