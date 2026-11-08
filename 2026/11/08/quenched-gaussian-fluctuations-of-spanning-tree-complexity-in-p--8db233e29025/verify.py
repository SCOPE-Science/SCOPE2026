#!/usr/bin/env python3
"""Independent finite checks of the stated threshold-graph spanning-tree formulas.

Standard-library only. Finite checks supplement, never replace, the proof.
"""
from itertools import product
import math
import random

checks = 0

def check(ok, message):
    global checks
    if not ok:
        raise AssertionError(message)
    checks += 1


def det_bareiss(matrix):
    """Exact integer determinant by fraction-free elimination."""
    a = [list(r) for r in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign, prev = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k+1, n) if a[j][k] != 0), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                val = a[i][j]*pivot - a[i][k]*a[k][j]
                assert val % prev == 0
                a[i][j] = val // prev
        for i in range(k+1,n):
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def exact_laplacian(bits):
    n = len(bits)
    a = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            a[i][j] = a[j][i] = bits[j]
    return [[(sum(a[i]) if i==j else -a[i][j]) for j in range(n)] for i in range(n)]


def eigen_product(bits):
    n=len(bits)
    tail=0
    eig=[]
    for i in range(n-1,-1,-1):
        if i>=1:
            eig.append((i+1)*bits[i]+tail)
        tail+=bits[i]
    prod=math.prod(eig)
    check(prod % n == 0, 'Matrix-tree normalizing divisor')
    return prod // n


for n in range(2, 10):
    for middle in product((0,1), repeat=n-2):
        z=(0,)+middle+(1,)
        lap=exact_laplacian(z)
        kirchhoff=det_bareiss([row[:-1] for row in lap[:-1]])
        check(kirchhoff == eigen_product(z), f'Exact tree count n={n}, bits={z}')
        check(kirchhoff >= 1, f'Connectivity n={n}')
        for i in range(1,n):
            v=[1]*i+[-i]+[0]*(n-i-1)
            lam=(i+1)*z[i]+sum(z[i+1:])
            lv=[sum(lap[j][k]*v[k] for k in range(n)) for j in range(n)]
            check(lv == [lam*w for w in v], f'Laplacian eigenvector n={n}, i={i}')


def f(p):
    return -1+(1-2*p)/(1-p)*math.log(p)


def h_mean(p, x):
    return p*math.log(p+(1-p)*x)+(1-p)*math.log(p*(1-x))


def g(p,y):
    return math.log((p+(1-p)*y)/p)/(1-p)-math.log1p(-y)/p


def midpoint(fn, intervals=20000):
    """Composite midpoint integration on [0,1], avoiding singular x=1."""
    h=1/intervals
    acc=0.0
    for j in range(intervals):
        x=(j+0.5)*h
        # Midpoint rule converges rapidly for integrable logarithmic endpoints.
        acc+=fn(x)
    return acc*h

for p in (0.1,0.25,0.5,0.75,0.9):
    f_integral=midpoint(lambda x: h_mean(p,x))
    check(abs(f_integral-f(p)) < 0.0002, f'Integral mean p={p}')
    check(midpoint(lambda x: g(p,x)**2)*p*(1-p)>0, f'Positive variance p={p}')

vhalf = 0.25 * midpoint(lambda x:g(0.5,x)**2,100000)
check(abs(vhalf - math.pi**2/3) < 0.001, f'Special variance: {vhalf}')
check(all(f(p)<f(q) for p,q in zip((.01,.1,.2,.5,.8),(.1,.2,.5,.8,.99))), 'Monotone f')

rng=random.Random(20261104)
for p in (0.25,0.5,0.75):
    n=2000
    samples=[]
    for _ in range(350):
        z=[int(rng.random()<p) for _ in range(n-1)]+[1]
        tail=0
        L=0.0
        for i in range(n-1,0,-1):
            lam=(i+1)*z[i]+tail
            L+=math.log(lam/n)
            tail+=z[i]
        samples.append((L-n*f(p))/math.sqrt(n))
    empirical=sum(samples)/len(samples)
    sample_var=sum((t-empirical)**2 for t in samples)/len(samples)
    target=p*(1-p)*midpoint(lambda x:g(p,x)**2)
    check(abs(sample_var-target)<0.45*target,'Seeded Monte Carlo consistency')

print(f'PASS: {checks} exact/algebraic/numerical checks; v(1/2)={vhalf:.9f}; pi^2/3={math.pi**2/3:.9f}')
print('Finite tests do not certify any asymptotic limit or historical priority.')
