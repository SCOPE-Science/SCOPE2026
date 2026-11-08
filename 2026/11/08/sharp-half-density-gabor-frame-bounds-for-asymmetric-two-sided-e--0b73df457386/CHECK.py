"""Independent finite checks for sharp half-density asymmetric exponential Gabor frame bounds.
Run: python CHECK.py (requires numpy only).
"""
import math
import numpy as np


def exact(alpha, beta):
    r, s = math.exp(-alpha), math.exp(-beta)
    p = 1 / (1 + r*r)
    h = s*s / (1 + s*s)
    q = s*(s+r) / ((1+r*r)*(1+s*s))
    root = (2*alpha*p) / (math.sqrt((alpha-beta)**2*q*q+4*alpha*beta*p*h)+(alpha-beta)*q)
    # This rationalized expression is stable when beta exceeds alpha.
    # Note: root is y_*, since multiplying numerator and denominator by conjugate.
    x = min(1., max(0., math.log(root) / (alpha+beta)))
    lower = 2*(p*math.exp(-2*alpha*x) + h*math.exp(2*beta*x) - 2*q*math.exp((beta-alpha)*x))
    upper = 2*((1/(1-r*r) + s*s/(1-s*s))**2 + (r/(1-r*r) + s/(1-s*s))**2)
    return lower, upper, x

def raw_multiplier(alpha,beta,x,omega,cut=160):
    k=np.arange(-cut,cut+1)
    t=x+k
    g=np.where(t>=0,np.exp(-alpha*np.maximum(t,0)),np.exp(beta*np.minimum(t,0)))
    z0=np.sum(g*np.exp(-2j*np.pi*k*omega))
    z1=np.sum(g*np.exp(-2j*np.pi*k*(omega+0.5)))
    return float(abs(z0)**2+abs(z1)**2)

def fiber(alpha,beta,x,c):
    r,s=math.exp(-alpha),math.exp(-beta)
    R,S=r*r,s*s
    A,B=math.exp(-alpha*x),math.exp(beta*x)
    P=A-B*R*S
    Q=S*(B-A)
    C=r*(A-r*s*B)
    D=s*(B-r*s*A)
    return 2*(P*P+Q*Q+C*C+D*D+2*(P*Q+C*D)*c)/((1+R*R-2*R*c)*(1+S*S-2*S*c))

cases=[(1.,1.),(1.,2.),(2.,1.),(0.2,3.),(3.,0.2),(0.5,0.75),(2.2,3.6),(.9,.31)]
checks=0
for a,b in cases:
    lo,hi,xstar=exact(a,b)
    assert 0<=xstar<=1 and 0<lo<=hi
    for xx in np.linspace(0,1,17):
        for ww in np.linspace(0,0.5,19):
            c=math.cos(4*math.pi*ww)
            val=raw_multiplier(a,b,xx,ww)
            closed=fiber(a,b,xx,c)
            assert abs(val-closed)<3e-9*max(1.,closed),(a,b,xx,ww,val,closed)
            assert lo-1e-9<=val<=hi+1e-9,(a,b,xx,ww,val,lo,hi)
            checks+=1
    assert abs(fiber(a,b,xstar,-1)-lo)<1e-8
    assert abs(fiber(a,b,0.,1)-hi)<1e-8
    assert abs(fiber(a,b,1.,1)-hi)<1e-8
    lr,ur,xr=exact(b,a)
    assert abs(lo-lr)<2e-9 and abs(hi-ur)<2e-9 and abs(xstar+xr-1)<2e-8
    checks+=6
# Independently reduce the symmetric case to the known integer-oversampling formula at q=2.
for alpha in [.25,.75,1.5,3.]:
    r=math.exp(-alpha)
    lo,hi,xstar=exact(alpha,alpha)
    alo=4*r*(1-r)**2/(1+r*r)**2
    bhi=2*((1+r*r)**2+4*r*r)/(1-r*r)**2
    assert abs(lo-alo)<1e-10 and abs(hi-bhi)<1e-10
    assert abs(xstar-0.5)<1e-12
    checks+=3
print('ASYMMETRIC_HALF_DENSITY_GABOR_CHECKS_PASSED',checks)
