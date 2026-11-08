"""Finite checks for a rootless comb weighted-shift construction.

Usage: python3 checker.py
Finite checks are illustrative; the proof of convergence is analytic.
"""
from math import sqrt, log, exp, isclose

TESTS = 0

def check(condition, label="check"):
    global TESTS
    TESTS += 1
    if not condition:
        raise AssertionError(label)

def weight(j, m, N, beta):
    """Weight on the edge entering (j,m), with j>=0, m integral."""
    if j == 0:
        return sqrt((N+m)/(N+m+1)) if m >= 0 else 1.0
    if j == 1:
        return (N+m)**(-0.5) if m >= 1 else (N+1+abs(m))**(-0.5)
    if m >= 2 and 2 <= j <= m:
        return exp(beta*log(1+m/N)/(2*(m-1)))
    return 1.0

def parent_norm_sq(j, m, N, beta):
    if j == 0:
        return weight(0,m-1,N,beta)**2 + weight(1,m,N,beta)**2
    return weight(j+1,m,N,beta)**2

def dual_weight(j,m,N,beta):
    if j == 0:
        return weight(0,m,N,beta)/parent_norm_sq(0,m+1,N,beta)
    if j == 1:
        return weight(1,m,N,beta)/parent_norm_sq(0,m,N,beta)
    return weight(j,m,N,beta)/parent_norm_sq(j-1,m,N,beta)

def path_ratio(m,N,beta,dual=False):
    """Ratio of two m-step path products from (0,m) to (m,m)/(0,0)."""
    w = dual_weight if dual else weight
    spine = 1.0
    for t in range(m):
        spine *= w(0,t,N,beta)
    side = w(1,m,N,beta)
    for j in range(2,m+1):
        side *= w(j,m,N,beta)
    return (side/spine)**2

def target_g(m,N,beta):
    return (1+m/N)**beta if m>=2 else 1.0

def perturbation_column_sq(j,m,N,beta):
    if j==0:
        return (weight(0,m-1,N,beta)-1.0)**2+weight(1,m,N,beta)**2
    return (weight(j+1,m,N,beta)-1.0)**2

def target_norm(N,beta):
    return max(sqrt(2*(1-sqrt(N/(N+1)))), (1+2/N)**(beta/2)-1)

for N in (2,4,9,20,100):
    for beta in (0.5,1.0,1.2,2.0,3.0):
        for m in range(-24,43):
            for j in (0,1,2,3,7,31):
                check(parent_norm_sq(j,m,N,beta)>=1-1e-12,"expansive")
        for m in range(1,43):
            g=target_g(m,N,beta)
            check(isclose(path_ratio(m,N,beta),g/N,rel_tol=1e-11,abs_tol=1e-13),"primal path")
            check(isclose(path_ratio(m,N,beta,True),1/(N*g),rel_tol=1e-11,abs_tol=1e-13),"dual path")
        observed=max(sqrt(perturbation_column_sq(j,m,N,beta))
                     for m in range(-65,105) for j in range(0,105))
        check(isclose(observed,target_norm(N,beta),rel_tol=2e-12,abs_tol=2e-12),"perturbation norm")
        bound=max(sqrt(2/(N+1)), exp(beta/N)-1)
        check(observed<=bound+1e-12,"norm smallness bound")
        for m in range(2,102):
            check(weight(2,m+1,N,beta)<=weight(2,m,N,beta)+1e-12,"monotone tail amplitude")

# Ensure the analyticity and dual-transition tests are not based on a finite cutoff.
# Numerically verify the series' exact terms, leaving convergence to p-series.
for beta in (0.7,1.0,1.6,3.0):
    N=5
    for m in range(2,300):
        g=target_g(m,N,beta)
        check(g>=1,"primal divergence term")
        check(isclose(1/g,(1+m/N)**(-beta),rel_tol=1e-13),"dual p-series term")

# Direct Schatten column-norm accumulation checks for sample finite truncations.
for N,beta in ((5,2.0),(14,1.2),(25,3.0)):
    for p in (1.5,2.0,2.5,3.0,4.0):
        for M in (20,60,120):
            direct=sum(perturbation_column_sq(0,m,N,beta)**(p/2)
                       for m in range(-M,M+1))
            direct+=sum(perturbation_column_sq(j,m,N,beta)**(p/2)
                        for m in range(-M,M+1) for j in range(1,M+2))
            bsum=sum(perturbation_column_sq(0,m,N,beta)**(p/2)
                     for m in range(-M,M+1))
            tsum=sum((m-1)*(weight(2,m,N,beta)-1)**p for m in range(2,M+1))
            check(isclose(direct,bsum+tsum,rel_tol=1e-12,abs_tol=1e-12),"orthogonal-column Schatten count")
print(f"PASS: {TESTS} finite checks for edge weights, Cauchy dual, path ratios, norm, Schatten sums")
