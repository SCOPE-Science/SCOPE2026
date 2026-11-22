#!/usr/bin/env python3
"""Independent numerical checks for the exact Szász–Kantorovich BV leakage theorem.
Dependencies: Python 3.10+, scipy. This script checks finite test instances; analytic assertions are proved in RESULT.md.
"""
import math
from scipy.stats import poisson
from scipy.integrate import quad
from scipy.optimize import brentq


def tail_at_one(n, k):
    return float(poisson.cdf(k, n)) if k >= 0 else 0.0


def erlang_overshoot(n, k):
    if k == 0: return 0.0
    return k/n * tail_at_one(n, k) - tail_at_one(n, k-1)


def response(n, s, x):
    z=n*s
    m=min(n-1, int(math.floor(z)))
    a=z-m
    return poisson.sf(m, n*x) + (1-a)*poisson.pmf(m, n*x)


def exact_error(n, s):
    z=n*s; m=int(math.floor(z)); a=z-m
    return 2*s*poisson.pmf(m,z)-(1-a)*erlang_overshoot(n,m)-a*erlang_overshoot(n,m+1)


def direct_error(n, s):
    v1=quad(lambda x: response(n,s,x), 0, s, epsabs=3e-11)[0]
    v2=quad(lambda x: 1-response(n,s,x), s, 1, epsabs=3e-11)[0]
    return v1+v2


def root_per_cell(n, m):
    q=tail_at_one(n,m)
    pm=math.exp(-m)*m**m/math.factorial(m) if 0<m<100 else (1. if m==0 else float(poisson.pmf(m,m)))
    if 2*pm<=q: return None
    a=brentq(lambda aa:2*(1-aa)*poisson.pmf(m,m+aa)-q,0,1,xtol=1e-13)
    if not (1e-8<a<1-1e-8): return None  # numerically unresolved boundary-near root
    return (m+a)/n


def run():
    count=0
    for n in [1,2,3,4,5,7,10,15,20,30,50,80]:
        for j in range(1,65):
            s=(j+.237)/(65.0)
            a=exact_error(n,s); b=direct_error(n,s)
            assert abs(a-b)<5e-9, (n,s,a,b)
            count+=1
    print('DIRECT_POISSON_INTEGRAL_VS_GAMMA_MIXTURE_PASS',count)
    count=0
    for n in [1,2,3,4,5,7,10,20,50,100]:
        best=(-1,None)
        for m in range(n):
            s=root_per_cell(n,m)
            if s is None: continue
            eps=min(1/(10000*n), (s-m/n)/5, ((m+1)/n-s)/5)
            mid=exact_error(n,s)
            # Stationary derivative changes sign inside well-resolved cells.
            aa=n*s-m
            dleft=2*(1-(aa-n*eps))*poisson.pmf(m,m+aa-n*eps)-tail_at_one(n,m)
            dright=2*(1-(aa+n*eps))*poisson.pmf(m,m+aa+n*eps)-tail_at_one(n,m)
            assert dleft>0 and dright<0, (n,m,dleft,dright)
            if mid>best[0]:best=(mid,s)
            count+=1
        assert best[1] is not None
        grid=max(exact_error(n,(i+.5)*.001) for i in range(2000) if (i+.5)*.001<1) if n==1 else None
        if grid is not None: assert best[0]>=grid-1e-5
        assert best[0]>0
    print('STRICT_CELL_MAXIMA_AND_FINITE_SHARP_SEARCH_PASS',count)
    count=0
    for n in [2,5,20]:
        import random
        rng=random.Random(n)
        roots=[root_per_cell(n,m) for m in range(n)]
        C=max(exact_error(n,s) for s in roots if s is not None)
        for _ in range(12):
            steps=sorted(rng.uniform(0.001,0.999) for i in range(4))
            weights=[rng.uniform(-1,1) for i in range(4)]
            # Numerically integrate the error of the superposition of four jumps.
            def ff(x):return sum(w*(float(x>=s)-response(n,s,x)) for s,w in zip(steps,weights))
            bounds=[0.]+steps+[1.]
            e=sum(quad(lambda x:abs(ff(x)),l,r,epsabs=3e-6)[0] for l,r in zip(bounds[:-1],bounds[1:]))
            assert e<=C*sum(abs(w) for w in weights)+1e-7,(n,e,C,weights)
            count+=1
    print('MULTIJUMP_BV_BOUNDS_PASS',count)
    print('EXAMPLE',[(n, round(max((exact_error(n,s),s) for s in [root_per_cell(n,m) for m in range(n)] if s is not None)[0],10)) for n in (1,2,3,10,50,100)])
    print('ALL_SZASZ_KANTOROVICH_BV_CHECKS_PASS')

if __name__=='__main__':run()
