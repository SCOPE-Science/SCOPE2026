#!/usr/bin/env python3
"""Reproduce exact near-capacity charging equilibrium moment identities."""
from fractions import Fraction as F

C=F(300)
W=F(30)
U_TOTAL=F(25)
V_TOTAL=F(2500,3)

# These identities are valid for -6 < threshold < -3/2.
def mass0(t): return F(3,8)-t/F(30)
def u0(t): return F(25,3)-F(5,6)*t
def v0(t): return F(3125,12)-F(250,9)*t

assert mass0(F(-5)) == F(13,24)
assert u0(F(-5)) == F(25,2)
assert v0(F(-5)) == F(14375,36)
assert V_TOTAL-v0(F(-5)) == F(15625,36)
assert v0(F(-5))/V_TOTAL == F(23,48)
assert (V_TOTAL-v0(F(-5)))/V_TOTAL == F(25,48)
assert W*F(24)*V_TOTAL/(2*C) == F(1000)
assert (F(23,48)-F(1,2))/F(4,5) == F(-5,192)

def waiting(t, lam, i):
    u = float(u0(F(t))) if i==0 else float(U_TOTAL-u0(F(t)))
    v = float(v0(F(t))) if i==0 else float(V_TOTAL-v0(F(t)))
    delta = 300-lam*u
    assert delta>0
    return 30*lam*lam*u*v/(300*(300*300-lam*lam*u*u))

def root(lam):
    # U0 decreases in t; capacity feasibility bounds the root interval.
    lo = (float(F(25,3))-300/lam)*6/5
    hi = (float(F(25,3))-(25-300/lam))*6/5
    assert -6<lo<hi<-1.5
    pad=(hi-lo)*1e-8
    lo+=pad; hi-=pad
    def residual(t): return waiting(t,lam,0)-waiting(t,lam,1)-t
    assert residual(lo)>0>residual(hi)
    for _ in range(85):
        mid=(lo+hi)/2
        if residual(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

for lam in (23.9,23.99,23.999):
    t=root(lam)
    eta=24-lam
    eps=25*eta
    d0=300-lam*float(u0(F(t)))
    d1=300-lam*(25-float(u0(F(t))))
    assert abs((d0+d1)-eps) < 5e-10
    assert abs((waiting(t,lam,0)-waiting(t,lam,1))-t)<3e-6
    print('lambda=',lam,'threshold=',t,'station0_slack_share=',d0/eps,
          'scaled_wait0=',eps*waiting(t,lam,0),'scaled_wait1=',eps*waiting(t,lam,1))
    if lam>=23.999:
        assert abs(d0/eps-float(F(23,48)))<0.00005
        assert abs(eps*waiting(t,lam,0)-1000)<0.2
        assert abs(eps*waiting(t,lam,1)-1000)<0.02
        assert abs((t+5)/eta-float(F(-5,192)))<0.0001
print('ALL EXACT IDENTITIES AND NUMERICAL CONSISTENCY TESTS PASS')
