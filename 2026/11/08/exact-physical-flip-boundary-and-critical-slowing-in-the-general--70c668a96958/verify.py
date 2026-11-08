#!/usr/bin/env python3
"""Standalone reproducibility checks for a cubic Allee-logistic flip theorem."""
from math import sqrt, isfinite
import sympy as s

x, v, m, c, r, delta = s.symbols('x v m c r delta', real=True)
q = (1-x)*(c+m*x)
poly = s.expand(r*x*q)
assert s.expand(poly-r*x*(c+(m-c)*x-m*x*x)) == 0
assert s.expand(s.diff(poly,x,2)/2-r*(m-c-3*m*x)) == 0
assert s.expand(s.diff(poly,x,3)/6+r*m) == 0
qv = s.expand(q.subs(x,v))
flip = s.expand(2*c+3*(m-c)*v-4*m*v*v)
# At a flip, the fixed-point multiplier is -1 iff the displayed quadratic vanishes.
assert s.expand((2*qv + v*s.diff(q,x).subs(x,v))-flip)==0
# Reducing polynomial expressions modulo the flip relation proves coefficient formula.
a = s.expand((s.diff(poly,x,2)/2).subs({x:v,r:1/qv}))
b = s.expand((s.diff(poly,x,3)/6).subs({x:v,r:1/qv}))
a_reduced = -2/v-m*v/qv
assert s.factor((a-a_reduced)*v*qv) == s.factor(flip)
kap = s.factor(a_reduced*a_reduced+b)
assert s.simplify(kap-(4/v**2+3*m/qv+(m*v/qv)**2))==0
# Complete two-iterate cubic coefficient at lambda=-1 is -2(a*a+b).
u,A,B =s.symbols('u A B',real=True)
f0=-u+A*u**2+B*u**3
iter2=s.series(f0.subs(u,f0),u,0,4).removeO()
assert s.expand(iter2-u+2*(A*A+B)*u**3) == 0

cases=[(0.0,0.0),(0.1,0.5),(0.3,0.15),(0.4,0.5),(0.5,0.1),(0.75,0.2),(1.0,0.0)]
count=0
ampl_errors=[]
for M,H in cases:
    C=1-M*(1+H)
    if C < -1e-12: continue
    C=max(C,0.0)
    V=2/3 if M==0 else (3*(M-C)+sqrt(9*(M-C)**2+32*M*C))/(8*M)
    Q=(1-V)*(C+M*V)
    R=1/Q
    K=(4/V**2)+(3*M/Q)+(M*V/Q)**2
    D=3*Q+M*V**2
    assert 2/3-1e-12<=V<=3/4+1e-12
    assert K>0 and D>0
    F=lambda xx,RR: RR*xx*(1-xx)*(C+M*xx)
    DP=lambda xx,RR: RR*(C+2*(M-C)*xx-3*M*xx*xx)
    assert abs(F(V,R)-V)<1e-12 and abs(DP(V,R)+1)<1e-12
    # [0,1] preservation proven in the analytic text; verify fine mesh here.
    for k in range(201):
        xx=k/200
        assert -1e-12<=F(xx,R)<1
        count+=1
    # Critical two-step orbit scaling, starting close enough to attract the flip equilibrium.
    xx=V+0.005
    for j in range(22000):
        xx=F(F(xx,R),R)
    scaled=(xx-V)*sqrt(4*K*22000)
    assert 0.97<scaled<1.03, (M,H,scaled)
    # Two-cycle sampled via many iterations slightly above flip; compare amplitude sqrt law.
    eps=2e-4
    RR=R+eps
    # Upper equilibrium at RR, choosing the larger of the two stationary roots.
    if M==0: fixed=1-1/RR
    else:
        disc=(M-C)**2-4*M*(1/RR-C)
        fixed=((M-C)+sqrt(disc))/(2*M)
    xx=fixed+0.015
    for j in range(45000):
        xx=F(xx,RR)
    yy=F(xx,RR)
    amp=abs(xx-yy)/2
    approx=sqrt(D*eps/K)
    err=abs(amp/approx-1)
    ampl_errors.append(err)
    assert err<0.16,(M,H,amp,approx,err)
    count+=3
print('VERIFY_OK cases=%d exact_symbolic=7 bounded_iterates=%d max_amplitude_relative_error=%.6f' % (len(cases),count,max(ampl_errors)))
