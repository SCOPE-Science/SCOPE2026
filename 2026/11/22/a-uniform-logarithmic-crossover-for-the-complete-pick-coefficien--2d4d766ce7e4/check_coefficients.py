"""Numerical diagnostics for the Dirichlet-kernel reciprocal coefficients.

All infinite asymptotics in the accompanying result are analytic; this script
checks selected finite recurrences and scaling values only.
"""
from math import log, sinh, isfinite


def coefficients(alpha, N):
    a = [(k+1.0)**(-alpha) for k in range(N+1)]
    b = [0.0]*(N+1)
    for n in range(1, N+1):
        b[n] = a[n] - sum(b[k]*a[n-k] for k in range(1,n))
    return b


def phi(s):
    return 1.0 if s == 0 else (s/(2.0*sinh(s/2.0)))**2


count = 0
for alpha in (0.2,0.5,0.75,0.95,1.0):
    b=coefficients(alpha,150)
    for n in range(1,151):
        assert b[n]>0, (alpha,n,b[n])
        count+=1
    assert abs(b[1]-2.0**(-alpha)) < 1e-12
    count+=1
    assert abs(b[2]-(3.0**(-alpha)-4.0**(-alpha))) < 1e-12
    count+=1

for n in (200,500,1000):
    for s in (0.,1.,2.):
        alpha=1.0-s/log(n)
        b=coefficients(alpha,n)
        actual=n*log(n)**2*b[-1]
        target=phi(s)
        assert isfinite(actual) and actual>0 and actual<target*1.1
        count+=1

# Qualitative improvement as the sample size grows, without assuming a
# finite-sample remainder or substituting numerical evidence for the theorem.
for s in (0.,1.,2.):
    vals=[]
    for n in (200,500,1000):
        alpha=1.0-s/log(n)
        vals.append(n*log(n)**2*coefficients(alpha,n)[-1])
    assert vals[0] < vals[1] < vals[2]
    count+=1
print(f"DIRICHLET_PICK_COEFFICIENT_DIAGNOSTIC_OK {count}")
