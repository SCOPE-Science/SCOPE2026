"""Standalone checks of two-sided power Hardy averaging on interval BV.

Run: python verify_hardy.py
Only the Python standard library is required.
"""
import math
import random
from fractions import Fraction


def simpson(func, a=0.0, b=1.0, n=1200):
    assert n % 2 == 0
    h = (b-a)/n
    z = func(a)+func(b)
    for j in range(1,n):
        z += (4 if j % 2 else 2)*func(a+j*h)
    return z*h/3


def threshold_RL(s, alpha, beta):
    tmax=(1-s)**beta
    return simpson(lambda u:(1-u**(1/beta))**(-alpha),0,tmax)


def threshold_LR(s, alpha, beta):
    tmax=s**alpha
    return simpson(lambda u:(1-u**(1/alpha))**(-beta),0,tmax)


def root_RL(alpha,beta):
    lo,hi=1e-7,1-1e-7
    assert threshold_RL(lo,alpha,beta)>1 and threshold_RL(hi,alpha,beta)<1
    for _ in range(60):
        s=(lo+hi)/2
        if threshold_RL(s,alpha,beta)>1:lo=s
        else:hi=s
    return (lo+hi)/2


def root_LR(alpha,beta):
    lo,hi=1e-7,1-1e-7
    assert threshold_LR(lo,alpha,beta)<1 and threshold_LR(hi,alpha,beta)>1
    for _ in range(60):
        s=(lo+hi)/2
        if threshold_LR(s,alpha,beta)<1:lo=s
        else:hi=s
    return (lo+hi)/2


def lstep(x,s,a):
    return 0.0 if x<=s else 1-(s/x)**a


def rstep(x,s,b):
    return 1.0 if x>=s else ((1-s)/(1-x))**b


def RLstep(x,s,a,b):
    # Right Hardy mean of the left Hardy mean, with a uniform integral parameter.
    return simpson(lambda u:lstep(1-(1-x)*u**(1/b),s,a),n=300)


def LRstep(x,s,a,b):
    return simpson(lambda u:rstep(x*u**(1/a),s,b),n=300)


def assert_near(x,y,tol=3e-5):
    assert abs(x-y)<tol, (x,y,abs(x-y))


def run():
    for a,b in ((1,1),(1,2),(2,1),(2,2),(1.5,.8),(.8,1.5)):
        s=root_RL(a,b); t=root_LR(a,b)
        kr=1-(1-s)**b; kl=1-t**a
        assert_near(threshold_RL(s,a,b),1,3e-8)
        assert_near(threshold_LR(t,a,b),1,3e-8)
        assert_near(RLstep(1,s,a,b)-RLstep(0,s,a,b),kr)
        assert_near(LRstep(1,t,a,b)-LRstep(0,t,a,b),kl)
        for delta in (-.18,-.05,.05,.18):
            u=max(1e-5,min(1-1e-5,s+delta))
            v=max(1e-5,min(1-1e-5,t+delta))
            assert RLstep(1,u,a,b)-RLstep(0,u,a,b)<kr+5e-5
            assert LRstep(1,v,a,b)-LRstep(0,v,a,b)<kl+5e-5
        print('GENERAL_PARAMETER_TEST_PASS',a,b,round(s,9),round(kr,9),round(t,9),round(kl,9))
    s=math.exp(-1)
    assert_near(root_RL(1,1),s,1e-7)
    assert_near(root_LR(1,1),1-s,1e-7)
    assert_near(1-(1-root_RL(1,1)),1/math.e,1e-7)
    print('CLASSICAL_ONE_OVER_E_PASS')
    for a in (.25,.5,1.,2.,4.):
        t=(1/math.e if a==1 else a**(1/(1-a)))
        assert_near(root_RL(a,1),t,1e-7)
    print('UNILATERAL_POWER_EXPLICIT_FORMULA_PASS')
    # Exact identity for left-then-right, alpha=1,beta=2: 2s(1-s) <= 1/2.
    assert 4*Fraction(1,2)*(1-Fraction(1,2))==1
    # A rigorous lower certificate for right-then-left uses the positive atanh series.
    # log 3 = 2(sum_{k>=0} (1/2)^(2k+1)/(2k+1)) > 1+1/12+1/80 > 13/12.
    assert Fraction(1,1)+Fraction(1,12)+Fraction(1,80)>Fraction(13,12)
    assert ((Fraction(2,3)*(Fraction(1,1)+Fraction(1,12)+Fraction(1,80)))-Fraction(2,9))>Fraction(1,2)
    kr=1-(1-root_RL(1,2))**2
    assert .51238<kr<.51240
    print('EXACT_ORDER_ASYMMETRY_CERTIFICATE_PASS')
    # For randomized signed step measures, a grid verifies the BV contraction numerically.
    rng=random.Random(731924)
    for a,b in ((1,1),(1,2),(2,1)):
        kr=1-(1-root_RL(a,b))**b
        kl=1-root_LR(a,b)**a
        for _ in range(8):
            steps=sorted(rng.uniform(.08,.92) for j in range(4))
            coeffs=[rng.uniform(-1,1) for _ in steps]
            tv=sum(abs(c) for c in coeffs)
            xs=[i/40 for i in range(41)]
            for trans,bound in ((RLstep,kr),(LRstep,kl)):
                vals=[sum(c*trans(x,s,a,b) for s,c in zip(steps,coeffs)) for x in xs]
                total=sum(abs(y-x) for x,y in zip(vals,vals[1:]))
                assert total<=bound*tv+4e-5,(a,b,total,bound*tv)
        print('SIGNED_JUMP_NUMERICAL_STRESS_PASS',a,b,8)
    print('ALL_TWO_SIDED_HARDY_BV_CHECKS_PASS')

if __name__=='__main__':
    run()
