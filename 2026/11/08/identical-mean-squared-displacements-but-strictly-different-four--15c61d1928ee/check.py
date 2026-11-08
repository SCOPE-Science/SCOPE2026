"""Deterministic independent checks of ordered fourth cumulants in two stationary dimer force models."""
import math
import numpy as np
from scipy.integrate import quad
from numpy.linalg import eigvalsh

def F(c,d,T):
    return quad(lambda s: s*math.exp(-c*s)*((T-s)/d+math.expm1(-d*(T-s))/d**2),0,T,epsabs=5e-12,epsrel=5e-12)[0]

def predicted(a,b,A,B,T):
    c=a+b
    fg=48*(A*B)**2*(F(c,2*a,T)+F(c,2*b,T)+F(c,2*c,T))
    ft=48*(A*B)**2*(F(c,2*a,T)-F(c,2*c,T))
    return fg,ft

def four_cumulant_sorted(a,b,A,B,x,y,z,tele):
    ts=np.cumsum([0,x,y,z])
    def cov(d,v,i,j): return v*math.exp(-d*abs(ts[i]-ts[j]))
    pairs=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
    qy=sum(cov(a,A,i,j)*cov(a,A,k,l) for (i,j),(k,l) in pairs)
    if tele:
        qu=B**2*math.exp(-b*(x+z))
    else:
        qu=sum(cov(b,B,i,j)*cov(b,B,k,l) for (i,j),(k,l) in pairs)
    raw=qy*qu
    sub=sum((cov(a,A,i,j)*cov(b,B,i,j))*(cov(a,A,k,l)*cov(b,B,k,l)) for (i,j),(k,l) in pairs)
    return raw-sub

rng=np.random.default_rng(417)
ct=0
for t in range(40):
    a,b,A,B=np.exp(rng.uniform(-1,1,4))
    x,y,z=np.exp(rng.uniform(-1.5,0.4,3))
    for tele in [False,True]:
        got=four_cumulant_sorted(a,b,A,B,x,y,z,tele)
        c=a+b
        rhs=2*(A*B)**2*math.exp(-c*(x+z))*((math.exp(-2*a*y)-math.exp(-2*c*y)) if tele else (math.exp(-2*a*y)+math.exp(-2*b*y)+math.exp(-2*c*y)))
        assert abs(got-rhs)<1e-11*(1+abs(rhs)),(got,rhs)
        ct+=1
    T=float(math.exp(rng.uniform(-0.3,1.6)))
    g,h=predicted(a,b,A,B,T)
    assert g>h>0
    assert abs(g-h-48*(A*B)**2*(F(c,2*b,T)+2*F(c,2*c,T)))<1e-10*max(1,g)
    ct+=2
for a,b,A,B in [(1.1,0.7,0.8,1.3),(2,2,0.4,0.2),(0.3,4,2,1)]:
    for T in [10,50,200]:
        g,h=predicted(a,b,A,B,T)
        lg=24*(A*B)**2/(a+b)**2*(1/a+1/b+1/(a+b))
        lt=24*(A*B)**2/(a+b)**2*(1/a-1/(a+b))
        assert abs(g/T/lg-1)<12/T, (g/T/lg,T)
        assert abs(h/T/lt-1)<12/T, (h/T/lt,T)
        ct+=2
    # Numeric trace version for Gaussian product integral (Nyström midpoint covariance operators)
    T=1.8; n=180; w=T/n
    grid=(np.arange(n)+0.5)*w
    Cu=B*np.exp(-b*np.abs(grid[:,None]-grid[None,:]))*w
    Cy=A*np.exp(-a*np.abs(grid[:,None]-grid[None,:]))*w
    evals=eigvalsh(Cu)
    assert evals.min()>0
    # For Z=int_0^T u(t)y(t) dt, kappa4(Z)=6 tr((Cu Cy)^2)
    num=6*np.trace(Cu@Cy@Cu@Cy)
    g,_=predicted(a,b,A,B,T)
    assert abs(num/g-1)<0.004,(num,g,num/g)
    ct+=1
for a,b in [(1,0.2),(2,2),(0.3,3)]:
    A=B=1
    for T in [.003,.006]:
        g,h=predicted(a,b,A,B,T)
        assert abs(g/(6*T**4)-1)<.06
        assert abs(h/(0.8*b*T**5)-1)<.06,(h,T)
        ct+=2
# strict positivity and exponential variance bound for telegraph: ||u||_2^2=B*T; ||Cy||<=2A/a.
print('PASS checks',ct,'; algebra/Wick, positivity, rates, Nyström, short-time')
