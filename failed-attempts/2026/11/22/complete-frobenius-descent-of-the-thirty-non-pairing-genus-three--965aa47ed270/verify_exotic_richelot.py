#!/usr/bin/env python3
"""Exact finite group calculations for the thirty non-pairing genus-three kernels.
Uses only Python's standard library. Outputs no network traffic.
"""
from collections import Counter
from itertools import combinations, permutations
import json

N = 8
BITS = (1 << N) - 1
EVEN = sorted({min(a, a ^ BITS) for a in range(BITS + 1) if a.bit_count() % 2 == 0})
assert len(EVEN) == 64

def plus(a, b):
    t = a ^ b
    return min(t, t ^ BITS)

def orthogonal(a, b):
    return not ((a & b).bit_count() % 2)

def cycle_types(n, minimum=1):
    if n == 0:
        yield ()
        return
    for k in range(minimum, n + 1):
        for tail in cycle_types(n - k, k):
            yield (k,) + tail

def standard_permutation(partition):
    image = []
    initial = 0
    for length in partition:
        image.extend(range(initial + 1, initial + length))
        image.append(initial)
        initial += length
    assert len(image) == 8
    return tuple(image)

def transport(mask, image):
    t = 0
    for i in range(8):
        if mask & (1 << i):
            t |= (1 << image[i])
    return min(t, t ^ BITS)

def orbit_spectrum(transition):
    remaining = set(range(len(transition)))
    result = Counter()
    while remaining:
        i = min(remaining)
        j = i
        length = 0
        while j in remaining:
            remaining.remove(j)
            j = transition[j]
            length += 1
        assert j == i
        result[length] += 1
    return tuple(sorted(result.items()))

def all_matchings(vertices):
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for j in vertices[1:]:
        for tail in all_matchings(tuple(x for x in vertices[1:] if x != j)):
            yield ((first, j),) + tail

# Independent construction 1: every Lagrangian by isotropic triples of the
# 6-dimensional even-subset vector space.
lagrangians = set()
for a, b, c in combinations(EVEN[1:], 3):
    if not (orthogonal(a,b) and orthogonal(a,c) and orthogonal(b,c)):
        continue
    s = frozenset((0, a, b, c, plus(a,b), plus(a,c), plus(b,c), plus(plus(a,b),c)))
    if len(s) == 8:
        lagrangians.add(s)
assert len(lagrangians) == 135

tractable = set()
for matching in all_matchings(tuple(range(8))):
    sub = {0}
    for a, b in matching:
        basis = min((1 << a) | (1 << b), BITS ^ ((1 << a) | (1 << b)))
        sub |= {plus(basis, z) for z in tuple(sub)}
    assert len(sub) == 8
    tractable.add(frozenset(sub))
assert len(tractable) == 105
nontractable = lagrangians - tractable
assert len(nontractable) == 30
assert all(all(z == 0 or z.bit_count() == 4 for z in s) for s in nontractable)

# Independent construction 2: all affine structures on the eight labelled
# points. The seven hyperplane bipartitions are computed directly, without
# consulting the symplectic linear algebra or the pairing construction.
structures = set()
for labelling in permutations(range(8)):
    planes = []
    for functional in range(1,8):
        mask = sum(1 << i for i, coord in enumerate(labelling)
                   if (functional & coord).bit_count() % 2 == 0)
        assert mask.bit_count() == 4
        planes.append(min(mask, mask ^ BITS))
    assert len(set(planes)) == 7
    structures.add(frozenset(planes))
assert len(structures) == 30
assert structures == {frozenset(s-{0}) for s in nontractable}

# Check both independently produced thirty-point Frobenius permutations.
nontractable_order = sorted(nontractable, key=lambda v:tuple(sorted(v)))
index_lagrangian = {x: i for i,x in enumerate(nontractable_order)}
structure_order = sorted(structures, key=lambda v:tuple(sorted(v)))
index_affine = {x:i for i,x in enumerate(structure_order)}
tractable_order = sorted(tractable, key=lambda v:tuple(sorted(v)))
index_tractable = {x:i for i,x in enumerate(tractable_order)}

