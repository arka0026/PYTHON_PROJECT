# Problem 87: Return factorial of a number using recursion (no loops allowed).

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial of", num, "=", factorial(num))



# Code Explanation
# pythondef factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# Base case: When n is 0 or 1, the function directly returns 1 (since 0! = 1 and 1! = 1). This is what stops the recursion.

# Recursive case: For any other n, the function calls itself with n - 1, multiplying n by the result of that smaller call.

# Example: How factorial(5) is calculated

# Step 1 — Calls go "down" (building the stack):
# factorial(5) = 5 * factorial(4)
# factorial(4) = 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)
# factorial(1) = 1              ← base case reached, stops here

# Step 2 — Results come back "up" (resolving the stack):

# factorial(1) = 1
# factorial(2) = 2 * 1  = 2
# factorial(3) = 3 * 2  = 6
# factorial(4) = 4 * 6  = 24
# factorial(5) = 5 * 24 = 120
# Final result: factorial(5) = 120

# StepCalculationResultfactorial(1)base case1factorial(2)2 × 12factorial(3)3 × 26factorial(4)4 × 624factorial(5)5 × 24120
# The remaining lines
# pythonnum = int(input("Enter a number: "))

# Takes user input and converts it from a string to an integer.

# pythonprint("Factorial of", num, "=", factorial(num))

# Calls the function and prints the final result — e.g., if num = 5:
# Factorial of 5 = 120
# Note: If the user enters a negative number, the function never reaches the base case (it keeps subtracting 1 forever) and will raise a RecursionError. I can add a check for that if you'd like.