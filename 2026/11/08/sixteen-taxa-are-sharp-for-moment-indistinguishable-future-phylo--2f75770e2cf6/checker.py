#!/usr/bin/env python3
"""Exact verification of moment equivalence in unit-edge rooted trees.

Run with Python 3. No external packages or downloads required.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from math import comb

@lru_cache(None)
def shapes(n):
    """Canonical unordered rooted full-binary shapes on n leaves."""
    if n == 1:
        return ((),)
    ans = []
    for left in range(1, n // 2 + 1):
        for a in shapes(left):
            for b in shapes(n - left):
                if left == n - left and a > b:
                    continue
                ans.append((a, b))
    return tuple(ans)

@lru_cache(None)
def edge_profile(t):
    """Incoming-edge size list and ordered ancestor/descendant size pairs."""
    if t == ():
        return 1, (1,), ()
    n1, a, pa = edge_profile(t[0])
    n2, b, pb = edge_profile(t[1])
    n = n1 + n2
    return n, (n,) + a + b, pa + pb + tuple((n, x) for x in a + b)

def signature(t):
    """Coefficients in increasing powers of extinction probability q."""
    n = edge_profile(t)[0]
    sizes = edge_profile(t[0])[1] + edge_profile(t[1])[1]
    pairs = edge_profile(t[0])[2] + edge_profile(t[1])[2]
    expected = [0] * (n + 1)
    variance = [0] * (2 * n + 1)
    expected[0] = len(sizes)
    for k in sizes:
        expected[k] -= 1
        variance[k] += 1
        variance[2 * k] -= 1
    for ancestor, desc in pairs:
        variance[ancestor] += 2
        variance[ancestor + desc] -= 2
    return tuple(expected), tuple(variance)

def canon(a, b):
    na, nb = edge_profile(a)[0], edge_profile(b)[0]
    if (na, a) <= (nb, b):
        return (a, b)
    return (b, a)

leaf = ()
cherry = (leaf, leaf)
three = canon(leaf, cherry)
C4 = canon(leaf, three)
B4 = canon(cherry, cherry)
A = canon(canon(C4, C4), canon(B4, B4))
B = canon(canon(C4, B4), canon(C4, B4))

expected_shape_counts = [0, 1, 1, 1, 2, 3, 6, 11, 23, 46, 98, 207, 451, 983, 2179, 4850, 10905]
for n in range(2, 17):
    ts = shapes(n)
    assert len(ts) == expected_shape_counts[n], (n, len(ts))
    classes = defaultdict(list)
    for t in ts:
        classes[signature(t)].append(t)
    collisions = [group for group in classes.values() if len(group) >= 2]
    if n < 16:
        assert not collisions, (n, collisions)
    else:
        assert len(collisions) == 1 and len(collisions[0]) == 2
        assert set(collisions[0]) == {A, B}
    print('n=%d shapes=%d colliding_pairs=%d' %
          (n, len(ts), sum(len(g) * (len(g) - 1) // 2 for g in collisions)))

# Different method from the edge-covariance signature: enumerate ALL 2^16
# surviving subsets at q=1/2, recording edge coverage directly.
def edge_masks(t, first=0):
    if t == ():
        return 1 << first, [1 << first], first + 1
    _, aa, middle = edge_masks(t[0], first)
    _, bb, last = edge_masks(t[1], middle)
    return ((1 << last) - (1 << first)), aa + bb + [((1 << last) - (1 << first))], last

def histogram(t):
    _, x, middle = edge_masks(t[0], 0)
    _, y, last = edge_masks(t[1], middle)
    edges = x + y  # root has no incoming edge
    hist = [0] * (2 * last - 1)
    for surviving in range(1 << last):
        score = sum(1 for e in edges if surviving & e)
        hist[score] += 1
    return hist

hA, hB = histogram(A), histogram(B)
diff = {i: a - b for i, (a, b) in enumerate(zip(hA, hB)) if a != b}
assert diff == {5: 1, 6: -7, 7: 17, 8: -15, 9: -1, 10: 7, 11: -1, 12: -1}, diff
assert [sum((hA[k] - hB[k]) * k**r for k in range(len(hA))) for r in range(4)] == [0, 0, 0, -24]
print('q=1/2 histogram difference counts:', diff)

# Third raw-moment polynomial: independent recursive integer-polynomial
# arithmetic instead of the above edge-covariance formula.
def plus(*ps):
    r = [0] * max(map(len, ps))
    for p in ps:
        for i, x in enumerate(p):
            r[i] += x
    return tuple(r)

def prod(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i+j] += x*y
    return tuple(r)

def mulc(a, c):
    return tuple(c * x for x in a)

@lru_cache(None)
def incoming_moments(t):
    """Raw moments 0..3 of the subtree including its incoming edge."""
    if t == ():
        return ((1,), (1,-1), (1,-1), (1,-1))
    a, b = incoming_moments(t[0]), incoming_moments(t[1])
    n = edge_profile(t)[0]
    ans = [(1,)]
    for r in range(1, 4):
        # If Z=sum of two independent child contributions,
        # incoming contribution is Z + 1[Z>0].
        terms = []
        for k in range(r+1):
            for j in range(k+1):
                terms.append(mulc(prod(a[j], b[k-j]), comb(r, k)*comb(k,j)))
        terms.append((0,)*n+(-1,))
        ans.append(plus(*terms))
    return tuple(ans)

def root_third(t):
    a,b = incoming_moments(t[0]),incoming_moments(t[1])
    return plus(*(mulc(prod(a[j], b[3-j]), comb(3,j)) for j in range(4)))

lhs = root_third(A)
rhs = root_third(B)
delta = plus(lhs, mulc(rhs, -1))
want = (0,)*12 + (-6,12,-6)
assert delta[:len(want)] == want and all(x == 0 for x in delta[len(want):]), delta
print('raw third moment polynomial difference = -6*q^12*(1-q)^2')
print('ALL EXACT CHECKS PASSED')

# Exact bivariate generating-function identity in both q and z, not merely
# a check at one extinction probability. Sparse exponent pairs (q-degree,
# z-degree) are used so this calculation also has no symbolic dependency.
def bp(*terms):
    out = {}
    for coefficient, iq, iz in terms:
        out[iq, iz] = out.get((iq,iz), 0) + coefficient
    return {key:value for key,value in out.items() if value}

def badd(*polys):
    out = {}
    for pp in polys:
        for key, value in pp.items():
            out[key] = out.get(key,0)+value
    return {key:value for key,value in out.items() if value}

def bscale(pp, c):
    return {key:value*c for key,value in pp.items() if value*c}

def bmul(aa, bb):
    out = {}
    for (i,j), x in aa.items():
        for (k,l), y in bb.items():
            key = (i+k,j+l)
            out[key] = out.get(key,0)+x*y
    return {key:value for key,value in out.items() if value}

Q = bp((1,1,0))
Z = bp((1,0,1))
ONEB = bp((1,0,0))
FLEAF = badd(Q,bmul(badd(ONEB,bscale(Q,-1)),Z))

@lru_cache(None)
def generating_incoming(t):
    if t==():return FLEAF
    n=edge_profile(t)[0]
    zero = bp((1,n,0))
    return badd(zero,bmul(Z,badd(bmul(generating_incoming(t[0]),generating_incoming(t[1])),bscale(zero,-1))))

FC = generating_incoming(C4)
FB = generating_incoming(B4)
D = badd(FC,bscale(FB,-1))
factored_D = bmul(bp((1,2,2)),
           bmul(badd(Q,bscale(ONEB,-1)),
           bmul(badd(Z,bscale(ONEB,-1)),
           bp((1,1,2),(-2,1,1),(1,1,0),(-1,0,2)))))
assert D == factored_D

def generating_root(t):
    return bmul(generating_incoming(t[0]),generating_incoming(t[1]))

actual = badd(generating_root(A),bscale(generating_root(B),-1))
predicted = bmul(bp((1,8,0)), bmul(Z, bmul(badd(ONEB,bscale(Z,-1)),bmul(D,D))))
assert actual == predicted
coefficient_at_5 = {qdegree:coeff for (qdegree,zdegree),coeff in actual.items() if zdegree==5}
assert coefficient_at_5 == {14:1,15:-2,16:1}, coefficient_at_5
print('full bivariate generating-function factorization and probability at score five: verified')
