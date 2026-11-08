#!/usr/bin/env python3
"""Arithmetic probes for the two-species Ricker two-cycle equation.
Finite checks only; the mathematical argument is analytic.
"""
import mpmath as mp
from fractions import Fraction

assert (Fraction(2,1)/Fraction(3,2) - 1)**2 == Fraction(1,3)**2
mp.mp.dps = 95

def psi(X,u):
    return 2*mp.atanh(u/X)-u

def solve(X,Y,alpha,beta):
    X,Y,alpha,beta=map(mp.mpf,(X,Y,alpha,beta))
    th=(2/X-1)*(2/Y-1)
    present=alpha*beta>th+mp.mpf("1e-65")
    if not present:
        return {'present':False,'gap':str(alpha*beta-th)}
    left=mp.mpf('0'); right=X
    for _ in range(240):
        mid=(left+right)/2
        v=psi(X,mid)/alpha
        if v>=Y: right=mid
        else: left=mid
    cap=(left+right)/2
    def val(u):
        v=psi(X,u)/alpha
        return (psi(Y,v)/v)*(psi(X,u)/u)/(alpha*beta)-1
    lo=mp.mpf('1e-8')*min(X,cap); hi=cap*(1-mp.mpf('1e-8'))
    assert val(lo)<0 and val(hi)>0,(val(lo),val(hi))
    for _ in range(300):
        m=(lo+hi)/2
        if val(m)>0:hi=m
        else:lo=m
    u=(lo+hi)/2
    v=psi(X,u)/alpha
    r=mp.exp(X+alpha*Y); s=mp.exp(Y+beta*X)
    def T(x,y):return (r*x*mp.exp(-x-alpha*y),s*y*mp.exp(-y-beta*x))
    a=(X+u,Y+v);b=(X-u,Y-v)
    e=max(abs(z-w) for z,w in zip(T(*a),b))
    f=max(abs(z-w) for z,w in zip(T(*b),a))
    assert e<mp.mpf('1e-65') and f<mp.mpf('1e-65'),(e,f)
    return {'present':True,'u':mp.nstr(u,18),'v':mp.nstr(v,18),'max_residual':mp.nstr(max(e,f),5)}

tests=[('1.5','1.6','0.3','0.4'),('1.2','1.5','0.2','0.2'),('2','1','0.25','0.5'),('1','1','2','2'),('1.9','1.6','0.1','0.1'),('1.8','1.8','0.4','0.4'),('1.5','1.5',mp.mpf(1)/3,mp.mpf(1)/3)]
for i,t in enumerate(tests):
    ans=solve(*t)
    print('CASE',i+1,'threshold_product',mp.nstr((2/mp.mpf(t[0])-1)*(2/mp.mpf(t[1])-1),8), 'result',ans)
print('VERIFY_OK finite_parameter_cases=7 analytic_proof_required=1')
