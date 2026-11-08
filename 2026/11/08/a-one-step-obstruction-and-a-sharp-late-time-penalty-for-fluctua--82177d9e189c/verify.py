#!/usr/bin/env python3
"""Independent finite checks for lattice first-passage response to rate renewal.

Requires Python 3, NumPy and SciPy. Infinite-time and all-parameter claims
are proved in RESULT.md, not by these examples.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq
from scipy.special import ive
from scipy.stats import binom

CHECKS = 0

def check(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1

def h(m, u):
    """Exact survival starting m, unit total jump rate."""
    return float(ive(0, u) + ive(m, u) + 2 * sum(ive(k, u) for k in range(1, m)))

def density(m, u):
    return float(m * ive(m, u) / u)

def derivative_density(m, u):
    return density(m, u) * (ive(m + 1, u) / ive(m, u) + (m - 1) / u - 1)

def killed_generator(N=40):
    Q = np.zeros((N, N), dtype=float)
    for i in range(N):
        if i:
            Q[i, i - 1] = 0.5
        if i < N - 1:
            Q[i, i + 1] = 0.5
        Q[i, i] = -1 if i < N-1 else -0.5
    return Q

Q = killed_generator()

# Direct killed-chain dynamics, computed independently from Bessel identities.
for m in range(1, 7):
    for u in (0.2, 1.0, 3.0, 6.0):
        direct = np.sum(expm(Q*u)[m-1, :])
        check(abs(direct - h(m, u)) < 2e-12, f"matrix/Bessel {m},{u}")

# Exact rational generator jets certify first nonzero absorption coefficient.
# The top boundary of the truncated generator is too far to alter order <=m.
for m in range(1, 9):
    size = 2*m+4
    A = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for i in range(size):
        A[i][i] = Fraction(-1) if i != size-1 else Fraction(-1,2)
        if i > 0: A[i][i-1] = Fraction(1,2)
        if i+1<size: A[i][i+1] = Fraction(1,2)
    v = [Fraction(1) for _ in range(size)]
    for k in range(m+1):
        expected = Fraction(1) if k==0 else (Fraction(-1,2**m) if k==m else Fraction(0))
        check(v[m-1] == expected, f"Taylor derivative m={m} k={k}")
        v = [sum(A[i][j]*v[j] for j in range(size)) for i in range(size)]

# Density is monotone at one site and has exactly one critical point in samples.
for u in (0.001, 0.1, 1, 10, 100):
    check(derivative_density(1, u) < 0, f"m=1 density decreasing at {u}")
for m in range(2, 18):
    root = brentq(lambda u: derivative_density(m, u), 0.03, max(20, 5*m*m))
    check(root > (m*m-1)/3, f"root below analytic lower bound {m}")
    check(derivative_density(m, 0.9*root)>0, f"mode left {m}")
    check(derivative_density(m, 1.1*root)<0, f"mode right {m}")

# Bernoulli rate example: rate = 1/2 or 3/2 per unit interval.
def mix(m, t):
    n = int(math.floor(t))
    residue = t - n
    j = np.arange(n+1)
    weights = binom.pmf(j, n, 0.5)
    result = 0.0
    for k, w in zip(j, weights):
        clock = 0.5*n + float(k)
        result += w * (0.5*h(m, clock+residue*0.5) + 0.5*h(m, clock+residue*1.5))
    return float(result)

# Strict Jensen delay for the one-step starting position.
for t in (0.01, 0.1, 0.4, 0.8, 1.0, 2.5, 5, 20, 100, 500):
    check(mix(1, t) > h(1, t)+1e-14, f"near-target sign {t}")
# At least one reversal from early acceleration to late retardation.
for m, early, late in ((2,0.2,20),(3,0.5,30),(4,1.0,40),(5,2.0,80),(7,4.0,100)):
    check(mix(m, early) < h(m, early)-1e-13, f"early speedup {m}")
    check(mix(m, late) > h(m, late)+1e-12, f"late slowdown {m}")

# Exact resampled-clock averaging versus independently evolved killed chain.
for m in (1,2,3):
    for t in (1.2, 2.3, 4.0, 5.5):
        n = int(t); residue=t-n
        value = 0.0
        for k in range(n+1):
            w=binom.pmf(k,n,0.5)
            for rate in (0.5,1.5):
                u=0.5*n+k+rate*residue
                value += 0.5*w*np.sum(expm(Q*u)[m-1,:])
        check(abs(value-mix(m,t))<1e-11, f"independent clock/matrix {m},{t}")

# Exact long-time coefficient: 3*c_m*(variance)*(tau)/(8*mean**(5/2)).
for m in (1,2,3):
    coefficient = 3*m*math.sqrt(2/math.pi)*0.25/8
    errors=[]
    for t in (200,400,800,1600):
        delta = mix(m,t)-h(m,t)
        ratio=delta*t**1.5/coefficient
        errors.append(abs(1-ratio))
        check(abs(1-ratio)<0.08, f"long-time leading coefficient m={m},t={t}: {ratio}")
    check(errors[-1]<errors[0], f"convergence of coefficient {m}")

print(f"PASS: {CHECKS} independent exact-generator, mode, mixture and asymptotic checks")
for m in (2,3,5):
    mode = brentq(lambda u: derivative_density(m,u),0.03,5*m*m)
    print(f"m={m}: unique-curvature boundary u_m ~ {mode:.12f}, lower bound {(m*m-1)/3:.12f}")
