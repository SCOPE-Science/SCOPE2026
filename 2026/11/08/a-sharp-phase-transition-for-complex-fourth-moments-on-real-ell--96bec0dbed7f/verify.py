#!/usr/bin/env python3
"""Independent reproducibility checks of the complex linear fourth-moment theorem.
Requires Python 3 standard library only. Finite checks support, not replace, proof.
"""
from fractions import Fraction as F
from itertools import product
from math import gamma, isclose
import cmath
import random


def mulpoly(a,b):
    out={}
    for e,v in a.items():
        for f,w in b.items():
            t=tuple(u+v2 for u,v2 in zip(e,f))
            out[t]=out.get(t,0)+v*w
    return out


def quartic_by_direct_expansion(z,n,beta,gamma):
    re={tuple(int(j==i) for j in range(n)):z[i][0] for i in range(n)}
    im={tuple(int(j==i) for j in range(n)):z[i][1] for i in range(n)}
    rr=mulpoly(re,re); ii=mulpoly(im,im)
    for e,c in ii.items(): rr[e]=rr.get(e,0)+c
    all4=mulpoly(rr,rr)
    out=F(0)
    for e,c in all4.items():
        if any(x%2 for x in e): continue
        nz=tuple(x for x in e if x)
        if nz==(4,): m=beta
        elif nz==(2,2): m=gamma
        else: raise AssertionError((e,nz))
        out+=c*m
    return out


def moments(n,p):
    if p==1:
        denom=(n+1)*(n+2)*(n+3)*(n+4)
        return F(2,(n+1)*(n+2)), F(24,denom), F(4,denom)
    if p==2:
        return F(1,n+2),F(3,(n+2)*(n+4)),F(1,(n+2)*(n+4))
    if p=='inf':
        return F(1,3),F(1,5),F(1,9)
    raise AssertionError('exact rational checker only p=1,2,infinity')


def invariants(z):
    re=[F(a) for a,b in z]; im=[F(b) for a,b in z]
    w=[a*a+b*b for a,b in zip(re,im)]
    S=sum(w,F(0)); T=sum((v*v for v in w),F(0))
    qr=sum((a*a-b*b for a,b in zip(re,im)),F(0))
    qi=sum((2*a*b for a,b in zip(re,im)),F(0))
    q2=qr*qr+qi*qi
    return S,T,q2

# Rational partial fractions in the strict digamma monotonicity proof.
for x in (F(1,4),F(1,2),F(2,3),F(3,2)):
    for k in range(1,101):
        a=F(6,1)/(k+3*x)-F(5,1)/(k+5*x)-F(1,1)/(k+x)
        b=F(8*k)*x/((k+x)*(k+3*x)*(k+5*x))
        assert a==b and b>0
print('EXACT_GAMMA_RATIO_LOG_DERIVATIVE_PARTIAL_FRACTIONS_OK 400')

rng=random.Random(1039)
for n in range(2,8):
    for p in (1,2,'inf'):
        alpha,beta,gamma0=moments(n,p)
        h=gamma0/alpha**2
        R=beta/gamma0
        delta=R-3
        for trial in range(65):
            z=[(rng.randrange(-3,4),rng.randrange(-3,4)) for _ in range(n)]
            if all(a==b==0 for a,b in z): z[0]=(1,0)
            S,T,q2=invariants(z)
            integrated=quartic_by_direct_expansion(z,n,beta,gamma0)
            claimed=gamma0*(2*S*S+q2)+ (beta-3*gamma0)*T
            assert integrated==claimed, (n,p,z,integrated,claimed)
            K=integrated/(alpha*S)**2
            assert K/h==2+q2/S**2+delta*T/S**2
            if delta>0:
                lower=2+delta/F(n)
                upper=3+delta
                lowdiff=q2/S**2+delta*(T/S**2-F(1,n))
                updiff=1-q2/S**2+delta*(1-T/S**2)
            elif delta<0:
                d=-delta
                lower=2-d/F(2)
                upper=3-d/F(n)
                lowdiff=(1-d/F(2))*q2/S**2+(d/F(2))*(q2+S*S-2*T)/S**2
                updiff=(S*S-q2)/S**2+d*(T/S**2-F(1,n))
            else:
                lower=2; upper=3
                lowdiff=q2/S**2; updiff=1-q2/S**2
            assert K/h >= lower and K/h<=upper
            assert K/h-lower==lowdiff and upper-K/h==updiff
        if p==1:
            zmin=[(1,0)]+[(round(0),0) for _ in range(n-1)]
            assert R==6
            zm=[(1,0)] + [(0,0) for _ in range(n-1)]
            assert ((gamma0*(2*invariants(zm)[0]**2+invariants(zm)[2])+(beta-3*gamma0)*invariants(zm)[1])/(alpha*invariants(zm)[0])**2)/h==R
        if p=='inf': assert R==F(9,5)
