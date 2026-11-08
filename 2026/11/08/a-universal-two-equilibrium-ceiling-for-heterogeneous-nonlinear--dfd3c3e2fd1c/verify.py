"""Exact polynomial checks for a three-size nonlinear public-goods mixture.

Requires Python 3.9+ only. The general all-size theorem is analytic, not certified
by the finite tests performed here.
"""
from fractions import Fraction as Q
from random import Random


def padd(a, b):
    c = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a): c[i] += x
    for i, x in enumerate(b): c[i] += x
    return c


def pmul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i + j] += x * y
    return c


def pscale(a, s): return [x * s for x in a]


def ppow(a, n):
    out = [Q(1)]
    for _ in range(n): out = pmul(out, a)
    return out


def val(p, x): return sum(c * x**i for i, c in enumerate(p))


def gain(weight, size, delta):
    return pscale(ppow([Q(1), delta - 1], size - 1), weight / size)


def mixture(data):
    polynomial = [Q(0)]
    for w, size, d in data:
        polynomial = padd(polynomial, gain(w, size, d))
    return polynomial


sample = [(Q(1,2), 2, Q(1,4)),
          (Q(1,4), 3, Q(2)),
          (Q(1,4), 4, Q(1,2))]
G = mixture(sample)
assert G == [Q(19,48), -Q(11,96), Q(25,192), -Q(1,128)]
# rG-1 = -(3u-2)(u^2-16u+4)/144.
R = padd(pscale(G, Q(8,3)), [-Q(1)])
expected = pscale(pmul([-Q(2), Q(3)], [Q(4), -Q(16), Q(1)]), -Q(1,144))
assert R == expected
assert val(R,Q(0))>0 and val(R,Q(1,2))<0 and val(R,Q(1))>0
assert val(R,Q(2,3))==0
assert val(G,Q(1,2)) == Q(379,1024)
assert val(G,Q(0)) == Q(19,48)
assert val(G,Q(1)) == Q(155,384)
# The second derivative on [0,1] equals 25/96 - 3u/64 > 0.
assert Q(25,96)-Q(3,64)>0

# Exact sampled convexity checks across mixtures, with varying discount and synergy.
# Finite tests detect algebraic errors; they do not prove the infinite-family theorem.
rng = Random(6192026)
checked = 0
for n in range(1, 9):
    for _ in range(80):
        raw = [rng.randint(1, 12) for __ in range(n)]
        total = sum(raw)
        options = [Q(1,8),Q(1,4),Q(1,2),Q(1),Q(5,4),Q(2),Q(3)]
        data = [(Q(a,total),rng.randint(2,9),rng.choice(options)) for a in raw]
        p = mixture(data)
        x = Q(rng.randint(0,10),10)
        y = Q(rng.randint(0,10),10)
        lam = Q(rng.randint(0,10),10)
        z = lam*x+(1-lam)*y
        assert val(p,z) <= lam*val(p,x)+(1-lam)*val(p,y)
        checked += 1
print('Exact example and', checked, 'rational convexity tests passed.')
