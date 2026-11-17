#!/usr/bin/env python3
"""Standalone algebraic and numerical checks for the alternating implicit cubic map."""
from fractions import Fraction as Q
from math import sqrt, asinh, sinh, isclose

def Tinv(y):
    return 2/sqrt(3)*sinh(asinh(3*sqrt(3)*y/2)/3)

def amplitude(a,mu,nu):
    b=Tinv(a)
    return Tinv((1+mu)*b+(2+nu)*b**3)

def H(t,mu,nu):
    return t**4+3*t**3+3*t**2-nu*t-mu

def Hp(t,nu):
    return 4*t**3+9*t**2+6*t-nu

def fold(nu):
    lo,hi=0.0,max(nu,1.0)
    for _ in range(90):
        mid=(lo+hi)/2
        if Hp(mid,nu)>0: hi=mid
        else: lo=mid
    t=(lo+hi)/2
    return t,-3*t*t*(1+t)**2

def roots(mu,nu):
    pts=[0.0]
    if nu>0: pts.append(fold(nu)[0])
    upper=max(1.,abs(mu)+abs(nu)+5.)
    pts.append(upper)
    output=[]
    for left,right in zip(pts,pts[1:]):
        vl,vr=H(left,mu,nu),H(right,mu,nu)
        if abs(vl)<1e-11 and left>0:
            output.append(left)
        if vl*vr<0:
            lo,hi=left,right
            for _ in range(100):
                mid=(lo+hi)/2
                if H(mid,mu,nu)*vl>0:lo=mid
                else:hi=mid
            output.append((lo+hi)/2)
    return output

def check():
    n=0
    for bb in [Q(1,10),Q(1,4),Q(1,2),Q(1),Q(3,2),Q(2)]:
        t=bb*bb; a=bb+bb**3
        for nu in [Q(-3,2),Q(-1,3),Q(0),Q(1,3),Q(3)]:
            mu=t*((1+t)**3-1-nu)
            assert (1+mu)*bb+(2+nu)*bb**3==a+a**3
            B=(1+3*t)*(1+3*a*a)
            A=1+mu+3*(2+nu)*t
            assert B-A==2*t*Hp(t,nu)
            n+=1
    for t in [Q(1,100),Q(1,5),Q(1,2),Q(1),Q(2)]:
        nu=6*t+9*t*t+4*t**3
        mu=-3*t*t*(1+t)**2
        assert H(t,mu,nu)==0 and Hp(t,nu)==0
        n+=1
    # Distinct phase portraits and an exact fold.
    tests=[(-.2,-.5,0),(.3,-.2,1),(0.,0.,0),(0.,.5,1),(-.01,.5,2),(-.03,.5,0),(.1,.5,1)]
    for mu,nu,expected in tests:
        rr=roots(mu,nu)
        assert len(rr)==expected, (mu,nu,rr)
        for t in rr:
            b=sqrt(t); a=b+b**3
            assert isclose(amplitude(a,mu,nu),a,abs_tol=2e-10)
            fprime=((1+mu)+3*(2+nu)*t)/((1+3*t)*(1+3*a*a))
            assert (fprime<1)==(Hp(t,nu)>0)
            n+=1
    t,mu=fold(.5)
    assert isclose(amplitude(sqrt(t)*(1+t),mu,.5),sqrt(t)*(1+t),abs_tol=1e-11)
    n+=1
    # Global basin checks for strict coexistence (-0.01,0.5).
    mu,nu=-.01,.5
    tlo,thi=roots(mu,nu)
    lo=sqrt(tlo)*(1+tlo); hi=sqrt(thi)*(1+thi)
    for a0,expected in [(lo*.5,0.0),(lo*.999,0.0),(lo*1.001,hi),(hi*1.2,hi),(3.0,hi)]:
        a=a0
        for k in range(30000): a=amplitude(a,mu,nu)
        assert abs(a-expected)<1e-7,(a0,expected,a)
        n+=1
    # Quintic degeneracy, k a_k^4 -> 1/12.
    a=.7
    for k in range(200000): a=amplitude(a,0.0,0.0)
    clock=200000*a**4
    assert abs(clock-1/12)<.003,clock
    n+=1
    # Cubic-degenerate stable case, k a_k^2 -> -1/(2 nu).
    a=.7; nu=-.5
    for k in range(100000): a=amplitude(a,0.0,nu)
    clock=100000*a*a
    assert abs(clock-1)<.02,clock
    n+=1
    print('VERIFY_OK exact_rational_identities=35 root_and_multiplier_cases=7 basin_cases=5 critical_clocks=2 total_checks='+str(n))

if __name__=='__main__':check()
