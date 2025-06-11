# -- Step 4: To fix the error message, we write the function..
# def fizzbuzz():
#     pass 


# def fizzbuzz(num):
#     return num  

# -- Step 8: After returning num, my code now passes the test. Green Phase 

# def fizzbuzz(num):
#     if num % 3 == 0:
#         return "Fizz"
#     else:
#         return num  


# def fizzbuzz(num):
#     if num % 3 == 0:
#         return "Fizz"
#     elif num % 5 == 0:
#         return "Buzz"
#     else:
#         return num  



# def fizzbuzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "Fizzbuzz"
#     if num % 3 == 0:
#         return "Fizz"
#     elif num % 5 == 0:
#         return "Buzz"
#     else:
#         return num  

# -- Now we're in the green phase - All of our tests work and our code functions
# as it should. 

# -- Now we can refactor.

# def fizzbuzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         # This line can be changed to if num % 15 == 0:
#         return "Fizzbuzz"
#     if num % 3 == 0:
#         return "Fizz"
#     elif num % 5 == 0:
#         return "Buzz"
#     else:
#         return num  


def fizzbuzz(num):
    if num % 15 == 0:
        return "Fizzbuzz"
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num  