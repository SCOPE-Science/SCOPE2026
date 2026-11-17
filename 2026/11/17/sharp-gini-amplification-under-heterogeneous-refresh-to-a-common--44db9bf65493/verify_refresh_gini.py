"""Exact finite checks for Gini variation under heterogeneous mean refresh.

Run with Python 3 standard library: python verify_refresh_gini.py
Finite checks supplement, rather than replace, the all-n proof.
"""
from fractions import Fraction
from itertools import product
from random import Random


def gini(v):
    return sum(abs(x-y) for i,x in enumerate(v) for y in v[i+1:])


def refresh(v, a):
    mean = sum(v)/len(v)
    return [(1-ai)*x+ai*mean for x,ai in zip(v,a)]


def expected(n):
    return Fraction(1)+Fraction(((n-2)**2)//4,n*(n-1))


def binary_cut_ratio(n, cut, refreshed):
    k = cut.bit_count()
    m = n-k
    r = (cut & refreshed).bit_count()
    s = ((~cut) & refreshed & ((1<<n)-1)).bit_count()
    val = n*k*m + k*s*(m-k-s) + m*r*(k-m-r)
    return Fraction(val,n*k*m)


# Full binary choices of sites and of inputs, with an independent direct Gini calculation.
checked = 0
for n in range(2,9):
    best = Fraction(0)
    for cut in range(1,(1<<n)-1):
        f = [Fraction((cut>>i)&1) for i in range(n)]
        denominator = gini(f)
        for refreshed in range(1<<n):
            a = [Fraction((refreshed>>i)&1) for i in range(n)]
            direct = gini(refresh(f,a))/denominator
            algebra = binary_cut_ratio(n,cut,refreshed)
            assert direct == algebra, (n,cut,refreshed,direct,algebra)
            best = max(best,algebra)
            checked += 1
    assert best == expected(n),(n,best,expected(n))
print('EXACT_BINARY_REFRESH_AND_CUT_PAIRS_PASSED',checked)

# Direct random rational rate profiles and arbitrary rational inputs.
rng = Random(20261110)
checks = 0
for n in range(2,13):
    for trial in range(240):
        a = [Fraction(rng.randrange(13),12) for _ in range(n)]
        v = [Fraction(rng.randrange(-15,16),5) for _ in range(n)]
        d = gini(v)
        if not d:
            continue
        assert gini(refresh(v,a)) <= expected(n)*d
        checks += 1
print('RATIONAL_INTERIOR_RATE_AND_INPUT_BOUNDS_PASSED',checks)

# The explicit sharp singleton cut and its polarized refresh profile.
for n in range(2,401):
    s = (n-2)//2
    f = [Fraction(int(i==0)) for i in range(n)]
    a = [Fraction(int(1<=i<=s)) for i in range(n)]
    out = gini(refresh(f,a))/gini(f)
    assert out == expected(n), (n,out,expected(n))
    if n>=4:
        assert out > 1
    else:
        assert out == 1
print('EXACT_SHARP_SINGLETON_WITNESSES_PASSED',399)

# Every site can have strictly positive refresh rate and amplify once n>=4.
for n in range(4,101):
    s=(n-2)//2
    e=Fraction(1,1000)
    a=[Fraction(1) if 1<=i<=s else e for i in range(n)]
    f=[Fraction(int(i==0)) for i in range(n)]
    assert gini(refresh(f,a)) / gini(f) == (1-e)*expected(n)
    assert gini(refresh(f,a)) > gini(f)
print('ALL_POSITIVE_SITE_RATE_AMPLIFICATION_WITNESSES_PASSED',97)
print('ALL_HETEROGENEOUS_REFRESH_GINI_CHECKS_PASSED')
