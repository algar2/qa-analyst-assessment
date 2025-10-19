"""
This test file is to be used with pytest to automate testing the 
remove_duplicates function 
"""
from solution import remove_duplicates

def test_first_case():
    """
    Testing method on input of [1, 2, 3, 2, 4, 1, 5]
    Expected Output: [1, 2, 3, 4, 5]
    """
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_second_case():
    """
    Testing method on input of [1, 1, 1]
    Expected Output: [1]
    """
    assert remove_duplicates([1, 1, 1]) == [1]

def test_third_case():
    """
    Testing method on input of []
    Expected Output: []
    """
    assert remove_duplicates([]) == []