"""Standalone checks of a nonregular tetrahedral example and sharpness witnesses.
The global geometric theorem rests on the written proof, not finite sampling.
"""
import math
import random

signs = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
# Here the order of signs is chosen consistently with an even number of minus signs.
u = [tuple(a * x / 3 for a, x in zip((2, 2, 1), s)) for s in signs]
normal = [tuple(-a * x / math.sqrt(6) for a, x in zip((1, 1, 2), s)) for s in signs]
h = 2 / (3 * math.sqrt(6))
rho = h / math.sqrt(1 - h*h)
M = 1 / (2*math.sqrt(1-h*h))

def dot(x, y): return sum(a*b for a,b in zip(x,y))
def norm(x): return math.sqrt(dot(x,x))
def dist(x,y): return norm(tuple(a-b for a,b in zip(x,y)))

def support(w): return max(dot(w, ui) for ui in u)

for i in range(4):
    assert abs(norm(u[i])-1)<1e-12
    assert abs(norm(normal[i])-1)<1e-12
    for j in range(4):
        assert abs(dot(u[i], normal[j]) - (h if i != j else -3*h)) < 1e-12
    assert abs(support(normal[i])-h)<1e-12
assert abs(h*h - 2/27) < 1e-12
assert abs(M*M - 27/100) < 1e-12
assert 0 < h < 1/2

# An inner homothet of an optimal ball is feasible by convexity.
for j in range(4):
    center = tuple(M*x for x in normal[j])
    c_j = tuple(2*x for x in center)
    assert abs(norm(c_j)/2 - M)<1e-12
    for s in (0.001,0.01,0.1):
        near = tuple((1-s)*x for x in center)
        d = min(dist(near, tuple(M*x for x in nj)) for nj in normal)
        assert abs(d - s*M)<1e-12

# Finite checks only: not used as a proof of global positivity of kappa.
rng = random.Random(26261118)
checked = 0
for j in range(4):
    for _ in range(5000):
        v = [rng.gauss(0,1) for _ in range(3)]
        v = [x/norm(v) for x in v]
        w = [(1-0.005)*x+0.005*y for x,y in zip(normal[j],v)]
        w = [x/norm(w) for x in w]
        gap = support(w)-h
        assert gap >= -1e-12, (j,w,gap)
        checked += 1
print('PASS tetrahedral facet data, radius, sharpness witnesses;',checked,'support samples')
