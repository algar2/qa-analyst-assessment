# QA Analyst Technical Assessment

**Candidate:** Alfonso Garcia

**Language Used:** Python

**Completion Date:** 19 October 2025

## Part 1: Functional Programming

**Time Spent** ~30 Minutes

**Approach**: To remove duplicates from a given list of integers, I utilize a dictionary that maps digits to their current number of occurences. This way, I know that when iterating through a list containing duplicates, if the current digit's dict value is non-zero, it is a duplicate and therefore should not be appended to the duplicate free list. By iterating over the input list and performing a simultaneous look-up, I maintain the order of digits as they occur and remove duplicates as well.

## Part 2: API Testing

**Time Spent** ~30 Minutes

**Approach**: I wrote simple tests to cover the three cases of a GET request, POST request, and Error handling. For the GET request, I used the sample endpoint and because we need to verify that the user exists, I assert that the response is successful and that the required id, name, and email fields are all present in the response. Similarly for a POST request, I create a sample payload containing required fields for a post and verify that the post request was successful with the proper status code and that
the generated response contains the required fields. Finally to test 404 responses, I just fetch user 999 and validate it does not exist through checking the status code.

## How to Run

### Part 1

Within the Part 1 working directory terminal, install pytest if not already downloaded with `pip install pytest`

After downloading, run `pytest test_solution.py`

### Part 2

Within the terminal, install requests if not already installed `pip install requests` and if not already installed, run `pip install pytest`

Then in the terminal, run `pytest solution.py`.

To see the response following a successful validation of the 404 code, execute pytest with the -s flag, `pytest -s solution.py`
