from fractions import Fraction
from math import factorial, comb

def degree_factorial(n):
    M = n*(n+1)//2
    x = Fraction(factorial(M), 1)
    for j in range(1, n):
        x *= factorial(j)
    for j in range(1, n+1):
        x /= factorial(2*j-1)
    assert x.denominator == 1
    return x.numerator

def degree_shifted(n):
    lam = list(range(n, 0, -1))
    M = sum(lam)
    x = Fraction(factorial(M), 1)
    for a in lam:
        x /= factorial(a)
    for i in range(n):
        for j in range(i+1, n):
            x *= Fraction(lam[i]-lam[j], lam[i]+lam[j])
    assert x.denominator == 1
    return x.numerator

checks = ratio_checks = 0
for n in range(1, 31):
    D = degree_factorial(n)
    assert D == degree_shifted(n)
    E = 2**n
    if n <= 4:
        assert D < E
    else:
        assert D > E
    assert D != E
    checks += 1

for n in range(1, 30):
    M = n*(n+1)//2
    lhs = Fraction(degree_factorial(n+1), degree_factorial(n))
    rhs = Fraction(comb(M+n+1, n+1), comb(2*n+1, n+1))
    assert lhs == rhs
    if n == 2:
        assert lhs == 2
    if n >= 3:
        assert lhs > 2
    ratio_checks += 1

assert degree_factorial(4) == 12
assert degree_factorial(5) == 286
assert 2**4 == 16 and 2**5 == 32

print("VERIFY_OK", checks, ratio_checks)
