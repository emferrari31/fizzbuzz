# Step 6: ...And import it 
from lib.fizzbuzz import *



# -- Step 1: Consider a scenario that we want our code to do.

"""
Given a number not divisible by 3 of 5 (e.g., 1)
It returns that number 
"""

# -- Step 2: Write the test: 

def test_given_non_3_5_divisible_returns_number():
    result = fizzbuzz(1)
    assert result == 1

# -- Step 3: Run pytest in the terminal - You'll likely be in the red phase 
# -- i.e., errors returning 

# -- FAILED tests/test_fizzbuzz.py::test_given_non_3_5_divisible_returns_number - 
# -- NameError: name 'fizzbuzz' is not defined
# -- In this case, python is telling us the function we're referring to doesn't exist

# -- Step 6: run pytest again, see the following error: 
# -- FAILED tests/test_fizzbuzz.py::test_given_non_3_5_divisible_returns_number - 
# -- TypeError: fizzbuzz() takes 0 positional arguments but 1 was given

# -- This is down to put having placed num as a parameter, so I'll add that and 
# -- run the test again.

# -- Step 7: Assertion Error - FAILED tests/test_fizzbuzz.py::test_given_non_3_5_divisible_returns_number - assert None == 1
# -- This is saying that our result should be 1 but instead we're getting None 
# -- This is because we're currently using Pass. So let's change that.

# -- Step 9: Repeat! Then eventually you'll refactor 

"""
Given a number divisible by 3
Return "Fizz"
"""

def test_given_3_divisible_return_fizz():
    result = fizzbuzz(3)
    assert result == "Fizz"

"""
Given a number divisible by 5
Return "Buzz" 
"""

def test_given_5_divisible_return_buzz():
    result = fizzbuzz(5)
    assert result == "Buzz"

"""
Given a number divisible by 3 and 5
Return "Fizzbuzz"
"""

def test_given_3_and_5_divisible_return_fizzbuzz():
    result = fizzbuzz(15)
    assert result == "Fizzbuzz"