print('EXACT_DIRECT_FOURTH_MOMENTS_AND_DEFICITS_OK n=2..7 p=1,2,infinity; 1170 vectors')

# Verify the closed-form real/imaginary pairwise square identity exactly.
for n in range(2,10):
    for t in range(40):
        z=[(rng.randrange(-4,5),rng.randrange(-4,5)) for _ in range(n)]
        S,T,q2=invariants(z)
        pair=sum((F((z[i][0]*z[j][0]+z[i][1]*z[j][1])**2) for i in range(n) for j in range(i+1,n)),F(0))
        assert q2+S*S-2*T==4*pair
print('EXACT_COMPLEX_PHASE_SQUARE_IDENTITY_OK 320 cases')

# Scalar gamma interpolation and exact endpoint witnesses.
def ratios(n,p):
    if p=='inf': return 1.0,1.8
    x=1.0/p
    h=gamma(1+(n+2)*x)**2/(gamma(1+n*x)*gamma(1+(n+4)*x))
    r=gamma(5*x)*gamma(x)/gamma(3*x)**2
    return h,r
for n in (2,3,5,9,20):
    for p in (1,1.25,1.5,2,2.5,4,12,'inf'):
        h,r=ratios(n,p)
        assert h>0 and 1<r<=6+1e-12
        if p==2: assert isclose(r,3.0,rel_tol=1e-12)
        if p!='inf' and p<2: assert r>3
        if p=='inf' or p>2: assert r<3
        if p=='inf' or p>2:
            klo=h*(r+1)/2
            khi=h*(3+(r-3)/n)
        else:
            klo=h*(2+(r-3)/n)
            khi=h*r
        assert 0<klo<khi
print('GAMMA_REGIME_AND_SHARP_ENDPOINT_CONSISTENCY_OK 40 cases')

# Draw independent signs and Dirichlet/Gamma samples from the normalized ball.
def sample_point(n,p,rng):
    if p=='inf': return [rng.uniform(-1,1) for i in range(n)]
    x=[rng.gammavariate(1/p,1) for i in range(n)]
    s=sum(x)+rng.expovariate(1)
    return [(1 if rng.random()<.5 else -1)*(v/s)**(1/p) for v in x]
for n,p,z in [
    (2,1.0,[(1.,0.),(0.,1.)]),
    (3,1.5,[(1.,0.),(0.,1.),(-1.,0.)]),
    (3,2.0,[(1.,0.),(0.,1.),(0.,0.)]),
    (4,3.0,[(1.,0.),(0.,1.),(0.,0.),(0.,0.)]),
    (3,7.0,[(1.,0.),(1.,0.),(-1.,0.)]),
]:
    h,r=ratios(n,p)
    S=sum(a*a+b*b for a,b in z)
    T=sum((a*a+b*b)**2 for a,b in z)
    q=sum(complex(a,b)**2 for a,b in z)
    expected=h*(2+abs(q)**2/S**2+(r-3)*T/S**2)
    samples=35000
    second=fourth=0.0
    for _ in range(samples):
        x=sample_point(n,p,rng)
        rv=sum(a*v for (a,b),v in zip(z,x)); iv=sum(b*v for (a,b),v in zip(z,x))
        abs2=rv*rv+iv*iv
        second+=abs2; fourth+=abs2*abs2
    approx=(fourth/samples)/(second/samples)**2
    assert abs(approx-expected)<.10,(n,p,approx,expected)
print('INDEPENDENT_RANDOM_BALL_SAMPLING_OK 5 cases; finite consistency only')
print('ALL_COMPLEX_LP_BALL_FOURTH_MOMENT_CHECKS_OK')
