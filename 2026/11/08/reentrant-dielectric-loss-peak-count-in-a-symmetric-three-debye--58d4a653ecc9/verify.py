"""Reproduce the exact reentrant modal classification for a symmetric three-Debye spectrum.

Run: python3 verify.py. Standard library only.
"""
from fractions import Fraction
from math import cosh, exp, log, sqrt

A = Fraction(53, 100)
S0 = 4*A

def cubic(s):
    return float(A)*s**3 - 2*s*s + 4

def root_between(lo, hi):
    fl = cubic(lo)
    assert fl*cubic(hi) < 0
    for _ in range(100):
        mid = (lo+hi)/2
        if cubic(mid)*fl>0:
            lo=mid
            fl=cubic(lo)
        else:
            hi=mid
    return (lo+hi)/2

def q(z, a, s):
    B=s*s-1
    return (a+2*s)*z*z + 2*B*(a-s)*z + a*B*B

def zeros(s, a):
    assert s>4*a
    rad=s*(s-4*a)
    B=s*s-1
    return (B*(s-a-sqrt(rad))/(a+2*s), B*(s-a+sqrt(rad))/(a+2*s))

def exact_checks():
    # Check the noncentral double root and discriminant identities in rational arithmetic.
    b=S0*S0-1
    z0=b/3
    p=A+2*S0
    assert q(z0,A,S0)==0
    assert q(Fraction(2)*z0,A,S0)==p*z0*z0
    assert q(Fraction(0),A,S0)==p*z0*z0
    assert z0>1
    assert (S0*S0-4)**2 == 4*S0**3*(S0/Fraction(4)-2*(S0*S0-2)/S0**3)
    s1=root_between(2.16,2.18)
    s2=root_between(2.83,2.84)
    assert float(S0)<s1<sqrt(6)<s2
    assert abs(cubic(s1))<1e-12 and abs(cubic(s2))<1e-12
    amax=4/(3*sqrt(6))
    assert .5<float(A)<amax
    return s1,s2

def dlog_loss(y, r, a):
    # Independent derivative from the original three individual Debye terms.
    ell=log(r)
    def ds(t):
        u=exp(-abs(t))
        sech=2*u/(1+u*u)
        tanh=(1-u*u)/(1+u*u)
        if t<0:tanh=-tanh
        return -sech*tanh/2
    return ds(y+ell)+a*ds(y)+ds(y-ell)

def root_count(a,s):
    r=s+sqrt(s*s-1)
    # Only y>0. Ignore the always-stationary center y=0.
    M=30000
    yprev=1e-5
    vprev=dlog_loss(yprev,r,a)
    changes=[]
    for i in range(1,M+1):
        y=10*i/M
        val=dlog_loss(y,r,a)
        if val*vprev<0:
            changes.append((yprev,y))
        yprev,vprev=y,val
    return changes

def numerical_checks(s1,s2):
    cases=[(2.1,1),(2.13,3),(2.3,2),(4.0,3)]
    for s,peaks in cases:
        crossings=root_count(float(A),s)
        observed=1+len(crossings) if peaks==3 else (2 if len(crossings)==1 else 1)
        # For three maxima, two positive derivative roots; for two maxima one.
        expected_crossings={1:0,2:1,3:2}[peaks]
        assert len(crossings)==expected_crossings,(s,crossings)
        if s>float(S0):
            zl,zu=zeros(s,float(A))
            assert zu>1
            assert (zl>1)==(peaks==3)
            predicted=[log(sqrt(v)+sqrt(v-1)) for v in [zl,zu] if v>1]
            for (left,right),y in zip(crossings,predicted):
                assert left<=y<=right,(s,y,left,right)
        print('s=',s,'r=',s+sqrt(s*s-1),'local maxima=',peaks,'noncentral stationary pairs=',len(crossings))
    # Direct numerical check of the reciprocal-frequency symmetry and rational reduction.
    for s in (1.1,2.1,2.13,2.3,4,7):
        r=s+sqrt(s*s-1)
        for y in (-3,-1,-.2,0,.2,1,3):
            x=exp(y)
            direct=sum(w*(x*t)/(1+(x*t)**2) for w,t in ((1,1/r),(float(A),1),(1,r)))
            c=cosh(y)
            reduced=float(A)/(2*c)+s*c/(c*c+s*s-1)
            assert abs(direct-reduced)<2e-14
    # Verify the centered transition roots lie at the bottom of the outer-root interval.
    for s in (s1,s2):
        zl,zu=zeros(s,float(A))
        assert abs(zl-1)<1e-12 and zu>1
    print('s1=',repr(s1),'s2=',repr(s2))
    print('r0=',float(S0)+sqrt(float(S0)**2-1))
    print('r1=',s1+sqrt(s1*s1-1),'r2=',s2+sqrt(s2*s2-1))
    print('All checks passed')

if __name__=='__main__':
    s1,s2=exact_checks()
    numerical_checks(s1,s2)
