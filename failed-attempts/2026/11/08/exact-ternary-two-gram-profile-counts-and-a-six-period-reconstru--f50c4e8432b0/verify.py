"""Independent integer-algebra and exhaustive finite checks for ternary 2-gram profiles.
This program certifies specified finite identities and test ranges, not the infinite proof.
"""
from itertools import product
from math import comb


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def plus(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a): c[i] += v
    for i, v in enumerate(b): c[i] += v
    return trim(c)


def neg(a): return tuple(-x for x in a)


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b): c[i+j] += u*v
    return trim(c)


class RationalSeries:
    def __init__(self, numerator=(1,), denominator=(1,)):
        self.p, self.q = trim(numerator), trim(denominator)
        assert self.q[0] == 1

    def __add__(self, other):
        return RationalSeries(plus(mul(self.p, other.q), mul(self.q, other.p)), mul(self.q, other.q))

    def __neg__(self):
        return RationalSeries(neg(self.p), self.q)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return RationalSeries(mul(self.p, other.p), mul(self.q, other.q))

    def equals(self, other):
        return mul(self.p, other.q) == mul(self.q, other.p)

    def series(self, max_deg):
        a = [0]*(max_deg+1)
        for k in range(max_deg+1):
            a[k] = ((self.p[k] if k < len(self.p) else 0)
                    - sum(self.q[j]*a[k-j] for j in range(1, min(k+1,len(self.q)))))
        return a

ONE = RationalSeries()
Z = RationalSeries((0,1))
Z2 = RationalSeries((0,0,1))
Z3 = RationalSeries((0,0,0,1))
L = RationalSeries((0,1), (1,-1))
C2 = RationalSeries((0,0,1), mul(mul((1,-1),(1,-1)), (1,0,-1)))
B = RationalSeries((1,0,0,1),mul(mul(mul((1,-1),(1,-1)),(1,-1)),mul(mul(mul((1,0,-1),(1,0,-1)),(1,0,-1)),(1,0,0,-1))))
H = RationalSeries((0,1,1), B.q)
J = RationalSeries((0,0,1),mul(mul(mul((1,-1),(1,-1)),(1,-1)),(1,0,-1)))
THREE = RationalSeries((3,))
SIX = RationalSeries((6,))
TARGET = RationalSeries((0,9,-12,5,19,-4,-10,-14,14,6,-9,3),
      mul(mul(mul(mul(mul(mul((1,-1),(1,-1)),(1,-1)),(1,-1)),(1,-1)),mul((1,-1),(1,-1))),mul(mul((1,1),(1,1)),(1,1,1))))
DERIVED = B - ONE - THREE*L*L - THREE*L*C2 - L*L*L + SIX*(H-J)
assert DERIVED.equals(TARGET), 'symbolic generating-function identity failed'
EXPECTED = [9,24,65,156,342,683,1272,2226,3708,5919,9120,13625]
assert TARGET.series(len(EXPECTED))[1:] == EXPECTED


def signature(word):
    out = [0]*9
    for a,b in zip(word,word[1:]): out[3*a+b]+=1
    return tuple(out)


def graph_realisable(counts):
    row = [sum(counts[3*i:3*i+3]) for i in range(3)]
    col = [sum(counts[i::3]) for i in range(3)]
    diff = [row[i]-col[i] for i in range(3)]
    if sorted(diff) not in ([0,0,0],[-1,0,1]):
        return False
    active = {i for i in range(3) if row[i]+col[i] > 0}
    if not active:
        return False
    reached = {next(iter(active))}
    while True:
        old = len(reached)
        for i in list(reached):
            for j in active:
                if counts[3*i+j] or counts[3*j+i]: reached.add(j)
        if len(reached)==old:break
    return reached == active


def nonnegative_compositions(m,k):
    if k==1:
        yield (m,)
    else:
        for v in range(m+1):
            for rest in nonnegative_compositions(m-v,k-1):
                yield (v,)+rest


for m in range(1,10):
    direct = {signature(word) for word in product(range(3),repeat=m+1)}
    flow = {cnt for cnt in nonnegative_compositions(m,9) if graph_realisable(cnt)}
    assert direct == flow, f'gap in Euler criterion at m={m}'
    assert len(direct) == EXPECTED[m-1], f'profile count at m={m}'
    print('m=',m,'profiles=',len(direct),'words=',3**(m+1),'candidate matrices=',comb(m+8,8))

# Test first dozen coefficients from a separate OGF power-series construction.
assert DERIVED.series(12)[1:] == EXPECTED
print('VERIFY_OK: symbolic identity, rational expansion, 9 exhaustive word/matrix checks')
