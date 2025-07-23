value = int(input("Enter a number: "))

def factorial(n):
    factorial_value = 1
    while n>=1 :

        factorial_value *= n
        n = n - 1
    return factorial_value
result = factorial(value)
print("Factorial of",value," is:",result)