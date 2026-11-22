"""Finite exact and numerical diagnostics for the factorial-block semigroup.

These checks are not proofs of the infinite-dimensional claims.
"""
from fractions import Fraction
from math import factorial, exp, pi, sin
import cmath

# Exact multiplicative cocycle on rational exponents, using the variable
# u=exp(-q*z) and v=exp(-d*z), for distinct complex times.
for n in range(1, 11):
    for u in (Fraction(1, 3), Fraction(2, 5), Fraction(3, 4)):
        for v in (Fraction(1, 7), Fraction(4, 5)):
            left = (1-u) + u*(1-v)
            assert left == 1-u*v

# Factorial digit tails on finite expansions are bounded by the next digit.
for jmax in range(3, 14):
    digits = {j: (j-1)//3 for j in range(2, jmax+1)}
    x = sum((Fraction(digits[j], factorial(j)) for j in digits), Fraction(0))
    for n in range(1, jmax):
        tail = factorial(n)*x
        tail -= tail.numerator // tail.denominator
        assert Fraction(digits[n+1], n+1) <= tail <= Fraction(digits[n+1]+1, n+1)

# All rational frequencies eventually kill the upper right block exactly.
for den in range(1, 30):
    for num in range(-3, 4):
        x = Fraction(num, den)
        assert all(factorial(n)*x == int(factorial(n)*x) for n in range(den, den+4))

# Evaluate the semigroup law and imaginary-time magnitude for finite blocks.
for n in range(1, 9):
    q = factorial(n); d = q*q; gamma = 0.6
    def block(z):
        a=cmath.exp(-d*z)
        return a, (n**gamma)*a*(1-cmath.exp(-q*z)), a*cmath.exp(-q*z)
    z=complex(0.15,0.02); w=complex(0.06,0.03)
    a,b,c=block(z); e,f,g=block(w)
    aa,bb,cc=block(z+w)
    assert abs(aa-a*e)<1e-10 and abs(cc-c*g)<1e-10
    assert abs(bb-(a*f+b*g))<1e-10

print('PASS: exact cocycle, rational frequencies, factorial tails, finite blocks')
