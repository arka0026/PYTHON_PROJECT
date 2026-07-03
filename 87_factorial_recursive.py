# Problem 87: Return factorial of a number using recursion (no loops allowed).

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial of", num, "=", factorial(num))
