"""Exact finite corroboration of the three-term contractivity proof.

No finite loop is used to infer any infinite quantifier; the infinite theorem
uses the inequalities in the accompanying mathematical proof.
"""
from itertools import product, combinations
from math import comb

checks = 0


def check(test, description):
    global checks
    if not test:
        raise AssertionError(description)
    checks += 1


# Exact integer certificates for the strict scalar constant comparisons.
check(3**5 * 20**4 < 79**4, '3^(5/4) < 79/20')
check(59**5 * 3**3 < 50**5 * 4**3, '59/20 < (5/2)(4/3)^(3/5)')

# Numerical powers are unnecessary: x=a^5, etc., reduce the scalar
# inequality to one integer comparison.
for a in range(1, 9):
    for b in range(a+1):
        for c in range(b+1):
            x,y,z = a**5,b**5,c**5
            rhs = x*x+y*y+z*z+x*y
            numerator = a**8+b**8+c**8
            check(numerator**5 <= rhs**4, 'scalar inequality')
            if b:
                check(numerator**5 < rhs**4, 'strict scalar inequality')

# Verify difference uniqueness for all progression-free triples of
# homogeneous exponents at several low degrees and dimensions.
for m in range(1, 9):
    for n in (2,3):
        exponents = [t for t in product(range(m+1), repeat=n)
                     if sum(t) == m]
        for T in combinations(exponents, 3):
            midpoint = any(all(2*T[j][d]==T[i][d]+T[k][d]
                               for d in range(n))
                           for j in range(3)
                           for i,k in ((q,r) for q in range(3)
                                       for r in range(q+1,3)
                                       if j!=q and j!=r))
            if midpoint:
                continue
            diffs = [tuple(T[i][d]-T[j][d] for d in range(n))
                     for i in range(3) for j in range(3) if i!=j]
            check(len(set(diffs)) == 6, 'distinct nonzero differences')

print('THREE_MONOMIAL_BH_EXACT_OK', checks)
