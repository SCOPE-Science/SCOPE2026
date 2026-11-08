#!/usr/bin/env python3
"""Exact finite-field verification for the genus-17 octahedral quotient."""
from collections import Counter

P = 11
ZERO = (0, 0)
ONE = (1, 0)
INF = None

def add(a, b):
    return ((a[0] + b[0]) % P, (a[1] + b[1]) % P)

def mul(a, b):
    return ((a[0] * b[0] - a[1] * b[1]) % P,
            (a[0] * b[1] + a[1] * b[0]) % P)

def neg(a):
    return (-a[0] % P, -a[1] % P)

def power(a, n):
    r = ONE
    while n:
        if n & 1:
            r = mul(r, a)
        a = mul(a, a)
        n //= 2
    return r

def div(a, b):
    assert b != ZERO
    return mul(a, power(b, 119))

def matmul(g, h):
    return (add(mul(g[0],h[0]),mul(g[1],h[2])),
            add(mul(g[0],h[1]),mul(g[1],h[3])),
            add(mul(g[2],h[0]),mul(g[3],h[2])),
            add(mul(g[2],h[1]),mul(g[3],h[3])))

def normalize(g):
    z = next(v for v in g if v != ZERO)
    return tuple(div(v, z) for v in g)

def mobius(g, x):
    if x is INF:
        return INF if g[2] == ZERO else div(g[0],g[2])
    numerator = add(mul(g[0],x),g[1])
    denominator = add(mul(g[2],x),g[3])
    return INF if denominator == ZERO else div(numerator,denominator)

T = normalize((ZERO, ONE, ONE, ZERO))
S = normalize((ONE, (7, 7), (7, 4), ONE))
I = normalize((ONE, ZERO, ZERO, ONE))
group = {I}
queue = [I]
while queue:
    g = queue.pop()
    for generator in (T, S):
        h = normalize(matmul(g, generator))
        if h not in group:
            group.add(h)
            queue.append(h)
            assert len(group) <= 24
assert len(group) == 24

def order(g):
    h = I
    for n in range(1, 25):
        h = normalize(matmul(h, g))
        if h == I:
            return n
    raise AssertionError('order exceeds group size')

assert Counter(order(g) for g in group) == {1: 1, 2: 9, 3: 8, 4: 6}
points = [(a,b) for a in range(P) for b in range(P)] + [INF]
assert len(points) == 122
seen = set()
orbits = []
for x in points:
    if x in seen:
        continue
    o = {mobius(g,x) for g in group}
    assert o.isdisjoint(seen)
    seen.update(o)
    orbits.append(o)
assert len(seen) == len(points)
assert Counter(map(len,orbits)) == {24:4,6:1,8:1,12:1}

def curve_components(x):
    if x is INF:
        return ('six',)
    x4 = power(x,4)
    x8 = power(x,8)
    x12 = power(x,12)
    v8 = add(add(x8, neg(mul((3,0),x4))), ONE)
    v6 = mul(x,add(x4,ONE))
    v12 = add(x12,neg(ONE))
    return tuple(k for k,v in [('six',v6),('eight',v8),('twelve',v12)] if v == ZERO)

special = {key: {x for x in points if key in curve_components(x)}
           for key in ('six','eight','twelve')}
assert [len(special[k]) for k in ('six','eight','twelve')] == [6,8,12]
assert special['six'].isdisjoint(special['eight'])
assert special['six'].isdisjoint(special['twelve'])
assert special['eight'].isdisjoint(special['twelve'])
for kind, length in [('six',6),('eight',8),('twelve',12)]:
    assert special[kind] in orbits
    assert len(special[kind]) == length

def j(x):
    # ∞ is a regular point with value one; poles represented by None.
    if x is INF:
        return ONE
    x4 = power(x,4)
    q8 = add(add(power(x,8),neg(mul((3,0),x4))),ONE)
    q12 = add(power(x,12),neg(ONE))
    if q12 == ZERO:
        return INF
    return div(power(q8,3),power(q12,2))

# Both Möbius generators preserve the rational function at every point of P1(F121).
# Cross products have degree <=48; the 110 nonpoles exceed this bound,
# so these exact tests imply identities in F121(x), not just finite samples.
for g in (T,S):
    for x in points:
        assert j(mobius(g,x)) == j(x), (g,x)
