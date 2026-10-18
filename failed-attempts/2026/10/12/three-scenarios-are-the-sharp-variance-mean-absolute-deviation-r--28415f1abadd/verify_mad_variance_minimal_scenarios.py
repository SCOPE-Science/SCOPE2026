#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

def mean(xs):
    return Fraction(sum(xs), len(xs))

def mad(xs):
    m=mean(xs)
    return sum(abs(Fraction(x)-m) for x in xs)/len(xs)

def var(xs):
    m=mean(xs)
    return sum((Fraction(x)-m)**2 for x in xs)/len(xs)

# One scenario: every sample is constant, both risks are zero.
for x in range(-20,21):
    assert mad((x,)) == 0 and var((x,)) == 0

# Two equal-weight scenarios: MAD^2 = variance exactly.
for a in range(-30,31):
    for b in range(-30,31):
        xs=(a,b)
        assert mad(xs)*mad(xs) == var(xs)

A=(10,20,30)
B=(14,15,31)
assert mean(A)==mean(B)==20
assert mad(A)==Fraction(20,3)
assert mad(B)==Fraction(22,3)
assert var(A)==Fraction(200,3)
assert var(B)==Fraction(182,3)
assert mad(A)<mad(B)
assert var(A)>var(B)

# Structural identity for every centered integer triple checked in a box.
# Choose the sign orientation so two deviations are nonpositive:
# (-a,-b,a+b), with a,b>=0. Let s=a+b and h=|a-b|.
for a in range(0,41):
    for b in range(0,41):
        if a==0 and b==0:
            continue
        xs=(-a,-b,a+b)
        s=a+b
        h=abs(a-b)
        assert mean(xs)==0
        assert mad(xs)==Fraction(2*s,3)
        assert var(xs)==Fraction(s*s,2)+Fraction(h*h,6)

# Persistent equal-mean family: pad both samples with their common mean.
for n in range(3,501):
    An=A+(20,)*(n-3)
    Bn=B+(20,)*(n-3)
    assert mean(An)==mean(Bn)==20
    assert mad(An)==Fraction(20,n)
    assert mad(Bn)==Fraction(22,n)
    assert var(An)==Fraction(200,n)
    assert var(Bn)==Fraction(182,n)
    assert mad(An)<mad(Bn)
    assert var(An)>var(Bn)

print('VERIFY_OK')
print('two_scenario_identity=MAD^2=variance')
print('A', mean(A), mad(A), var(A))
print('B', mean(B), mad(B), var(B))
print('triple_identity_checked_a_b_0_to_40')
print('persistent_family_checked_n_3_to_500')
