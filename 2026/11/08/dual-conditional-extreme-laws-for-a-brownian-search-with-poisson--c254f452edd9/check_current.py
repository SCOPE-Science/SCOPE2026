"""Deterministic diagnostics for stopped Brownian maximum and reset counts.

Run: python3 check_current.py
Uses only the Python standard library. Finite tests do not certify limits.
"""
import math

checks = 0

def close(x, y, tol=2e-10):
    global checks
    checks += 1
    assert math.isfinite(x) and math.isfinite(y) and abs(x-y) <= tol * (1 + abs(y)), (x,y)

def probabilities(z, L):
    assert 0 < z < L
    a = math.sinh(L-z) / math.sinh(L)
    b = math.sinh(z) / math.sinh(L)
    c = 1.0-a-b
    return a,b,c

for z in (0.15, 0.4, 0.8, 1.3, 2.5):
    p = math.exp(-z)
    q = -math.expm1(-z)
    for gap in (0.15, 0.4, 1.0, 2.0, 4.0, 8.0):
        L = z + gap
        a,b,c = probabilities(z,L)
        close(a+b+c,1)
        assert a > 0 and b > 0 and c > 0
        close(sum(a*c**n for n in range(250)),(a/(a+b))*(1-c**250))
        close(sum(p*q**n for n in range(250)),1-q**250)
        close(b/(a+b), 1-a/(1-c))
        close(sum((1-c)*c**n for n in range(250)),1-c**250)
        for n in range(16):
            close((a*c**n)/(p*q**n), (a/p)*(c/q)**n)
            close((a*c**n)/(a/(a+b)), (a+b)*c**n)
            joint_tail=p*q**n-a*c**n
            assert joint_tail>=-3e-14

# High-max posterior tends to the size-biased geometric distribution.
for z in (0.25,0.7,1.5):
    p=math.exp(-z)
    q=-math.expm1(-z)
    for L in (12.0,16.0,20.0):
        a,b,c=probabilities(z,L)
        tail=b/(a+b)
        close(sum((p*q**n-a*c**n) for n in range(250)),1-q**250-(a/(a+b))*(1-c**250),3e-9)
        for n in range(1,9):
            posterior=(p*q**n-a*c**n)/tail
            target=n*p*p*q**(n-1)
            assert abs(posterior-target)<0.003, (z,L,n,posterior,target)

# Gumbel profile when conditioned on a growing reset count.
for z in (0.25,0.8,1.7):
    p=math.exp(-z);q=1-p
    for n in (2000,20000):
        for y in (-1.5,-0.25,0,0.75,2.0):
            L=math.log(n)+math.log1p(math.exp(z))+y
            a,b,c=probabilities(z,L)
            cdf=(a/p)*(c/q)**n
            target=math.exp(-math.exp(-y))
            assert abs(cdf-target)<0.0015,(z,n,y,cdf,target)

# Singular weak-reset limit: large maximum selects zero or one reset.
for u in (0.3,1.0,2.4):
    for z in (0.003, 0.0003):
        p=math.exp(-z);q=1-p
        a,b,c=probabilities(z,u)
        tail=b/(a+b)
        posterior0=(p-a)/tail
        posterior1=(p*q-a*c)/tail
        assert abs(posterior0-math.exp(-u))<0.005
        assert abs(posterior1-(1-math.exp(-u)))<0.025
        assert abs(tail/z-1/math.sinh(u))<0.025

print(f"PASS: {checks} exact-identity assertions plus conditional-limit diagnostic grids")
