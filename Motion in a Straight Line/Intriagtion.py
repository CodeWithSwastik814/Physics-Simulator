from sympy import *

x = symbols('x')

print("Symbolic Integration Tool")
print("Supported: x**2, sin(x), exp(x), log(x), sqrt(x), etc.\n")

expr_input = input("Enter f(x) = ").strip()

try:
    y = sympify(expr_input)
    integral = integrate(y, x)
    print(f"\nf(x)  = {y}")
    print(f"∫f(x) = {integral} + C")
except Exception as e:
    print(f"Error: {e}")