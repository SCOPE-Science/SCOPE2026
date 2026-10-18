from math import factorial
from fractions import Fraction

def deg(n):
    assert n >= 4
    return 2*factorial(4*n-7)//((n-1)*(n-2)*factorial(2*n-3)*factorial(2*n-5))

def euler(n):
    return 2*n*(n-1)

def root_denominator(n):
    z = 2*n-3
    for j in range(3,n+1):
        z *= (j-1)*(j-2)*(2*n-j-1)*(2*n-j-2)
    return z

def closed_denominator(n):
    return (n-1)*(n-2)*factorial(2*n-3)*factorial(2*n-5)

assert deg(4) == 168
assert euler(4) == 24

checks = 0
for n in range(4,201):
    D = deg(n)
    E = euler(n)
    assert D > E
    assert root_denominator(n) == closed_denominator(n)
    checks += 1

for n in range(4,200):
    lhs = Fraction(deg(n+1),deg(n))
    rhs = Fraction(2*(4*n-5)*(4*n-3), n*(2*n-1))
    assert lhs == rhs
    assert Fraction(deg(n+1),euler(n+1)) > Fraction(deg(n),euler(n))
    poly = 30*n**3 - 97*n**2 + 95*n - 30
    assert poly > 0
    checks += 1

print("VERIFY_OK", checks)
