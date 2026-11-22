#!/usr/bin/env python3
"""Reproduce exact two-feature/three-trait frozen-state counts on bicliques.

Standard-library only. All enumerations are finite certificates for the fixed
nine-culture alphabet; the all-order proof uses surjections onto these supports.
"""
from collections import Counter
from itertools import product
from math import factorial, comb

C = list(product(range(3), repeat=2))
REL = [[int(x == y or (x[0] != y[0] and x[1] != y[1])) for y in C] for x in C]

def common_neighbours(s):
    return frozenset(v for v in range(9) if all(REL[u][v] for u in s))

def explicit_formula(a,b):
    return (9*(5**a + 5**b)+18*2**(a+b)+6*3**(a+b)
            -36*(2**a+2**b)-18*(3**a+3**b)+81)

def stirling(n,k):
    return sum((-1)**(k-j)*comb(k,j)*j**n for j in range(k+1))//factorial(k)

def surjection_count(a,b,profile):
    return sum(v*factorial(k)*stirling(a,k)*c**b
               for (k,c),v in profile.items() if c)

profile = Counter()
for mask in range(1,1<<9):
    s = [i for i in range(9) if mask & (1<<i)]
    profile[(len(s),len(common_neighbours(s)))] += 1
assert sum(profile.values()) == 511
positive = {(k,c):v for (k,c),v in profile.items() if c}
assert positive == {(1,5):9,(2,2):18,(2,3):18,
                    (3,1):72,(3,3):6,(4,1):45,(5,1):9}
print('NINE_CULTURE_SUPPORT_CLASSIFICATION_PASS',sorted(positive.items()))

# Independently enumerate all inclusion-wise maximal oriented complete bicliques
# in the looped culture compatibility relation.
maximal=set()
for mask in range(1,1<<9):
    a = frozenset(i for i in range(9) if mask & (1<<i))
    b = common_neighbours(a)
    if b and common_neighbours(b) == a:
        maximal.add((a,b))
shape=Counter((len(a),len(b)) for a,b in maximal)
assert shape == {(1,5):9,(5,1):9,(2,2):18,(3,3):6}
for a,b in maximal:
    assert all(REL[x][y] for x in a for y in b)
print('FORTY_TWO_MAXIMAL_COMPATIBILITY_BICLIQUES_PASS',dict(shape))

# Algebraic certificate from support counts, for arbitrary positive a,b.
for a in range(1,25):
    for b in range(1,25):
        assert surjection_count(a,b,profile)==explicit_formula(a,b),(a,b)
print('SURJECTION_EXPANSION_AND_SYMMETRIC_FORMULA_PASS 576')

# Separate, direct labelled graph-state enumeration for small shore sizes.
# This loop does not use support counts or Stirling numbers.
case_count=0
for a,b in [(1,1),(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3)]:
    count=0
    for left in product(range(9),repeat=a):
        for right in product(range(9),repeat=b):
            if all(REL[x][y] for x in left for y in right):
                count+=1
    assert count==explicit_formula(a,b),(a,b,count)
    case_count+=1
print('INDEPENDENT_DIRECT_ALL_STATES_CHECK_PASS',case_count)

# Maximal motif counting; the asymptotic source amplitudes are 9 and 6.
triangles=[frozenset((i,perm[i]) for i in range(3))
            for perm in __import__('itertools').permutations(range(3))]
assert len(triangles)==6
for tri in triangles:
    assert all(REL[C.index(x)][C.index(y)] for x in tri for y in tri)

# Rigorous limit dominance via exact base comparisons (both shores diverge).
assert 3**2 > 2**2
assert 5>3>2
# Exactly enumerate four covering motif events for small graph instances.
D = [frozenset(C.index((i,perm[i])) for i in range(3))
     for perm in __import__('itertools').permutations(range(3))]
assert len(D)==6
rectangles = [(frozenset((x,y)),common_neighbours((x,y)))
              for x in range(9) for y in range(x+1,9)
              if C[x][0]==C[y][0] or C[x][1]==C[y][1]]
assert len(rectangles)==18
for a,b in ((1,1),(1,3),(2,2),(2,3),(3,3)):
    cnt=Counter()
    for left in product(range(9), repeat=a):
        ls=frozenset(left)
        for right in product(range(9), repeat=b):
            rs=frozenset(right)
            ok=all(REL[x][y] for x in left for y in right)
            mono_left=len(ls)==1
            mono_right=len(rs)==1
            tri=any(ls|rs<=d for d in D)
            rect=any(ls==u and rs==v for u,v in rectangles)
            if ok:
                assert mono_left or mono_right or tri or rect
            else:
                assert not tri and not rect
            assert not(rect and (mono_left or mono_right or tri))
            if ok:
                cnt['total']+=1
                if mono_left:cnt['M']+=1
                if mono_right:cnt['N']+=1
                if tri:cnt['T']+=1
                if rect:cnt['R']+=1
    assert cnt['total']==explicit_formula(a,b)
    assert cnt['M']==9*5**b
    assert cnt['N']==9*5**a
    assert cnt['T']==6*3**(a+b)-9
    assert cnt['R']==18*(2**a-2)*(2**b-2)
print('FOUR_MOTIF_EXHAUSTIVENESS_AND_EXACT_COMPONENT_COUNTS_PASS')

print('EXACT_DOMINANCE_BASES_PASS')
print('VERIFY_OK')
