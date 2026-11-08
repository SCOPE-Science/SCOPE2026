"""Exact diagnostics for sixth moments of two-site signed sampling.

This code corroborates the closed formulas and algebraic identities in RESULT.md.
It is not a substitute for the universal optimization proof.
"""
from fractions import Fraction as F
from itertools import combinations, product
from random import Random


def direct(n, a):
    total2 = F(0)
    total6 = F(0)
    for i, j in combinations(range(n), 2):
        for u, v in product((-1, 1), repeat=2):
            t = u * a[i] + v * a[j]
            total2 += t**2
            total6 += t**6
    den = 4 * (n * (n-1) // 2)
    return total2 / den, total6 / den


def formula(n, a):
    s2 = sum((t**2 for t in a), F(0))
    s4 = sum((t**4 for t in a), F(0))
    s6 = sum((t**6 for t in a), F(0))
    return F(2, n) * s2, F(2, n*(n-1)) * (15*s2*s4 + (n-16)*s6)


def sharp(n):
    lo = F(n*n,4) if n <= 3 else F(4)
    hi = F(n*n*(n+14),16*(n-1)) if n <= 5 else F(n*n,4)
    return lo,hi


def ratio(moments):
    m2, m6 = moments
    return m6/m2**3


rng = Random(460216)
cases = 0
for n in range(2, 17):
    for q in range(28):
        a = [F(rng.randint(-7,7),rng.randint(1,8)) for _ in range(n)]
        if not any(a): a[0]=F(1)
        d, f = direct(n,a),formula(n,a)
        assert d == f, (n,a,d,f)
        kval=ratio(d)
        low, high=sharp(n)
        assert low<=kval<=high, (n,a,kval,low,high)
        cases+=1
print('INDEPENDENT_EXACT_SIGN_AND_PAIR_ENUMERATION_OK',cases)

for n in range(2, 101):
    lo, hi=sharp(n)
    v=[F(0)]*n;v[0]=F(1)
    e=[F(1)]*n
    two=[F(1),F(1)]+[F(0)]*(n-2)
    kv,ke,kt=(ratio(formula(n,x)) for x in (v,e,two))
    assert kv == F(n*n,4)
    assert ke == 4
    if n<=3: assert kv==lo and kt==hi
    elif n==4: assert kv==lo and ke==lo and kt==hi
    elif n==5: assert ke==lo and kt==hi
    elif n==6: assert ke==lo and kt==hi and kv==hi
    else: assert ke==lo and kv==hi
    if n==6:
        for i in range(1,22):
            z=[F(i),F(22-i)]+[F(0)]*(n-2)
            assert ratio(formula(n,z))==hi
print('EXACT_ALL_ENDPOINT_CONFIGURATIONS_OK',99)

# Pair-concentration identity, with no numerical approximations.
for n in range(2,100):
    c=16-n
    for _ in range(200):
        u,v=F(rng.randint(0,31),37),F(rng.randint(0,31),37)
        s=u+v;p=u*v
        lhs=15*(u*u+v*v)-c*(u**3+v**3)
        rhs=15*s*s-c*s**3+3*(c*s-10)*p
        assert lhs==rhs
print('EXACT_TWO_COORDINATE_VARIATION_IDENTITY_OK')

# The dimension-dependent normalized endpoints give the Euclidean-distortion sixth powers.
for n in range(3,101):
    low,hi=sharp(n)
    distortion6 = hi/low
    expected={2:F(4),3:F(17,8),4:F(3,2),5:F(475,256)}.get(n,F(n*n,16))
    assert distortion6==expected
print('EXACT_EUCLIDEAN_DISTORTION_FORMULAS_OK')
print('ALL_SPARSE_PAIR_SIXTH_MOMENT_CHECKS_PASSED')
