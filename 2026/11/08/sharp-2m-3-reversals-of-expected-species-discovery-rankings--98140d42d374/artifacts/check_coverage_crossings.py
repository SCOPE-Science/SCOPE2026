#!/usr/bin/env python3
"""Exact reproducibility checks for coverage-deficit crossing witnesses."""
from fractions import Fraction
from itertools import product


def deficit(probs, n):
    return sum((p * (1-p)**n for p in probs), Fraction(0))


def raw_sign(counts_p, counts_q, den, n):
    assert sum(counts_p) == sum(counts_q) == den
    num = sum(v*(den-v)**n for v in counts_p)-sum(v*(den-v)**n for v in counts_q)
    return (num > 0) - (num < 0)


def variation(counts_p, counts_q):
    # Group equal frequencies before counting coefficient sign changes.
    coeff = {}
    for v in counts_p:
        coeff[v] = coeff.get(v, 0) + v
    for v in counts_q:
        coeff[v] = coeff.get(v, 0) - v
    # Decay base is (den-v), hence descending v is ascending base.
    signs = [((coeff[v]>0)-(coeff[v]<0)) for v in sorted(coeff, reverse=True) if coeff[v]]
    return sum(a*b<0 for a,b in zip(signs,signs[1:]))

cases = [
    (10,[1,9],[2,8],[(5,-1),(6,1)]),
    (30,[1,7,22],[2,10,18],[(6,-1),(7,1),(12,1),(13,-1),(15,-1),(16,1)]),
    (1000,[484,426,81,9],[272,58,665,5],
        [(4,1),(5,-1),(14,-1),(15,1),(19,1),(20,-1),
         (47,-1),(48,1),(144,1),(145,-1)]),
]
for den,p,q,expect in cases:
    assert variation(p,q) <= 2*len(p)-2
    for n,expected_sign in expect:
        actual = raw_sign(p,q,den,n)
        assert actual == expected_sign, (den,n,actual,expected_sign)
    vals = [sign for _,sign in expect]
    assert sum(a*b<0 for a,b in zip(vals,vals[1:])) == 2*len(p)-3
    print(f'Exact {len(p)}-species witness: {2*len(p)-3} alternating reversals confirmed')

# Direct state-enumeration check independent of the closed form.
for den,p,_,_ in cases[:2]:
    masses = tuple(Fraction(v,den) for v in p)
    for n in range(0,5):
        expected = Fraction(0)
        for outcome in product(range(len(p)), repeat=n):
            mass = Fraction(1)
            for i in outcome:
                mass *= masses[i]
            missing = sum((x for i,x in enumerate(masses) if i not in outcome),Fraction(0))
            expected += mass*missing
        assert expected == deficit(masses,n)
print('Independent exact enumeration: 10 model/sample-size checks confirmed')

# Illustrate, not replace, the inductive proof with one rational rare-species step.
b = Fraction(1,200)
a = b*b
P = [Fraction(1,10),Fraction(9,10)]
Q = [Fraction(1,5),Fraction(4,5)]
Pnew = [(1-a)*x for x in P]+[a]
Qnew = [(1-b)*x for x in Q]+[b]
for n,s in [(5,-1),(12,1),(200,-1),(2000,1)]:
    h = deficit(Pnew,n)-deficit(Qnew,n)
    assert (h>0)-(h<0)==s
print('Inductive rational step: three reversals confirmed')
print('All exact checks passed')
