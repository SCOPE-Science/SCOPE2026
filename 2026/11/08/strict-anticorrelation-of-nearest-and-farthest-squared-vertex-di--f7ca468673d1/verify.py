"""Exact rational certificates and independently sampled geometry for simplex distance covariance.
Scientific checks only; no external libraries required.
"""
from fractions import Fraction as F
from math import log, pi, sqrt, comb
from random import Random

def theoretical(n):
    assert n >= 2
    h = sum((F(1,k) for k in range(1,n+1)),F(0))
    j = sum((F(1,k*k) for k in range(1,n+1)),F(0))
    var_q = F(4*(n-1), (n+1)**2*(n+2)*(n+3))
    cov_q_max = (h*h+j-2*h)/(n*(n+1)*(n+2))
    cov_q_min = F(2*(1-n), n**3*(n+1)*(n+2))
    cov_max_min = (1-h)/(n**3*(n+1))
    cov = var_q-2*cov_q_max-2*cov_q_min+4*cov_max_min
    var_max = (n*j-h*h)/(n*n*(n+1))
    var_min = F(n-1,n**4*(n+1))
    var_r = var_q+4*var_max-4*cov_q_max
    var_t = var_q+4*var_min-4*cov_q_min
    return {'h':h,'j':j,'var_q':var_q,'cov_q_max':cov_q_max,
        'cov_q_min':cov_q_min,'cov_max_min':cov_max_min,
        'cov':cov, 'var_r':var_r, 'var_t':var_t}

# Exact finite cases, and a global analytic inequality for n >= 7:
# h_n >= h_7, j_n >= 1, so h_n^2+j_n-2h_n >= (h_7-1)^2
# > 2+2/7 >= 2n(n-1)/((n+1)(n+3)) + 2(n-1)/n^2.
assert (theoretical(7)['h']-1)**2 > F(2)+F(2,7)
for n in range(2,7):
    z=theoretical(n)
    assert z['cov']<0,(n,z['cov'])
    print('finite certificate',n, 'covariance',z['cov'])
for n in range(7,500):
    z=theoretical(n)
    assert z['cov']<0
    positive_gap=z['h']**2+z['j']-2*z['h']-(F(2*n*(n-1),(n+1)*(n+3))+F(2*(n-1),n*n))
    assert positive_gap>0

# Independent exact beta integration for E[Q max(X)]: inclusion-exclusion
# j-constraint conditional shifts and known Dirichlet quadratic moment.
for n in range(2,14):
    v=F(0)
    for k in range(1,n+1):
        vv=(F(2,k*k*n*(n+1)*(n+2))+
            F(2,k*n*(n+1)*(n+2))+
            F(2,k*(n+1)*(n+2)))
        v+=(-1)**(k+1)*comb(n,k)*vv
    z=theoretical(n)
    expected=F(2,n+1)*z['h']/n+z['cov_q_max']
    assert v==expected, (n,v,expected)

# Independent geometric Monte Carlo using exponential-normalized coordinates.
rng=Random(20261101)
for n,N in [(3,50000),(5,50000),(12,70000)]:
    sr=st=sr2=st2=srt=0.0
    for _ in range(N):
        xs=[rng.expovariate(1) for i in range(n)]
        s=sum(xs); xs=[t/s for t in xs]
        q=sum(t*t for t in xs)
        r=1+q-2*max(xs)
        t=1+q-2*min(xs)
        sr+=r; st+=t; sr2+=r*r; st2+=t*t; srt+=r*t
    cov=srt/N-(sr/N)*(st/N)
    exact=float(theoretical(n)['cov'])
    print('simulation',n,'observed',cov,'exact',exact,'relative discrepancy',abs(cov/exact-1))
    assert cov<0 and abs(cov-exact)<max(0.0002,0.05*abs(exact))

# Harmonic asymptotics: scaled signs, requires slow log convergence.
for n in [1000,10000]:
    z=theoretical(n)
    print('asymptotic ratio',n,float(z['cov'])*n**3/(-2*log(n)**2))
    assert float(z['cov'])<0
print('SIMPLEX_NEAREST_FARTHEST_COVARIANCE_CHECKS_PASSED')
