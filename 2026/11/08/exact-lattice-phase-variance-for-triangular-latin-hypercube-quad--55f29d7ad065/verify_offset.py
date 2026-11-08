#!/usr/bin/env python3
"""Exact rational checks of an all-offset triangular LHS variance formula.

The independent route below computes cell Bernoulli probabilities and the
permutation covariance identity directly, while the claimed route uses the
single closed polynomial. Neither uses floating-point arithmetic.
"""
from fractions import Fraction as F
from math import factorial
from itertools import permutations

checks=0

def assert_equal(a,b,label):
    global checks
    if a != b:
        raise AssertionError((label,a,b))
    checks+=1

def triangular_cell(t):
    if t<=0:return F(0)
    if t>=2:return F(1)
    if t<=1:return t*t/2
    return 1-(2-t)**2/2

def direct_variance(n,c):
    a=[[triangular_cell(n*c-i-j) for j in range(n)] for i in range(n)]
    rows=[sum(row,F(0)) for row in a]
    total=sum(rows,F(0))
    center=total/F(n*n)
    # Conditional independent jitter in the n selected grid cells.
    jitter=sum((a[i][j]*(1-a[i][j]) for i in range(n) for j in range(n)),F(0))/n
    # Exact permutation-variance identity (n>=2).
    perm=sum(((a[i][j]-rows[i]/n-rows[j]/n+center)**2
             for i in range(n) for j in range(n)),F(0))/(n-1)
    return (jitter+perm)/n**2

def polynomial_formula(n,c):
    s=min(c,2-c)
    t=n*s
    theta=t-(t.numerator//t.denominator)
    L=3*s**4-8*s**3+6*s*s
    P=-6*theta**5+9*theta**4+2*theta**3-6*theta**2+theta
    numerator=n**3*L+n*s*(6*theta**2*(1-theta)**2-1)+P
    return numerator/(12*n**3*(n-1))

for n in range(2,25):
    samples=[F(0),F(1),F(2),F(1,13),F(2,7),F(3,8),F(1,2),F(5,7),
             F(9,10),F(7,9),F(13,17),F(11,10),F(3,2),F(5,3),F(25,13)]
    for c in samples:
        assert_equal(direct_variance(n,c),polynomial_formula(n,c),('variance',n,c))
        if c>=0 and c<=2:
            assert_equal(polynomial_formula(n,c),polynomial_formula(n,2-c),('reflection',n,c))
    # At c=1, recover the known exact center value.
    assert_equal(polynomial_formula(n,F(1)),F(n+1,12*n*n),('center',n))
    # Across each rational grid offset, match a factorial-time permutation
    # enumeration of the conditional-jitter law at small n.
    if n<=6:
        for c in [F(1,3),F(2,5),F(1,2),F(5,4)]:
            a=[[triangular_cell(n*c-i-j) for j in range(n)] for i in range(n)]
            means=[]; within=[]
            for p in permutations(range(n)):
                z=[a[i][p[i]] for i in range(n)]
                means.append(sum(z,F(0)))
                within.append(sum((v*(1-v) for v in z),F(0)))
            av=sum(means,F(0))/factorial(n)
            permv=sum(((v-av)**2 for v in means),F(0))/factorial(n)
            jigv=sum(within,F(0))/factorial(n)
            assert_equal((permv+jigv)/n**2,polynomial_formula(n,c),('enumeration',n,c))

print('PASS: exact all-offset LHS triangular variance')
print('Exact rational assertions:',checks)
for n,c in [(2,F(1,2)),(3,F(2,5)),(4,F(1,1)),(7,F(1,3))]:
    print(f'n={n} c={c} variance={polynomial_formula(n,c)}')
print('The all-n theorem, irrational-phase limit set and asymptotics rely on proof, not finite checks.')
