"""Independent reproducibility examples for a sharp antiphase two-cycle criterion.
The universal statement is proved analytically in RESULT.md; finite checks are not its proof.
Run: python verify_antiphase_ricker.py
"""
import math
from scipy.optimize import brentq

def U(L,t):
    return t - 2*math.atanh(t/L)

def root_s(L):
    return brentq(lambda t: U(L,t), 1.e-10, L*(1-1.e-12),xtol=1e-13)

def cycle(X,Y,a,b):
    sX=root_s(X); sY=root_s(Y)
    def w(u): return U(X,u)/a
    # Find earliest crossing of w=sY, or use sX when w never reaches sY.
    lim=sX
    last=1.e-9
    for i in range(1,10001):
        current=sX*i/10000
        if w(current)>=sY:
            lim=brentq(lambda t:w(t)-sY,last,current)
            break
        last=current
    def res(u):return U(Y,w(u))-b*u
    lo=1.e-7;hi=lim
    assert res(lo)>0, (X,Y,a,b,res(lo))
    assert res(hi)<0, (X,Y,a,b,res(hi))
    u=brentq(res,lo,hi,xtol=2e-13)
    v=w(u)
    r=math.exp(X+a*Y);s=math.exp(b*X+Y)
    p=(X+u,Y-v);q=(X-u,Y+v)
    def T(p):return (r*p[0]*math.exp(-p[0]-a*p[1]),s*p[1]*math.exp(-b*p[0]-p[1]))
    err=max(abs(z-z0) for Z,Z0 in ((T(p),q),(T(q),p)) for z,z0 in zip(Z,Z0))
    assert err<3.e-10, (p,q,err)
    return (u,v,err)

for X,Y,a,b in [(3,4,.4,.2),(4.5,3.5,.15,.3),(3,3,.16,.16)]:
    th=(1-2/X)*(1-2/Y)
    assert a*b<th
    u,v,e=cycle(X,Y,a,b)
    print('EXISTENCE',X,Y,a,b,'threshold',th,'amplitudes',round(u,10),round(v,10),'map_error',e)
for X,Y,a,b in [(3,4,1/3,1/2),(3,4,.6,.4),(2,4,.2,.3),(1.5,5,.2,.1)]:
    th=(1-2/X)*(1-2/Y) if X>2 and Y>2 else 0
    assert not (X>2 and Y>2 and a*b<th-1.e-12)
    print('NONEXISTENCE_CRITERION',X,Y,a,b,'threshold',th)
print('VERIFY_OK three_cycle_reconstructions=3 analytic_no_existence_cases=4')
