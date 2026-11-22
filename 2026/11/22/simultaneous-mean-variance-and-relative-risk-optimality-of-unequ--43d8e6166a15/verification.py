"""Reproduce exact first-contact moment and rate-allocation identities.

Run: python verification.py  (Python 3 and SymPy required).
Optional deterministic event-driven sampling checks are included.
"""
from __future__ import annotations
import math
import random
from fractions import Fraction
import sympy as S

x,L,v,g,k=S.symbols('x L v g k', positive=True)
delta_squared=1-2*k/g
fm=x/v+k*x*(L-x)/(2*v**2)
fp=(L-x)/v+k*x*(L-x)/(2*v**2)
f=fm+fp
d=fm-fp
D0=-L*(L**2*g*k+6*L*g*v+6*v**2)/(6*g*v**3)
D=S.expand(D0+2*L*x/v**2+k*(L*x**2-2*x**3/3)/v**3+2*x/(g*v))
I=S.expand(D0*x+L*x**2/v**2+k*(L*x**3/3-x**4/6)/v**3+x**2/(g*v))
T=S.expand(-D0+(1+delta_squared)*(x**2-L*x)/v**2-k*I/v)
GM=S.expand((T+D)/2)
GP=S.expand((T-D)/2)
Fbar=L/(2*v)+k*L**2/(12*v**2)+1/(2*g)
Gbar=S.factor(S.integrate(T/2+f/(2*g)+1/g**2,(x,0,L))/L)
Gtarget=(L/v)**2*((k*L/v)**2+10*(k*L/v)+20+20*k/g+60*v/(g*L)+60*v**2/(g*L)**2)/60
Vbar=S.factor(Gbar-Fbar**2)
Vtarget=(L/v)**2*(7*(k*L/v)**2+60*(k*L/v)+60+180*k/g+360*v/(g*L)+540*v**2/(g*L)**2)/720

assert S.simplify(Gbar-Gtarget)==0
assert S.simplify(Vbar-Vtarget)==0
assert S.simplify(D.subs(x,0)+T.subs(x,0))==0
assert S.simplify(T.subs(x,L)-D.subs(x,L))==0
assert S.simplify(S.diff(D,x)-(2*f+2/g)/v)==0
assert S.simplify(S.diff(T,x)-((1+delta_squared)*d-k*D)/v)==0
assert S.simplify(S.diff(fm,x)-(2-k*d)/(2*v))==0
assert S.simplify(S.diff(fp,x)-(-2-k*d)/(2*v))==0
assert S.simplify(fm.subs(x,0))==0
assert S.simplify(fp.subs(x,L))==0

# Exact four-state backward equations with independent unequal reversal rates.
a,b=S.symbols('a b', positive=True)
subs={g:a+b,k:2*a*b/(a+b)}
FM=S.factor(fm.subs(subs)); FP=S.factor(fp.subs(subs))
FC=(1+a*FP+b*FM)/(a+b)
FD=(1+a*FM+b*FP)/(a+b)
GM4=GM.subs(subs); GP4=GP.subs(subs)
GC=(2*FC+a*GP4+b*GM4)/(a+b)
GD=(2*FD+a*GM4+b*GP4)/(a+b)
# First backward equations for states A=(-2v), B=(+2v), C=(0), D=(0).
checks=[
 -2*v*S.diff(FM,x)+a*(FD-FM)+b*(FC-FM)+1,
  2*v*S.diff(FP,x)+a*(FC-FP)+b*(FD-FP)+1,
 a*(FP-FC)+b*(FM-FC)+1,
 a*(FM-FD)+b*(FP-FD)+1,
 -2*v*S.diff(GM4,x)+a*(GD-GM4)+b*(GC-GM4)+2*FM,
  2*v*S.diff(GP4,x)+a*(GC-GP4)+b*(GD-GP4)+2*FP,
 a*(GP4-GC)+b*(GM4-GC)+2*FC,
 a*(GM4-GD)+b*(GP4-GD)+2*FD,
]
for i, expr in enumerate(checks):
    assert S.cancel(S.together(expr))==0, f'generator residual {i}'

r,h=S.symbols('r h',positive=True)
cv=(7*r**2*h**2+60*r**2*h+60*r**2+180*r*h+360*r+540)/(5*(r*h+6*r+6)**2)
d_cv=24*r**2*(r*h+10*r-4*h+30)/(5*(r*h+6*r+6)**3)
assert S.factor(S.diff(cv,h)-d_cv)==0
assert S.simplify((Gbar-Vbar)-Fbar**2)==0

# Simulate event-driven paths independently of the moment ODEs.
def sample(rng, a0, b0, L0=1.0, v0=1.0):
    xx=rng.random()*L0
    s1=1 if rng.random()<.5 else -1
    s2=1 if rng.random()<.5 else -1
    G=a0+b0
    elapsed=0.0
    while True:
        velocity=v0*(s2-s1)
        flight=(xx/(-velocity)) if velocity<0 else ((L0-xx)/velocity if velocity>0 else math.inf)
        event=rng.expovariate(G)
        if flight<event:
            return elapsed+flight
        elapsed+=event
        xx+=velocity*event
        # trajectories cannot cross before the event (flight check above)
        if rng.random()<a0/G:
            s1=-s1
        else:
            s2=-s2

def predictions(a0,b0):
    G=a0+b0
    K=2*a0*b0/G
    mean=0.5+K/12+1/(2*G)
    var=(7*K*K+60*K+60+180*K/G+360/G+540/(G*G))/720
    return mean,var

rng=random.Random(20261117)
for a0,b0 in ((0.0,3.0),(0.5,2.5),(1.5,1.5), (0.65,0.8)):
    N=60000
    ys=[sample(rng,a0,b0) for _ in range(N)]
    mean=sum(ys)/N
    variance=sum((z-mean)**2 for z in ys)/N
    m,vv=predictions(a0,b0)
    # Conservative deterministic Monte Carlo tolerances, not used as proof.
    assert abs(mean-m)<0.05*m, (a0,b0,mean,m)
    assert abs(variance-vv)<0.11*vv, (a0,b0,variance,vv)

print('PASS: 10 symbolic identities, 8 symbolic generator equations,')
print('      2 algebraic risk identities, and 240000 independent event-driven paths.')
