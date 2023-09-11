def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: factorial of n is n multiplied by factorial of (n-1)
        return n * factorial(n - 1)

def is_leap_year(year):
    # Check if it's a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage for factorial calculation
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")

# Example usage for leap year determination
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