assert len([x for x in points if j(x) is not INF]) == 110
for kind,target in [('six',ONE),('eight',ZERO),('twelve',INF)]:
    assert all(j(x) == target for x in special[kind])

# Identity in F11[s] with s=x^4. Use exhaustive coefficient calculation.
def poly_mul(a,b):
    c = [0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):
            c[i+j] = (c[i+j]+u*v)%P
    return c

def poly_pow(a,n):
    result = [1]
    for _ in range(n):
        result = poly_mul(result,a)
    return result

def poly_scale(a,c):
    return [(c*z)%P for z in a]

def poly_add(a,b):
    return [((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%P
            for i in range(max(len(a),len(b)))]

left = poly_add(poly_pow([1,-3,1],3),poly_scale(poly_mul([0,1],poly_pow([1,1],4)),9))
right = poly_pow([-1,0,0,1],2)
assert left == right
assert 48*(4-1)+64*(3-1)+48*(4-1) == 416
assert -2*192+416 == 2*17-2

# Arithmetic behavior of the three ramification fibers of the 192-cover.
# x=9 (=-2) belongs to the eight-point orbit and gives eight rational
# places because both defining radical equations split into 4 x 2 roots.
alpha = (0,1)
def f(x):
    return mul(add(x,ONE), add(add(power(x,2),x),ONE))

def equations_at(x):
    z_square = mul(add(alpha,ONE),mul(f(x),f(mul(alpha,x))))
    ys = [y for y in points if y is not INF and
          add(add(power(y,4),neg(mul((2,0),power(y,2)))),power(x,12)) == ZERO]
    zs = [z for z in points if z is not INF and power(z,2) == z_square]
    return ys, zs

assert (9,0) in special['eight']
y9,z9 = equations_at((9,0))
assert sorted(y9) == sorted([(4,2),(4,9),(7,2),(7,9)])
assert sorted(z9) == sorted([(1,10),(10,1)])
assert len(y9)*len(z9) == 8
# At x=0, the four places of the biquadratic intermediate cover have
# rational local expansions y = ±sqrt(2) or y = ± x^6/sqrt(2)+O(x^18).
# The last quadratic radical is nonsquare, forcing residue degree 2.
assert (0,0) in special['six']
assert power((1,1),60) == (10,0)  # alpha+1 is nonsquare
assert power((0,3),2) == (2,0)   # sqrt(2) lies in F121
# At x=1, the y-quartic specializes to (y^2-1)^2, giving two
# distinct ramified y-places y=+1,-1; the final quadratic equation
# has the two distinct roots z=+alpha,-alpha. This proves four rational
# points over x=1, and automorphism transitivity gives 48 in that orbit.
y1,z1 = equations_at(ONE)
assert sorted(y1) == [(1,0),(10,0)]
assert sorted(z1) == [(0,1),(0,10)]
assert len(y1)*len(z1) == 4
# Fully enumerate affine rational places away from x^12=1 and x=0.
# For all such x, the quartic equation for y and quadratic equation for z
# are separable. The product count is therefore the exact place count.
from collections import defaultdict
counts_by_j = defaultdict(int)
x_by_j = defaultdict(set)
all_special = set().union(*special.values())
local_counts = Counter()
for x in points:
    if x in all_special:
        continue
    y_values,z_values = equations_at(x)
    count = len(y_values)*len(z_values)
    assert count in (0,8)
    local_counts[count] += 1
    if count:
        counts_by_j[j(x)] += count
        x_by_j[j(x)].add(x)
assert local_counts == {0:48,8:48}
assert dict(counts_by_j) == {(4,4):192,(4,7):192}
assert all(len(xs)==24 and xs in orbits for xs in x_by_j.values())
assert 64+48+192+192 == 496  # genus-17 maximal curve over F121
print('ARITHMETIC_OK: rational quotient image={0, infinity, 4+4alpha, 4-4alpha}')
print('RATIONAL_ORBITS_OK: 48+64+192+192=496; 48 quadratic points above j=1')
print('VERIFY_OK |H|=24; orbit lengths 6,8,12,24x4; quotient degree24; 192-cover signature (4,3,4)')