rows = []
for partition in cycle_types(8):
    sigma = standard_permutation(partition)
    transition_a = [index_lagrangian[frozenset(transport(z,sigma) for z in subset)] for subset in nontractable_order]
    transition_b = [index_affine[frozenset(transport(z,sigma) for z in subset)] for subset in structure_order]
    assert orbit_spectrum(transition_a) == orbit_spectrum(transition_b)
    transition_t = [index_tractable[frozenset(transport(z,sigma) for z in subset)] for subset in tractable_order]
    u = orbit_spectrum(transition_a)
    t = orbit_spectrum(transition_t)
    assert sum(degree*count for degree,count in u) == 30
    assert sum(degree*count for degree,count in t) == 105
    rows.append(dict(branch_partition=list(partition), nontractable_frobenius_cycles=[[a,b] for a,b in u], tractable_rational_kernels=dict(t).get(1,0), nontractable_rational_kernels=dict(u).get(1,0)))
assert len(rows) == 22
special = next(row for row in rows if row['branch_partition'] == [1,7])
assert special['nontractable_frobenius_cycles'] == [[1,2],[7,4]]
assert special['tractable_rational_kernels'] == 0
assert sum(transport(mask, standard_permutation((1,7))) == mask for mask in EVEN) == 1

# Independent 7-cycle fixed point count via conjugacy class in AGL_3(F2).
# Any affine map of 8 points fixing one point uniquely corresponds to a linear
# element of GL_3(F2) of order 7. GL_3(F2) has exactly 48 such elements.
# Therefore 8*48=384 7-cycles lie in AGL_3(F2), giving
# [S8:AGL3]*384/(8!/7)=2 fixed affine structures.
from math import factorial
# Enumerate invertible linear maps by independent images of basis 1,2,4.
# This is separate from constructing the 30 coset action above.
linear_order_seven = 0
linear_group_order = 0
for b1, b2, b4 in permutations(range(1,8), 3):
    image = [((b1 if i & 1 else 0) ^
              (b2 if i & 2 else 0) ^
              (b4 if i & 4 else 0)) for i in range(8)]
    if len(set(image)) != 8:
        continue
    linear_group_order += 1
    if orbit_spectrum(image) == ((1,1),(7,1)):
        linear_order_seven += 1
assert linear_group_order == 168
assert linear_order_seven == 48
assert (30 * (8 * linear_order_seven)) % (factorial(8)//7) == 0
assert 30 * (8 * linear_order_seven) // (factorial(8)//7) == 2

# An explicit odd-characteristic example: x(x^7+x+1) over F5.
# Rabin's irreducibility criterion at prime degree 7: x^(5^7)=x mod f
# and gcd(f, x^5-x)=1; assert using monic polynomial remainder arithmetic.
p = 5
f = (1,1,0,0,0,0,0,1)  # 1+x+x^7

def trim(a):
    a = tuple(a)
    while len(a)>1 and a[-1] == 0: a=a[:-1]
    return a

def rem(a, b):
    a = list(trim(a)); b = trim(b)
    while len(a)>=len(b) and a != [0]:
        d = len(a)-len(b); c=a[-1]*pow(b[-1], -1, p)%p
        for i,v in enumerate(b): a[d+i]=(a[d+i]-c*v)%p
        a=list(trim(a))
    return tuple(a)

def multiply(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]=(z[i+j]+x*y)%p
    return trim(z)

def modular_power(base, exponent):
    result=(1,)
    while exponent:
        if exponent & 1:result=rem(multiply(result,base),f)
        base=rem(multiply(base,base),f)
        exponent>>=1
    return result

def gcd(a,b):
    while b!=(0,):a,b=b,rem(a,b)
    return trim(a)

x=(0,1)
assert modular_power(x, 5**7) == x
q=list(modular_power(x,5));q[1]=(q[1]-1)%5
assert len(gcd(f,trim(q)))==1

print('GENUS_THREE_30_NONTRACTABLE_22_FROBENIUS_TYPES_VERIFIED')
print('geometry: 135 isotropic kernels = 105 pair-matchings + 30 affine structures')
print('branch (1,7): two rational non-pairing kernels, zero rational pairing kernels')
print('F5_example: x*(x^7+x+1), irreducible degree seven factor')
print('all 22 partitions and affine-structure spectra:', json.dumps(rows,sort_keys=True,separators=(',',':')))
