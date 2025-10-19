"""
Alfonso Garcia
19 October 2025

Take-Home Assignment Part 1: Functional Programming 

Problem:

Write pure function that removes duplicates from a list/array while
preserving original order of first occurrences

    Requirements:
        -Pure function, same input always gives same output
        -Original input is not modified
        -Functional programming approaches
        -Solution is tested

    Test Cases:
        remove_duplicates([1, 2, 3, 2, 4, 1, 5])  # [1, 2, 3, 4, 5]
        remove_duplicates([1, 1, 1])              # [1]
        remove_duplicates([])                     # []
"""


def remove_duplicates(duplicate_list):
    """
    Method that takes a list of integers that may or may not contain duplicates
    and outputs a duplicate-free list that preserves the order of numbers
    as they occur and does not modify the original input.
    """

    # Maintain dictionary to map specific digit to its number of occurences
    digit_occurences = {
        0: 0,  1: 0, 2: 0,3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0
    }

    duplicate_free_list = []
    
    for digit in duplicate_list:
        # Only add digit if it has not yet been encountered (not duplicate)
        if digit_occurences[digit] == 0:
            duplicate_free_list.append(digit)
            digit_occurences[digit] += 1
    return duplicate_free_list 

