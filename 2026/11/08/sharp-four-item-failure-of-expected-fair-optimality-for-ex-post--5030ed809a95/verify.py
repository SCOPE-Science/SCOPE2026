#!/usr/bin/env python3
"""Exact small-case verification for two-agent uncertain Bernoulli items.

Only the standard Python library is needed. This finite checker does not
certify general algebraic claims; those are proved in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product


def nonenv_probability(ps, ownmask):
    m = len(ps)
    ans = Q(0)
    for bits in product((0, 1), repeat=m):
        w = Q(1)
        for b, p in zip(bits, ps):
            w *= p if b else 1 - p
        own = sum(bits[i] for i in range(m) if ownmask & (1 << i))
        other = [bits[i] for i in range(m) if not ownmask & (1 << i)]
        if own >= sum(other) - max(other, default=0):
            ans += w
    return ans


def ef1_probability(ps, ownmask):
    full = (1 << len(ps)) - 1
    return nonenv_probability(ps, ownmask) * nonenv_probability(ps, full ^ ownmask)


def literal_joint_probability(ps, ownmask):
    m = len(ps)
    ans = Q(0)
    for a in product((0, 1), repeat=m):
        wa = Q(1)
        for b, p in zip(a, ps):
            wa *= p if b else 1-p
        for b in product((0, 1), repeat=m):
            wb = Q(1)
            for x, p in zip(b, ps):
                wb *= p if x else 1-p
            bundle_a = [a[i] for i in range(m) if ownmask & (1 << i)]
            other_a = [a[i] for i in range(m) if not ownmask & (1 << i)]
            bundle_b = [b[i] for i in range(m) if not ownmask & (1 << i)]
            other_b = [b[i] for i in range(m) if ownmask & (1 << i)]
            if (sum(bundle_a) >= sum(other_a)-max(other_a, default=0)
                    and sum(bundle_b) >= sum(other_b)-max(other_b, default=0)):
                ans += wa*wb
    return ans


if __name__ == '__main__':
    tests = 0
    for den in (6, 9, 15):
        for x_n in range(1, den):
            for y_n in range(1, den-x_n):
                x, y = Q(x_n,den), Q(y_n,den)
                ps = [x+y,x,y]
                base = ef1_probability(ps, 1)
                assert base-ef1_probability(ps,2) == y*y
                assert base-ef1_probability(ps,4) == x*x
                assert all(base >= ef1_probability(ps,mask) for mask in range(8))
                tests += 1
    e = Q(1,60)
    ps = [e,Q(1,3),Q(2,3),Q(1,3)+e]
    fair = 5
    other = 4
    assert sum(ps[i] for i in range(4) if fair & (1<<i)) == sum(ps[i] for i in range(4) if not fair & (1<<i))
    balanced = [mask for mask in range(16)
                if sum(ps[i] for i in range(4) if mask & (1<<i))
                == sum(ps[i] for i in range(4) if not mask & (1<<i))]
    assert balanced == [5, 10], balanced
    fa = ef1_probability(ps, fair)
    fb = ef1_probability(ps, other)
    assert fa == literal_joint_probability(ps, fair)
    assert fb == literal_joint_probability(ps, other)
    assert fa == ((3*e*e-2*e+26)*(12*e*e-8*e+27))/729
    assert fb == (26-9*e-9*e*e)/27
    assert fb-fa == Q(5431,29160000)
    assert fb > max(ef1_probability(ps,mask) for mask in balanced)
    print('PASS:', tests, 'three-good parameter pairs;',
          'two independent exact four-good joint enumerations;',
          'unique expected-fair partition up to exchange;',
          'gain', fb-fa)
