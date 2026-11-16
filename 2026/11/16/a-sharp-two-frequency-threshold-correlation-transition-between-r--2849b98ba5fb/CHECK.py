"""Exact arithmetic checks for a two-frequency threshold-correlation theorem.

The infinite frequency cutoff is proved analytically in RESULT.md. This script
checks the complete finite residue and independent arc-intersection identities.
"""
from fractions import Fraction as F
from math import gcd

R0, R1, R2 = F(1, 6), F(3, 16), F(1, 5)
SMALL = [(1, 2)] + [(1, j) for j in range(3, 16, 2)] + [(3, 5)]
TARGET = {
    (1, 2): (F(1, 30), F(0), F(1, 30)),
    (1, 3): (F(4, 45), F(0), F(0)),
    (1, 5): (F(0), F(0), F(4, 75)),
    (1, 7): (F(16, 105), F(1, 14), F(8, 105)),
    (1, 9): (F(4, 45), F(0), F(0)),
    (1, 11): (F(8, 165), F(1, 22), F(16, 165)),
    (1, 13): (F(8, 65), F(1, 26), F(8, 195)),
    (1, 15): (F(4, 45), F(0), F(4, 75)),
    (3, 5): (F(4, 45), F(1, 30), F(4, 75)),
}
assert SMALL == list(TARGET)


def bernoulli(x):
    y = x - x.numerator // x.denominator
    return y*y-y+F(1, 6)


def probability(a, b, r):
    assert 1 <= a < b and gcd(a,b) == 1
    base = 8*r*r
    if (a+b) % 2 == 0:
        return base + F(2,a*b)*(bernoulli((b-a)*r)-bernoulli((a+b)*r))
    return base + F(1,2*a*b)*(bernoulli(2*(b-a)*r)-bernoulli(2*(a+b)*r))


def sharp(r):
    assert R0 <= r <= R2
    return (28*r-4)/5 if r <= R1 else 4*r/3


def pieces(a, sign, r):
    # Measurable components of the pullback of a circle arc, clipped to [0,1].
    ans = []
    for k in range(-1,a+2):
        center = (F(k,a) if sign == 1 else F(2*k+1,2*a))
        lo,hi = max(F(0),center-r/a), min(F(1),center+r/a)
        if lo < hi: ans.append((lo,hi))
    return sorted(ans)


def overlap(xs,ys):
    i=j=0
    total=F(0)
    while i<len(xs) and j<len(ys):
        lo=max(xs[i][0],ys[j][0]);hi=min(xs[i][1],ys[j][1])
        if lo<hi: total += hi-lo
        if xs[i][1] <= ys[j][1]:i+=1
        else:j+=1
    return total


def geometry(a,b,r):
    return sum((overlap(pieces(a,s,r), pieces(b,s,r)) for s in (1,-1)), F(0))

# Assertion 1: all product exceptions are listed without relying on a finite cutoff.
exceptions=[]
for a in range(1,20):
    for b in range(a+1,20):
        if gcd(a,b)!=1:continue
        if ((a+b)%2==0 and a*b<16) or ((a+b)%2 and a*b<4):
            exceptions.append((a,b))
assert exceptions == SMALL, (exceptions, SMALL)

# Assertion 2: exact values at all three proof nodes.
assert probability(1,3,R1) == F(1,4) == probability(1,5,R1)
for a,b in SMALL:
    actual=tuple(probability(a,b,r)-sharp(r) for r in (R0,R1,R2))
    assert actual == TARGET[(a,b)],(a,b,actual)
    assert all(y>=0 for y in actual)

# Assertion 3: no fractional-part singularity occurs inside either affine cell.
for a,b in SMALL:
    ks = [b-a,a+b] if (a+b)%2==0 else [2*(b-a),2*(a+b)]
    for k in ks:
        assert all(not (R0 < F(j,k) < R2 and F(j,k)!=R1)
                   for j in range(1,k))

# Assertion 4: exact sharp candidate branches.
for j in range(301):
    r=R0+(R2-R0)*F(j,300)
    assert probability(1,5,r)==(28*r-4)/5
    assert probability(1,3,r)==4*r/3
    assert sharp(r)==min(probability(1,5,r),probability(1,3,r))
    assert 8*r*r-sharp(r)>=F(1,32)

# Assertion 5: compare the Bernoulli and independently constructed arc formulas.
comparisons=0
for b in range(2,22):
    for a in range(1,b):
        if gcd(a,b)!=1:continue
        for r in (F(1,6), F(17,100), F(11,60), F(3,16), F(19,100),F(1,5)):
            assert probability(a,b,r)==geometry(a,b,r),(a,b,r,probability(a,b,r),geometry(a,b,r))
            comparisons += 1
print('CHECK_OK: exact finite table, analytic-cutoff exceptions, affine breakpoints, candidates, independent interval overlaps;',comparisons,'geometric comparisons')
