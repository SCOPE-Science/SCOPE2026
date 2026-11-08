"""Exact finite-step checks for a two-type random affine Markov cocycle.

These computations support, but do not replace, the all-scale proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product

types = ((F(1), F(1)), (F(3), F(1)))  # (left-to-right, right-to-left) rates
m = F(1, 3)
lo, hi = F(1, 4), F(1, 2)

for eps in (F(1, 100), F(1, 50), F(1, 10), F(1, 5)):
    assert 0 < eps < F(1, 4)
    q = sum((1-eps*(a+b))**2 for a,b in types)/2
    stationary_variance = eps/(9*(6-10*eps))
    for n in range(1, 9):
        vals = []
        for seq in product(types, repeat=n):
            w=m
            for a,b in seq:
                w = (1-eps*(a+b))*w+eps*b
            vals.append(w)
        mean = sum(vals, F(0))/len(vals)
        variance = sum((v-m)**2 for v in vals)/len(vals)
        assert mean == m, (eps,n,mean)
        assert variance == stationary_variance * (1-q**n), (eps,n,variance)
        assert all(lo <= v <= hi for v in vals)
    assert max(abs(lo-m),abs(hi-m)) == F(1, 6)
    for a,b in types:
        u = b/(a+b)
        w=lo if u==hi else hi
        for _ in range(600):
            w=(1-eps*(a+b))*w+eps*b
        assert abs(w-u) <= (1-eps*(a+b))**600 * (hi-lo)
print('PASS: 2,040 exact enumerated finite-word states; 64 exact moment identities; four endpoint tests')
