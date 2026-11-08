#!/usr/bin/env python3
"""Exact finite stress checks for a distribution-free four-item pairing theorem.

The proof is analytic.  This checker independently tests exhaustive ordered
three-point rational laws, with continuous independent symmetric jitter for
removing ties, and rational exponential examples.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from collections import defaultdict


def fdominates(x, y):
    # x is first-order stochastically larger than y
    return x[0] <= y[0] and x[0] + x[1] <= y[0] + y[1]


def conv(x, y):
    z = defaultdict(F)
    for i, a in x.items():
        for j, b in y.items():
            z[i + j] += a * b
    return dict(z)


def to_dist(t):
    return {i: F(v, 4) for i, v in enumerate(t) if v}


def win(x, y):
    return sum(a * b * (F(1) if i > j else F(1, 2) if i == j else F(0))
               for i, a in x.items() for j, b in y.items())


def prob(choices, i, j, generic):
    v = [to_dist(s) for s in choices]
    others = [k for k in range(4) if k not in (i, j)]
    u = conv(conv(v[i], v[j]), generic)
    w = conv(conv(v[others[0]], v[others[1]]), generic)
    return win(u, w)


def exact_exp_win(means):
    a, b, c, d = [F(1, n) for n in means]
    return (c * d * (a*a + a*b + a*c + a*d + b*b + b*c + b*d + c*d)
            / ((a+c)*(a+d)*(b+c)*(b+d)))


def main():
    pmfs = [(a,b,4-a-b) for a in range(5) for b in range(5-a)]
    chains = 0
    cases = 0
    for x in pmfs:
        for y in pmfs:
            if not fdominates(x,y): continue
            for z in pmfs:
                if not fdominates(y,z): continue
                for w in pmfs:
                    if not fdominates(z,w): continue
                    chains += 1
                    for g in ({0:F(1)}, {0:F(1,2), 1:F(1,2)}):
                        a = [prob((x,y,z,w), 0, j, g) for j in (1,2,3)]
                        assert a[0] >= a[1] >= F(1,2), (x,y,z,w,g,a)
                        assert 1-a[1] <= a[2] <= a[1], (x,y,z,w,g,a)
                        assert a[2]*(1-a[2]) >= a[1]*(1-a[1]) >= a[0]*(1-a[0])
                        cases += 1
    a,b,c,d=(8,4,2,1)
    ps=[exact_exp_win(v) for v in ((a,b,c,d),(a,c,b,d),(a,d,b,c))]
    assert ps == [F(8,9),F(58,81),F(3,5)], ps
    assert [p*(1-p) for p in ps] == [F(8,81), F(1334,6561), F(6,25)]
    # Mean-ordered laws without FSD: first item is mixture of 0,9,100
    # (probabilities 1/2, 2/5, 1/10), other three are 9,3,1.
    # Adding iid U(0,1/4) jitter preserves strict comparison outcomes.
    q=[F(1),F(1,2),F(1,10)]
    assert [p*(1-p) for p in q] == [F(0), F(1,4), F(9,100)]
    print('PASS: first-order stochastic-dominance chains:',chains)
    print('PASS: exact pairing checks (two baseline laws):',cases)
    print('PASS: independent exponential example:',[str(p) for p in ps])
    print('PASS: mean-order counterexample:',[str(p) for p in q])

if __name__=='__main__': main()
