"""Reproducibility checks for exact two-state positive exponential splitting.
Uses Python standard library only. Analytic proof is supplied in RESULT.md.
"""
from math import exp, expm1, log, isfinite
from random import Random

def matmul(a,b):
    return ((a[0][0]*b[0][0]+a[0][1]*b[1][0], a[0][0]*b[0][1]+a[0][1]*b[1][1]),
            (a[1][0]*b[0][0]+a[1][1]*b[1][0], a[1][0]*b[0][1]+a[1][1]*b[1][1]))

def generator(u,v):
    return ((-u,v),(u,-v))

def exponential(u,v,t):
    lam=u+v
    c=-expm1(-lam*t)/lam
    return ((1-c*u,c*v),(c*u,1-c*v))

def theta(a,b,h):
    # Stable evaluation via logarithms of entire phi_1(-z).
    ga=-expm1(-b*h)/(b*h)
    gb=-expm1(-(a+b)*h)/((a+b)*h)
    return (log(ga)-log(gb))/(a*h)

def max_err(a,b):
    return max(abs(a[i][j]-b[i][j]) for i in range(2) for j in range(2))

def run():
    rng=Random(2112026)
    count=0
    worst=0.0
    for _ in range(250):
        u1=exp(rng.uniform(-3,3));v1=exp(rng.uniform(-3,3))
        u2=exp(rng.uniform(-3,3));v2=exp(rng.uniform(-3,3))
        a=u1+v1;b=u2+v2
        h=exp(rng.uniform(-5.5,2.5))
        q=theta(a,b,h)
        assert 0<q<.5, (a,b,h,q)
        exact=exponential(u1+u2,v1+v2,h)
        approx=matmul(matmul(exponential(u1,v1,q*h), exponential(u2,v2,h)),exponential(u1,v1,(1-q)*h))
        err=max_err(exact,approx)
        worst=max(worst,err)
        assert err < 2e-12, (a,b,h,err)
        assert all(approx[i][j]>=-1e-14 for i in range(2) for j in range(2))
        assert all(abs(approx[0][j]+approx[1][j]-1)<2e-12 for j in range(2))
        count+=1
    # Smooth strict decrease and correct asymptotic limit, across rate ratios.
    for a,b in [(1,1),(0.4,9),(9,0.4),(17,31),(1e-1,1e-2),(1e-2,1e-1)]:
        hs=[0.01,0.03,0.1,0.3,1,3,10,30,100]
        vals=[theta(a,b,h) for h in hs]
        assert all(0<vals[j+1]<vals[j]<.5 for j in range(len(vals)-1)),(a,b,vals)
        for h in [0.002,0.004]:
            approx=.5-(a+2*b)*h/24
            assert abs(theta(a,b,h)-approx)<1e-3, (a,b,h)
        count+=len(hs)+2
    # Noncommuting witness, and cubic (not higher) Strang local defect.
    u1,v1,u2,v2=2.,1.,4.,7.
    a=u1+v1;b=u2+v2
    pi1=v1/a;pi2=v2/b
    coefficient=-a*b*(a+2*b)*(pi2-pi1)/24
    for h in [0.001,0.002,0.004]:
        standard=matmul(matmul(exponential(u1,v1,h/2),exponential(u2,v2,h)),exponential(u1,v1,h/2))
        exact=exponential(u1+u2,v1+v2,h)
        actual=(standard[0][0]-exact[0][0])/h**3
        assert abs(actual-coefficient)<abs(coefficient)*0.05,(h,actual,coefficient)
        count+=1
    print('PASS:', count,'positive-rate tests, maximum factorization entrywise error', format(worst,'.4g'))
    print('PASS: ordering, strict positive substeps, near-zero Taylor test, nonzero Strang cubic error')
if __name__=='__main__':run()
