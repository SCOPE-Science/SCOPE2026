#!/usr/bin/env python3
"""Independent high-dimensional affine-relation and Gaussian-count checks."""
from collections import Counter
from itertools import product
from math import comb, prod

# Six ordered points spanning affine dimension four have a unique
# projective coefficient relation a=(a_0,...,a_5), sum a_i=0.
# Exclude two-coordinate relations, which would identify points.
representatives = set()
for a in product(range(3), repeat=6):
    if not any(a) or sum(a) % 3 != 0:
        continue
    if sum(bool(x) for x in a) < 3:
        continue
    b = tuple((2*x)%3 for x in a)
    representatives.add(min(a, b))
assert len(representatives) == 106

def relation_type(a):
    m = sum(bool(x) for x in a)
    if m == 3:
        assert sorted(x for x in a if x) in ([1]*3, [2]*3)
        return 'three_equal'
    if m == 4:
        assert Counter(x for x in a if x) == {1:2, 2:2}
        return 'four_balanced'
    if m == 5:
        assert sorted(Counter(x for x in a if x).values()) == [1,4]
        return 'five_one_four'
    if m == 6:
        return 'six_equal' if len(set(a)) == 1 else 'six_balanced'
    raise AssertionError(a)

patterns = Counter(relation_type(a) for a in representatives)
assert patterns == {'three_equal':20, 'four_balanced':45,
                    'five_one_four':30, 'six_equal':1,
                    'six_balanced':10}, patterns

# All phase assignments arising from the affine span are exactly
# (u_0,...,u_5) with u_0=0 and a.u=0; a Fourier zero requires 2,2,2.
phase_words = [(0,)+tail for tail in product(range(3),repeat=5)
               if Counter((0,)+tail) == {0:2, 1:2, 2:2}]
assert len(phase_words) == 30
by_type = {}
for a in representatives:
    z = sum(sum(a[i]*u[i] for i in range(6))%3 == 0 for u in phase_words)
    typ = relation_type(a)
    if typ in by_type:
        assert by_type[typ] == z
    by_type[typ] = z
assert by_type == {'three_equal':12,'four_balanced':12,
                   'five_one_four':6,'six_equal':30,'six_balanced':12},by_type

# In affine dimension five, all 3^5 phase words occur, with 30 zeros.
rank5 = 3**5 - len(phase_words)
assert rank5 == 213

GL4 = prod(3**4-3**j for j in range(4))
GL5 = prod(3**5-3**j for j in range(5))
K4 = 3**4*GL4//720
K5 = 3**5*GL5//720
assert 3**4*GL4 % 720 == 0 and 3**5*GL5 % 720 == 0
assert (K4,K5)==(2729376,160503685056)

def gaussian(n,k):
    if not 0<=k<=n:return 0
    top=prod(3**(n-i)-1 for i in range(k))
    bot=prod(3**(k-i)-1 for i in range(k))
    assert top%bot==0
    return top//bot

def flat_count(n,r):
    return 3**(n-r)*gaussian(n,r) if r<=n else 0

for d in range(2,9):
    h2,h3,h4,h5=(flat_count(d,r) for r in range(2,6))
    by_fraction = {
        '1/3': 12*h2,
        '5/9': 10530*h3,
        '17/27': K4*h4,
        '7/9': 72*h2+75816*h3,
        '23/27': 113724*h3+75*K4*h4,
        '71/81': K5*h5,
        '25/27': 75816*h3+30*K4*h4,
        '1': 16848*h3,
    }
    assert sum(by_fraction.values()) == comb(3**d,6),(d,by_fraction)
    if d==3:
        assert by_fraction == {'1/3':468,'5/9':10530,'17/27':0,
           '7/9':78624,'23/27':113724,'71/81':0,'25/27':75816,'1':16848}
print('PASS: 106 relation classes; balanced phase zeros; all-d counts d=2..8.')
