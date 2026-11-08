#!/usr/bin/env python3
"""Exact finite checks of cherry/shape covariance in rooted binary leaf-labeled trees.

Generate every rooted nonplane tree on labels 0,...,n-1 exactly once by
inserting the next leaf in every rooted edge (including the stem edge).
No external packages are required.
"""
from fractions import Fraction
from math import comb


def double_factorial_odd(k):
    if k <= 0:
        return 1
    z = 1
    for a in range(1, k+1, 2):
        z *= a
    return z


def attach_everywhere(t, new):
    # The stem edge is included by creating a new root.
    yield (t, new)
    if isinstance(t, tuple):
        left, right = t
        for x in attach_everywhere(left, new):
            yield (x, right)
        for y in attach_everywhere(right, new):
            yield (left, y)


def stats(t):
    if not isinstance(t, tuple):
        return (1, 0, 0, 0)  # leaf size, cherries, balanced, caterpillar
    a, b = t
    na, ca, ba, aa = stats(a)
    nb, cb, bb, ab = stats(b)
    count = na + nb
    cherries = ca + cb + (count == 2)
    bal = ba + bb + (count == 4 and na == 2 and nb == 2)
    asym = aa + ab + (count == 4 and (na == 1 or nb == 1))
    return (count, cherries, bal, asym)


def formulas(n):
    if not (n >= 4):
        raise ValueError('n must be >= 4')
    rn = double_factorial_odd(2*n-3)
    # use integer ratios exactly
    eC = Fraction(comb(n,2),2*n-3)
    eB = Fraction(3*comb(n,4)*double_factorial_odd(2*n-9), rn)
    eA = 4*eB
    disjointB = Fraction(0)
    if n>=6:
        disjointB = Fraction(3*comb(n,2)*comb(n-2,4)*double_factorial_odd(2*n-11), rn)
    covB = 2*eB + disjointB - eC*eB
    covA = eA + 4*disjointB - eC*eA
    return eC,eB,eA,covB,covA


def rational_formula(n):
    a=n*(n-1)*(n-2)*(n-3)
    covB=Fraction(a*(3*n*n-19*n+24),8*(2*n-9)*(2*n-7)*(2*n-5)*(2*n-3)**2)
    covA=Fraction(-a*(n*n-5*n+3),2*(2*n-9)*(2*n-7)*(2*n-5)*(2*n-3)**2)
    return covB,covA


def main():
    trees=[(0,1)]
    total_assertions=0
    for n in range(2,9):
        if n>2:
            trees=[u for t in trees for u in attach_everywhere(t,n-1)]
        assert len(trees)==double_factorial_odd(2*n-3); total_assertions+=1
        if n<4:
            continue
        m=len(trees)
        rows=[stats(t) for t in trees]
        assert all(s[0]==n for s in rows);total_assertions+=m
        ec=Fraction(sum(s[1] for s in rows),m)
        eb=Fraction(sum(s[2] for s in rows),m)
        ea=Fraction(sum(s[3] for s in rows),m)
        covb=Fraction(sum(s[1]*s[2] for s in rows),m)-ec*eb
        cova=Fraction(sum(s[1]*s[3] for s in rows),m)-ec*ea
        f=formulas(n)
        assert (ec,eb,ea,covb,cova)==f;total_assertions+=5
        assert (covb,cova)==rational_formula(n);total_assertions+=2
        assert covb>0 and cova<0;total_assertions+=2
        if n>=6:
            prevb,preva=rational_formula(n-1)
            assert covb/(-cova)>prevb/(-preva);total_assertions+=1
        print('n',n,'trees',m,'E(C)',ec,'E(B)',eb,'E(A)',ea,'Cov(C,B)',covb,'Cov(C,A)',cova)
    print('PASS:',total_assertions,'integer and rational assertions')

if __name__=='__main__':main()
