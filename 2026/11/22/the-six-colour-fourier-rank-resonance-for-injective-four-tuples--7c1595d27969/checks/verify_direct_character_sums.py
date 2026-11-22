"""Direct independent K4 colouring/character-sum calculation.

Run: python3 checks/verify_direct_character_sums.py
Python standard library, with floating point character evaluation as an additional
finite numerical cross-check (not used to prove all-group identities).
"""
from collections import Counter
from itertools import product
from math import cos, sin, tau


def check(factors):
    points = list(product(*(range(m) for m in factors)))
    q = len(points)
    zs = (0,) * len(factors)
    def add(a,b):
        return tuple((x+y)%m for x,y,m in zip(a,b,factors))
    def neg(a):
        return tuple((-x)%m for x,m in zip(a,factors))
    def val(k,x):
        angle = tau * sum(a*b/m for a,b,m in zip(k,x,factors))
        return complex(cos(angle), sin(angle))
    # Character table over the direct product group.
    char = {(k,x): val(k,x) for k in points for x in points}
    injective = [x for x in product(points, repeat=4) if len(set(x)) == 4]
    tally = Counter()
    for a in points:
        for b in points:
            for c in points:
                d = neg(add(add(a,b),c))
                total = sum(char[a,x[0]]*char[b,x[1]]*char[c,x[2]]*char[d,x[3]] for x in injective)
                n = round(total.real)
                assert abs(total - n) < 1.e-6, (factors, (a,b,c,d), total)
                tally[n] += 1
    t = sum(add(x,x)==zs for x in points)
    expected = Counter()
    for value,count in [
        (q*(q-1)*(q-2)*(q-3),1),
        (-q*(q-2)*(q-3),6*(q-1)),
        (2*q*(q-3),4*(q-1)*(q-2)),
        (-6*q,q**3-7*q*q+15*q-8-t),
        (q*(q-6),3*q*q-12*q+6+3*t),
        (2*q*(q-3),3*(q-t)),
        (3*q*(q-2),t-1)]:
        expected[value]+=count
    assert tally == +expected,(factors,tally,expected)
    print('PASS direct character sums',factors,'|proper colourings|=',len(injective), 'histogram=',sorted(tally.items()))


if __name__ == '__main__':
    for factors in ((4,), (2,2), (5,), (6,), (8,), (2,2,2)):
        check(factors)
