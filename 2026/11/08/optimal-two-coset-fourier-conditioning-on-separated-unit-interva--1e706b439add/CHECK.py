"""Check finite tests for two-unit-interval, two-coset Fourier Riesz bounds.

The infinite-dimensional theorem is proved analytically in RESULT.md;
these tests only check formulas and exact finite Fourier integrals.
"""
import cmath
import math
import random

PI = math.pi

def target(m,tau):
    h=max(abs(math.cos(PI*m*tau)),abs(math.cos(PI*(m+1)*tau)))
    return 2-2*h,2+2*h

def int_one_exp(freq,start):
    if abs(freq)<1e-12:
        return 1.+0.j
    return cmath.exp(2j*PI*freq*(start+0.5))*math.sin(PI*freq)/(PI*freq)

def exact_direct(ca,cb,tau,d):
    n=len(ca)
    freqs=list(range(-n//2,-n//2+n))
    seq=[(freqs[j],ca[j]) for j in range(n)] + [(freqs[j]+tau,cb[j]) for j in range(n)]
    s=0j
    for w,c in seq:
        for v,e in seq:
            s+=c*e.conjugate()*(int_one_exp(w-v,0)+int_one_exp(w-v,d))
    return s.real

def fiber_quadrature(ca,cb,tau,d,grid=24000):
    n=len(ca);freqs=list(range(-n//2,-n//2+n))
    m=math.floor(d);delta=d-m
    total=0.
    for k in range(grid):
        z=(k+0.5)/grid
        A=sum(ca[j]*cmath.exp(2j*PI*freqs[j]*z) for j in range(n))
        B=sum(cb[j]*cmath.exp(2j*PI*freqs[j]*z) for j in range(n))
        e=cmath.exp(2j*PI*tau*z)
        q=m+(z<delta)
        total+=(abs(A+e*B)**2+abs(A+e*cmath.exp(2j*PI*q*tau)*B)**2)/grid
    return total

rng=random.Random(20261106)
count=0
for m in range(1,9):
    tauopt=1/(2*m+1)
    cstar=math.sin(PI/(4*m+2))
    for shift in [tauopt,1-tauopt]:
        calc=max(abs(math.cos(PI*m*shift)),abs(math.cos(PI*(m+1)*shift)))
        assert abs(calc-cstar)<2e-13,(m,shift,calc,cstar)
        count+=1
    for j in range(1800):
        tau=rng.random()
        c=max(abs(math.cos(PI*m*tau)),abs(math.cos(PI*(m+1)*tau)))
        assert c>cstar-2e-12,(m,tau,c,cstar)
        count+=1
    for delta in [0.04,0.33,0.91]:
        d=m+delta
        for tau in [tauopt,0.137,0.276,0.418]:
            a,b=target(m,tau)
            for n in [2,3]:
                ca=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for j in range(n)]
                cb=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for j in range(n)]
                x=exact_direct(ca,cb,tau,d)
                coeff=sum(abs(z)**2 for z in ca+cb)
                assert a*coeff-1e-8<=x<=b*coeff+1e-8,(m,d,tau,a,x,b,coeff)
                y=fiber_quadrature(ca,cb,tau,d,grid=5000)
                assert abs(x-y)<0.006,(m,d,tau,x,y)
                count+=2
    # Integer-separated intervals allow exact orthogonality.
    tau=1/(2*m)
    a,b=2-2*abs(math.cos(PI*m*tau)),2+2*abs(math.cos(PI*m*tau))
    assert abs(a-2)<1e-12 and abs(b-2)<1e-12
    count+=1
print('TWO_INTERVAL_RIESZ_CHECKS_PASSED',count)
