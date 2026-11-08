"""Exact finite-rational consistency checks for the sharp l1 metric-selection theorem."""
from fractions import Fraction as F
from itertools import product
from random import Random

checks = 0

def require(condition):
    global checks
    if not condition:
        raise AssertionError('rational consistency check failed')
    checks += 1


def norm1(x):
    return sum(map(abs, x), F(0))


def project(x, r=F(1)):
    if norm1(x) <= r:
        return tuple(x)
    magnitudes = sorted((abs(u) for u in x), reverse=True)
    acc = F(0)
    tau = None
    for k, m in enumerate(magnitudes, 1):
        acc += m
        candidate = (acc-r)/k
        next_m = magnitudes[k] if k < len(magnitudes) else F(0)
        if next_m <= candidate < m:
            tau = candidate
            break
    assert tau is not None and tau > 0
    return tuple((1 if u > 0 else -1 if u < 0 else 0) * max(abs(u)-tau, F(0)) for u in x)


def witness(n):
    b = tuple(F(1,n) for i in range(n))
    e = F(1, 3*n)
    x = tuple(b[i] + (e if i == 0 else 0) for i in range(n))
    ys = [b]
    ys += [tuple(b[i] + (e if i == 0 else (-e if i == j else 0)) for i in range(n)) for j in range(1,n)]
    # The sharp optimal selector is forced to realize the minimax threshold.
    q = tuple(F(n-1,n) if i == 0 else -F(1,n) for i in range(n))
    require(norm1(x) == 1+e)
    require(sum(q) == 0)
    require(norm1(tuple(x[i] - (b[i]+e*q[i]) for i in range(n))) == e)
    for y in ys:
        require(norm1(y) == 1)
        require(norm1(tuple(x[i]-y[i] for i in range(n))) == e)
        require(norm1(tuple((b[i]+e*q[i])-y[i] for i in range(n))) == e*F(2*n-2,n))
    return x, ys

rnd = Random(20261102)
for n in range(1,9):
    constant = F(1) if n < 2 else F(2*n-2,n)
    for k in range(2,n+1):
        column_sum = F(k-1,k) + (k-1)*F(1,k)
        require(column_sum == F(2*k-2,k))
        require(column_sum <= constant)
    if n > 1:
        witness(n)
    for _ in range(260):
        x = tuple(F(rnd.randint(-30,30),10) for _ in range(n))
        y = tuple(F(rnd.randint(-30,30),10) for _ in range(n))
        px,py = project(x),project(y)
        require(norm1(px) <= 1)
        require(norm1(py) <= 1)
        require(norm1(tuple(x[i]-px[i] for i in range(n))) == max(norm1(x)-1,0))
        require(norm1(tuple(y[i]-py[i] for i in range(n))) == max(norm1(y)-1,0))
        require(norm1(tuple(px[i]-py[i] for i in range(n))) <= constant*norm1(tuple(x[i]-y[i] for i in range(n))))
    # Explicit full-dimensional active cell with column perturbation.
    if n >= 2:
        z = tuple(F(1,n)+F(2) for _ in range(n))
        z1 = tuple(z[i] + (F(1,100) if i == 0 else 0) for i in range(n))
        pz,pz1 = project(z),project(z1)
        require(norm1(tuple(pz[i]-pz1[i] for i in range(n))) == constant*F(1,100))

print('L1_METRIC_SELECTION_SHARP_OK',checks)
