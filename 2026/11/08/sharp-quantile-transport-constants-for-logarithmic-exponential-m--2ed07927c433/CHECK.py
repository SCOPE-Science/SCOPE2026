#!/usr/bin/env python3
"""Reproducible finite diagnostics for the log-exponential-maximum quantile theorem.
Analytic global inequalities and endpoint limits are established in RESULT.md,
not inferred from this finite verifier. Python 3 standard library only.
"""
import math

COUNT = 0

def check(condition, explanation):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(explanation)

def q(n, u):
    return math.log(-math.log1p(-math.exp(math.log(u)/n)))

def F(n, y):
    return (1.0-math.exp(-math.exp(y))) ** n

def h(x):
    t = math.exp(-x)
    return x*t / ((-math.expm1(-x))*(-math.log1p(-t)))

def dq(n, u):
    x = -math.log(u)/n
    return h(x)/(u*(-math.log(u)))

# Inverse-CDF identities over a broad finite grid.
for n in (1,2,3,5,10,30):
    for u in (0.00001,0.0001,0.01,0.1,0.25,0.5,0.8,0.99,0.9999):
        err=abs(F(n,q(n,u))-u)
        check(err < 2e-11, f'quantile inversion n={n}, u={u}, error={err}')

# Analytic derivative formula, compared to a centered finite difference.
for n in (1,2,3,7,20):
    for u in (0.01, 0.1, 0.3, 0.5, 0.8, 0.97):
        eps=1e-6*min(u,1-u)
        num=(q(n,u+eps)-q(n,u-eps))/(2*eps)
        check(abs(dq(n,u)/num-1)<3e-6, f'derivative n={n}, u={u}')

# Strict, global two-sided derivative bounds on a finite mesh.
for n,m in ((1,2),(1,10),(2,3),(2,9),(3,30),(10,100)):
    for k in range(1,1000):
        u=k/1000
        ratio=dq(m,u)/dq(n,u)
        check(n/m < ratio < 1.0, f'slope n={n},m={m},u={u}, ratio={ratio}')

# All interquantile gaps contract strictly by the sharp factor bounds.
probs=(0.005,0.02,0.1,0.25,0.4,0.6,0.8,0.95,0.99)
for n,m in ((1,2),(1,9),(2,3),(2,10),(10,20)):
    for i,u in enumerate(probs):
        for v in probs[i+1:]:
            old=q(n,v)-q(n,u)
            new=q(m,v)-q(m,u)
            check(n/m*old < new < old, f'width n={n},m={m},u={u},v={v}')

# Core strict logarithmic inequalities used in the proof, finite diagnostics only.
for k in range(1,1000):
    t=k/1000
    x=-math.log(t)
    a=-math.log1p(-t)
    check(t/a>1-t, f'first log inequality t={t}')
    check((1-t)/x>t, f'second log inequality t={t}')
    check(a>t, f'last log inequality t={t}')

# Sharp endpoint factors: numerical approach (the limits are proved analytically).
for n,m in ((1,2),(2,5)):
    low=[dq(m,10.0**(-k))/dq(n,10.0**(-k)) for k in (5,10,20,30)]
    high=[dq(m,1.0-10.0**(-k))/dq(n,1.0-10.0**(-k)) for k in (2,4,6,8,10)]
    check(abs(low[-1]-n/m)<abs(low[0]-n/m), 'lower endpoint approach')
    check(abs(high[-1]-1)<abs(high[0]-1), 'upper endpoint approach')

# Independent approximate moment quadrature on uniform quantile midpoint grids.
M=20000
vars=[]
for n in (1,2,3,4,10):
    values=(q(n,(j+0.5)/M) for j in range(M))
    s=ss=0.0
    for v in values:
        s+=v; ss+=v*v
    mean=s/M
    var=ss/M-mean*mean
    vars.append(var)
check(abs(vars[0]-math.pi**2/6)<0.003,'variance of log Exp(1)')
for v,w in zip(vars,vars[1:]):
    check(v>w>0,'variance monotonic grid')

print(f'PASS: {COUNT} finite numerical diagnostics; quantile mesh and moment checks passed.')
print('Approximate variances for n=1,2,3,4,10:', ', '.join(f'{v:.9f}' for v in vars))
print('Analytic proof required for all quantile levels, all sample sizes, and sharp endpoints.')
