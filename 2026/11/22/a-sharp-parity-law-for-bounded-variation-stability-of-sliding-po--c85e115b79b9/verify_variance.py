"""Reproducible finite checks for the sliding population-variance theorem.

Run with Python 3.9+; no third-party packages required.
The mathematical argument in RESULT.md covers arbitrary window length.
"""
from itertools import product
from fractions import Fraction
from random import Random


def moving_variance(x, m):
    return [sum((v - sum(x[i:i+m])/m)**2 for v in x[i:i+m])/m
            for i in range(len(x)-m+1)]


def tv(x):
    return sum(abs(b-a) for a,b in zip(x,x[1:]))


def step_derivative_raw(bits, m, j):
    """Integer h = m*m/2 times the derivative of a window variance."""
    n = len(bits)
    vals = []
    for i in range(n-m+1):
        right = [v for p,v in enumerate(bits[i:i+m],start=i) if p>j]
        left = [v for p,v in enumerate(bits[i:i+m],start=i) if p<=j]
        vals.append(len(left)*sum(right)-len(right)*sum(left))
    return vals


for m in range(2,9):
    # The maximum over a cube of a convex function occurs at a vertex.
    exact = 2*(m*m//4)
    worst = 0
    for L_R in product((0,1), repeat=2*m-2):
        left = L_R[:m-1]
        right = L_R[m-1:]
        h = [0]+[(m-k)*sum(right[:k])-k*sum(left[:m-k])
                 for k in range(1,m)]+[0]
        worst = max(worst, tv(h))
    assert worst == exact, (m, worst, exact)
print('EXHAUSTIVE_BINARY_CHAMBERS_PASS m=2..8')

for m in range(2,19):
    for signs in product((-1,1),repeat=m):
        r = signs.count(1)
        alpha = [(m-b)*signs[b-1]-sum(signs[b:]) for b in range(1,m)]
        beta = [(k-1)*signs[k-1]-sum(signs[:k-1]) for k in range(2,m+1)]
        maximum = sum(max(0,c) for c in alpha+beta)
        assert maximum == 2*r*(m-r), (m,signs,maximum)
print('SIGN_PAIR_DUAL_IDENTITY_PASS m=2..18')

for m in range(2,81):
    k=m//2
    h=[0]+[(m-t)*min(t,k) for t in range(1,m)]+[0]
    assert tv(h)==2*(m*m//4)
print('EXACT_SHARPNESS_STEP_WITNESSES_PASS m=2..80')

rng=Random(11311)
for m in range(2,12):
    target=Fraction(4*(m*m//4),m*m)
    for _ in range(330):
        n=2*m+rng.randrange(6)
        x=[rng.random() for _ in range(n)]
        y=[rng.random() for _ in range(n)]
        v=tv([a-b for a,b in zip(x,y)])
        actual=tv([a-b for a,b in zip(moving_variance(x,m),moving_variance(y,m))])
        assert actual <= float(target)*v+1e-11, (m,n,actual,v)
print('RANDOM_TWO_INPUT_VARIATION_INEQUALITY_PASS cases=3300')

for m in range(2,42):
    n=2*m
    j=m-1
    baseline=[0.0]*n
    for p in range(m,m+m//2):
        baseline[p]=1.0
    eps=1e-5
    mid=[eps+(1-2*eps)*v for v in baseline]
    d=eps
    x=[v+(d/2 if i>j else 0) for i,v in enumerate(mid)]
    y=[v-(d/2 if i>j else 0) for i,v in enumerate(mid)]
    assert min(x+y)>=0 and max(x+y)<=1
    ratio=tv([a-b for a,b in zip(moving_variance(x,m),moving_variance(y,m))])/tv([a-b for a,b in zip(x,y)])
    assert abs(ratio-4*(m*m//4)/m**2)<1e-4, (m,ratio)
print('FINITE_PAIR_LIMITING_SHARPNESS_PASS m=2..41')
print('ALL_SLIDING_VARIANCE_CHECKS_PASS')
