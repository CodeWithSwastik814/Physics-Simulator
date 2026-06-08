''' import math
import sympy as sp

def parse_and_differentiate():
    x, y, z, t = sp.symbols('x y z t')
    available_symbols = {'x': x, 'y': y, 'z': z, 't': t}

    print("=" * 50)
    print("   Symbolic Derivative Calculator (SymPy)")
    print("=" * 50)
    print("Supported functions: sin, cos, tan, exp, log, sqrt")
    print("Supported variables: x, y, z, t")
    print("Example inputs:")
    print("  x**3 + 2*x**2 - 5*x + 1")
    print("  sin(x) * exp(x)")
    print("  log(x**2 + 1)")
    print("  x**2 * y + y**3   (multivariable)")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  [1] Compute derivative")
        print("  [2] Compute nth-order derivative")
        print("  [3] Compute partial derivative")
        print("  [4] Evaluate derivative at a point")
        print("  [q] Quit")

        choice = input("\nChoose an option: ").strip().lower()

        if choice == 'q':
            print("Goodbye!")
            break

        elif choice == '1':
            expr_str = input("Enter equation f(x): ").strip()
            var_str = input("Differentiate with respect to (default x): ").strip() or 'x'
            try:
                expr = sp.sympify(expr_str, locals=available_symbols)
                var = available_symbols.get(var_str, sp.Symbol(var_str))
                derivative = sp.diff(expr, var)
                print(f"\n  f({var_str})  = {expr}")
                print(f"  f'({var_str}) = {derivative}")
                print(f"  Simplified  = {sp.simplify(derivative)}")
            except Exception as e:
                print(f"  Error: {e}")

        elif choice == '2':
            expr_str = input("Enter equation f(x): ").strip()
            var_str = input("Differentiate with respect to (default x): ").strip() or 'x'
            n_str = input("Order of derivative (e.g. 2 for second derivative): ").strip()
            try:
                expr = sp.sympify(expr_str, locals=available_symbols)
                var = available_symbols.get(var_str, sp.Symbol(var_str))
                n = int(n_str)
                derivative = sp.diff(expr, var, n)
                print(f"\n  f({var_str})           = {expr}")
                print(f"  d^{n}/d{var_str}^{n} f({var_str}) = {derivative}")
                print(f"  Simplified       = {sp.simplify(derivative)}")
            except Exception as e:
                print(f"  Error: {e}")

        elif choice == '3':
            expr_str = input("Enter multivariable equation (e.g. x**2*y + y**3): ").strip()
            var_str = input("Partial derivative with respect to: ").strip()
            try:
                expr = sp.sympify(expr_str, locals=available_symbols)
                var = available_symbols.get(var_str, sp.Symbol(var_str))
                partial = sp.diff(expr, var)
                print(f"\n  f        = {expr}")
                print(f"  ∂f/∂{var_str}  = {partial}")
                print(f"  Simplified = {sp.simplify(partial)}")
            except Exception as e:
                print(f"  Error: {e}")

        elif choice == '4':
            expr_str = input("Enter equation f(x): ").strip()
            var_str = input("Variable (default x): ").strip() or 'x' 
            point_str = input("Evaluate derivative at point: ").strip()
            try:
                expr = sp.sympify(expr_str, locals=available_symbols)
                var = available_symbols.get(var_str, sp.Symbol(var_str))
                derivative = sp.diff(expr, var)
                point = float(point_str)
                value = derivative.subs(var, point)
                print(f"\n  f({var_str})        = {expr}")
                print(f"  f'({var_str})       = {derivative}")
                print(f"  f'({point})     = {sp.simplify(value)}")
                print(f"  Numerical   ≈ {float(value):.6f}")
            except Exception as e:
                print(f"  Error: {e}")

        else:
            print("  Invalid option. Choose 1–4 or q.")


if __name__ == "__main__":
    try: 
        import sympy
    except ImportError:
        print("SymPy not found. Installing...")
        import subprocess, sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "sympy"])
    
    parse_and_differentiate() '''


''' from sympy import *
import numpy as np

 = symbols('x')
x = Symbol('x')
y = 2*x**2 + 1*x + 65
yprime = y.diff(x)
print(yprime)'''



from sympy import *

x = symbols('x')

print("Symbolic Differentiation Tool")
print("Supported: x**2, sin(x), exp(x), log(x), sqrt(x), etc.\n")

expr_input = input("Enter y = ").strip()

try:
    y = sympify(expr_input)
    dy = diff(y, x)
    print(f"\nf(x)  = {y}")
    print(f"f′(x) = {dy}")
except Exception as e:
    print(f"Error: {e}")
    

