from string import ascii_letters as letters 
def letter_counts(s):
    # 103 is the assci value of lowercase g
    # result[103] returns the number of lowercase g
    # >>> result[103]

    """
        >>> result = letter_counts('GHC Rocks!')
        >>> result[6]
        1
        >>> result[2]
        2
    """
    counts = 26 * [0]

    for ch in s:
        if ch in letters:
            counts[ord(ch.lower()) - ord('a')] += 1
    return counts

in_string = input("Enter a string: ")
counts = letter_counts(in_string)

for index, count in enumerate(counts):
    if count != 0:
        print(f"{chr(ord('a') + index)} {count}")

    #meow = s.lower()
    #counts = 256 * [0]
    #for ch in meow:
    #    counts[ord(ch)] += 1
    #return counts
"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()
"""

