"""Supplementary numerical consistency checks for a sharp coordinatewise normalization bound.

All-dimensional validity follows from the accompanying analytic proof, not these finite tests.
Run: python verification.py
"""
from __future__ import annotations
import math
import random

SEED = 431992
rng = random.Random(SEED)
checks = 0

def check(condition: bool, label: str) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(f"check {checks}: {label}")

def optimum_ratio(n: int) -> float:
    assert n >= 2
    return max(1.0, (math.sqrt(8 * n + 1) - 3) / 4)

def sharp_bound(n: int, a: float, b: float) -> float:
    if n == 1 or a == b:
        return 0.0
    u = min(b / a, optimum_ratio(n))
    return (n - 1) * (1 + u) / (a * (n - 1 + u * u) ** 1.5)

def normalize(x):
    q = math.sqrt(sum(z*z for z in x))
    return [z/q for z in x]

def matrix_jac(x):
    S = sum(z*z for z in x)
    q = math.sqrt(S)
    return [[(int(i==j) - x[i]*x[j]/S)/q for j in range(len(x))] for i in range(len(x))]

def local_modulus(x):
    return max(sum(abs(z) for z in row) for row in matrix_jac(x))

def scalar_profile(n, a, u):
    scale = a if u >= 1 else a / u
    m = n-1
    return m*(1+u)/(scale*(m+u*u)**1.5)

# The candidate scalar optimiser and all dimensional transition cases.
for n in range(2, 71):
    q=optimum_ratio(n)
    check(q == 1.0 if n <= 6 else q > 1.0, 'dimension-seven threshold')
    if n >= 7:
        check(abs(2*q*q+3*q-(n-1)) < 1e-11*n, 'critical point identity')
    for a in (0.3, 1.0, 2.6):
        for contrast in (1.001, 1.1, 1.6, 3.0, 10.0, 100.0):
            b=a*contrast
            v=min(contrast,q)
            predicted=sharp_bound(n,a,b)
            # Scalar candidates on either side of the equal-level transition.
            for j in range(81):
                u=1/contrast + (contrast-1/contrast)*j/80
                check(scalar_profile(n,a,u) <= predicted*(1+1e-12), 'scalar upper bound')
            # Interior approximation to all-boundary extremising vector.
            delta=min(a*2e-5, (b-a)/200)
            low=a+delta
            high=min(b-delta, a*v)
            if high < low:
                high=low
            x=[high]+[low]*(n-1)
            observed=local_modulus(x)
            check(observed <= predicted*(1+1e-12), 'Jacobian bound near extremiser')
            check(observed >= predicted*(1-7e-4), 'Jacobian sharpness witness')
            if n<=16:
                h=delta/20
                d=[1]+[-1]*(n-1)
                xp=[z+h*di for z,di in zip(x,d)]
                xm=[z-h*di for z,di in zip(x,d)]
                check(min(xm) >= a and max(xp) <= b, 'feasible finite difference')
                ratio=max(abs(vv-ww) for vv,ww in zip(normalize(xp),normalize(xm)))/(2*h)
                check(ratio <= predicted*(1+4e-8), 'finite difference upper bound')
                check(ratio >= predicted*(1-1e-3), 'finite difference lower witness')

# Random Jacobian and full two-input tests on the complete convex box.
for n in range(2, 34):
    for _ in range(160):
        a = 10**rng.uniform(-1.5,1.5)
        b = a * 10**rng.uniform(.01,2)
        x=[rng.uniform(a,b) for _ in range(n)]
        y=[rng.uniform(a,b) for _ in range(n)]
        L=sharp_bound(n,a,b)
        check(local_modulus(x) <= L*(1+2e-12), 'random Jacobian')
        fx=normalize(x)
        fy=normalize(y)
        gap=max(abs(z-w) for z,w in zip(fx,fy))
        distance=max(abs(z-w) for z,w in zip(x,y))
        check(gap <= L*distance*(1+2e-12), 'random input pair')
        # Exact row sum sign identity, independent of the matrix row norm code.
        S=sum(z*z for z in x)
        Q=math.sqrt(S)
        for i in (0,n-1):
            T=S-x[i]*x[i]
            H=sum(x[j] for j in range(n) if j!=i)
            identity=(T+x[i]*H)/(S*Q)
            check(abs(identity-sum(abs(z) for z in matrix_jac(x)[i])) < 1e-9, 'row sum identity')

# Cauchy equality mechanism for the off-distinguished block.
for n in range(2,100):
    m=n-1
    z=[rng.uniform(0.05,50) for _ in range(m)]
    H=sum(z)
    T=sum(v*v for v in z)
    check(H*H <= m*T*(1+1e-12), 'off-coordinate Cauchy')
    c=math.sqrt(T/m)
    check(abs(sum([c]*m)**2-m*sum(v*v for v in [c]*m))<1e-7*m*T, 'equal-tail equality')

# High-dimensional contrast limit, two asymptotic regimes.
for n in (2000, 4000, 8000, 20000):
    q=optimum_ratio(n)
    k=0.8
    L=sharp_bound(n,1.0,k*math.sqrt(n))
    check(abs(L-2/(3*math.sqrt(3))) < 0.025, 'high-contrast asymptotic')
    check(abs(sharp_bound(n,1.0,3)*math.sqrt(n)-4) < 0.2, 'fixed contrast asymptotic')

check(sharp_bound(1,1.0,100.0) == 0.0, 'dimension-one constant map')
check(sharp_bound(6,1.0,1.0) == 0.0, 'singleton boundary')
print(f'VERIFY_OK {checks} deterministic mathematical assertions')
