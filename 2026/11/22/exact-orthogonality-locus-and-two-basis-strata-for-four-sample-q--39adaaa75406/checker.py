"""Exact supplementary checks for four-sample quadratic-phase orthogonality.

Requires only Python 3 standard library. All equalities use rational arithmetic;
finite samples are diagnostics and not a substitute for the classification proof.
"""
from fractions import Fraction as F
from itertools import combinations, product


def plus(a, b):
    return (a[0]+b[0], a[1]+b[1])


def minus(a, b):
    return (a[0]-b[0], a[1]-b[1])


def mul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def conj(a):
    return (a[0], -a[1])


def power(a, n):
    v = ONE
    for _ in range(n):
        v = mul(v, a)
    return v


ZERO = (F(0), F(0))
ONE = (F(1), F(0))
NEG = (F(-1), F(0))
I = (F(0), F(1))
NI = (F(0), F(-1))


def v(r, t):
    return (ONE, r, mul(r,t), power(t,3))


def inner(a,b):
    s=ZERO
    for x,y in zip(a,b):
        s=plus(s,mul(conj(x),y))
    return s


def check_basis(pairs):
    vec=[v(r,t) for r,t in pairs]
    for i,j in product(range(4),repeat=2):
        assert inner(vec[i],vec[j])==(F(4),F(0)) if i==j else inner(vec[i],vec[j])==ZERO


def rational_circle(p,q):
    # Dense rational parametrization of the unit circle.
    assert p or q
    d=p*p+q*q
    return (F(p*p-q*q,d), F(2*p*q,d))


samples=set()
for p in range(-6,7):
    for q in range(-6,7):
        if p or q:
            samples.add(rational_circle(p,q))
for z in samples:
    pairs=((ONE,ONE),(NEG,ONE),(z,NEG),(mul(NEG,z),NEG))
    check_basis(pairs)
    assert inner(v(ONE,ONE),v(z,NEG))==ZERO
    assert inner(v(ONE,ONE),v(mul(NEG,z),NEG))==ZERO

cyclic=((ONE,ONE),(I,I),(NEG,NEG),(NI,NI))
check_basis(cyclic)

# Exact fourth-root grid census of every maximal orthogonal set.
phases=(ONE,I,NEG,NI)
vertices=tuple(product(phases,repeat=2))


def is_zero_ratio(a,b):
    return inner(v(*a),v(*b))==ZERO

edges=sum(is_zero_ratio(a,b) for a,b in combinations(vertices,2))
bases=[]
for four in combinations(vertices,4):
    if all(is_zero_ratio(a,b) for a,b in combinations(four,2)):
        bases.append(four)


def mulpair(a,b):
    return (mul(a[0],b[0]),mul(a[1],b[1]))


def inverse(z):
    return conj(z)


def normalized_type(four):
    # Translation in the phase torus, then comparison up to column ordering.
    for a in four:
        red=set((mul(x[0],inverse(a[0])),mul(x[1],inverse(a[1]))) for x in four)
        for z in phases:
            first={(ONE,ONE),(NEG,ONE),(z,NEG),(mul(NEG,z),NEG)}
            if red==first:
                return 'continuous'
        if red==set(cyclic):
            return 'isolated'
    raise AssertionError(f"Unclassified exact four-chirp basis: {four}")

kinds={'continuous':0,'isolated':0}
for four in bases:
    kinds[normalized_type(four)]+=1
assert sum(kinds.values())==len(bases)
assert kinds['continuous'] and kinds['isolated']

# Check the zero-difference classification for the full discrete grid.
E=lambda p: (p[1]==NEG or p in {(NEG,ONE),(I,I),(NI,NI)})
for r,t in vertices:
    assert (inner(v(ONE,ONE),v(r,t))==ZERO)==E((r,t))

print('PASS: exact rational-unit-circle continuous-family tests',len(samples))
print('PASS: isolated cyclic basis and exact phase-zero grid',len(vertices))
print('PASS: exhaustive fourth-root grid basis classification',len(bases),kinds)
print('PASS: full fourth-root pair graph edges',edges)
