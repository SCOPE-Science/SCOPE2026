"""Exact genus-four cyclic-trigonal Cartier and discriminant identities.
Requires SymPy >= 1.12; run: python verify_cartier.py.
"""
from math import factorial
import sympy as sp

x, a, b, c = sp.symbols('x a b c')
p = 7
f = x**5 + a*x**2 + b*x + c

def red(z):
    return sp.Poly(sp.expand(z), a, b, c, modulus=p).as_expr()

# Independent multinomial enumerator, not an expansion routine.
def multinomial_coefficient(power, degree):
    ans = 0
    for n5 in range(power+1):
        for n2 in range(power-n5+1):
            for n1 in range(power-n5-n2+1):
                n0 = power-n5-n2-n1
                if 5*n5 + 2*n2 + n1 == degree:
                    ans += factorial(power)//(
                        factorial(n5)*factorial(n2)*factorial(n1)*factorial(n0)
                    ) * a**n2 * b**n1 * c**n0
    return red(ans)

def expanded_coefficient(power, degree):
    return red(sp.Poly(sp.expand(f**power), x).nth(degree))

for exponent in (2, 4):
    for target in range(5*exponent + 1):
        assert multinomial_coefficient(exponent, target) == expanded_coefficient(exponent, target)

# Bases: omega0=dx/y; omega_(i+1)=x^i dx/y^2, i=0,1,2.
scalar = multinomial_coefficient(2, 6)
B = sp.Matrix(3, 3, lambda row, col:
              multinomial_coefficient(4, 7*(row+1)-1-col))
expected = sp.Matrix([
    [-3*a**3*c-a**2*b**2-2*b*c**2,
     -2*a**2*b*c-3*a*b**3-3*c**3,
     -a**2*c**2-2*a*b**2*c+b**4],
    [-2*a*b, -2*a*c-b**2, -3*a**3-2*b*c],
    [1, 0, 0],
])
assert scalar == red(2*b)
assert all(red(B[i, j]-expected[i, j]) == 0 for i in range(3) for j in range(3))

# Monic degree-five polynomial: discriminant = resultant(f,f') (sign +).
disc = red(sp.discriminant(f, x))
expected_disc = (3*a**5*c+a**4*b**2+3*a**2*b*c**2
                 +3*a*b**3*c-3*b**5+3*c**4)
assert red(disc-expected_disc) == 0
assert red(B.det()-2*b*disc) == 0
assert red(scalar*B.det()-4*b**2*disc) == 0

# Specialize to b=0, c=1. The lower 3x3 block has rank 2:
# determinant zero, while rows 0,2 columns 0,1 have minor +3.
B0 = B.subs({b:0,c:1})
assert red(B0.det()) == 0
assert red(B0[0,0]*B0[2,1]-B0[0,1]*B0[2,0]-3) == 0
print('CARTIER_DISCRIMINANT_OK')
print('scalar=2*b; block determinant=2*b*discriminant; total determinant=4*b^2*discriminant')
