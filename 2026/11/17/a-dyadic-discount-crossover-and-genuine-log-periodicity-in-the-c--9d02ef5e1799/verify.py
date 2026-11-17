"""Exact orbit-census and numerical scaling checks for the dyadic cat-map landscape.
Run with: python verify.py
Uses the Python standard library and optionally mpmath for high-precision checks.
"""
from collections import Counter
from fractions import Fraction
from math import exp, expm1

A = ((1, 1), (1, 2))

def matmul(X,Y):
    return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def counts_formula(a):
    if a == 1:
        return {1:1,3:3}
    d={1:1,3:15}
    for s in range(1,a-1):
        d[3*2**s]=3*4**(s+1)
    return d

def enumerate_periods(a):
    N=2**a
    out=Counter()
    seen=set()
    for x in range(N):
        for y in range(N):
            if (x,y) in seen:
                continue
            orbit=[]
            xx,yy=x,y
            while (xx,yy) not in seen:
                seen.add((xx,yy));orbit.append((xx,yy))
                xx,yy=(xx+yy)%N,(xx+2*yy)%N
            assert (xx,yy)==(x,y), 'This invertible map must have pure cycles'
            out[len(orbit)]+=len(orbit)
    assert len(seen)==N*N
    return dict(out)

def exact_trace(a,alpha):
    return sum((Fraction(c,1)/(1-alpha**period) for period,c in counts_formula(a).items()),Fraction(0))

def g(u):
    return -1/expm1(-u)

def profile(t,jmax=60):
    return sum(0.75*4.0**(-j)*g(t/2.0**j) for j in range(jmax+1))

def finite_trace(a,t):
    M=3*2**(a-2)
    return sum(c*g(t*period/M) for period,c in counts_formula(a).items())/4.0**a

if __name__=='__main__':
    A2=matmul(A,A); A3=matmul(A2,A)
    assert A3==((5,8),(8,13))
    C=tuple(tuple((A3[i][j]-(1 if i==j else 0))//4 for j in range(2)) for i in range(2))
    assert C==((1,2),(2,3)) and C[0][0]*C[1][1]-C[0][1]*C[1][0]==-1
    for a in range(1,7):
        assert enumerate_periods(a)==counts_formula(a)
        assert sum(counts_formula(a).values())==4**a
    for a in range(2,7):
        alpha=Fraction(1,2)
        F=exact_trace(a,alpha)
        assert F>0
    for t in (0.5,1.0,5.0):
        assert abs(finite_trace(15,t)-profile(t))<2e-4
    try:
        import mpmath as mp
        mp.mp.dps=45
        def f(z): return z*z/mp.expm1(z)
        def H(t): return mp.mpf(3)/4*sum(f(t*mp.power(2,-k)) for k in range(-14,80))
        v1=H(mp.mpf(1));v2=H(mp.mpf('1.5'))
        assert abs(v1-H(mp.mpf(2)))<mp.mpf('1e-20')
        assert v1-v2>mp.mpf('0.0001')
        c0=mp.pi**2/(8*mp.log(2))
        c1=3/(4*mp.log(2))*mp.gamma(2-2j*mp.pi/mp.log(2))*mp.zeta(2-2j*mp.pi/mp.log(2))
        assert abs(c1)>mp.mpf('1e-7')
        print('H(1)=',mp.nstr(v1,20),'H(3/2)=',mp.nstr(v2,20))
        print('periodic-average=',mp.nstr(c0,20),'nonzero-first-Fourier-abs=',mp.nstr(abs(c1),12))
    except ImportError:
        print('mpmath unavailable; the optional high-precision checks were skipped')
    print('VERIFY_OK exact_A3=1 dyadic_censuses=6 rational_traces=5 scaling_samples=3')
