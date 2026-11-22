"""Exact diagonal values and independent finite/numerical checks for Fock big Hankel pairs."""
import math
import numpy as np
from scipy.integrate import quad

def squared(m, beta, n):
    assert m >= 1 and isinstance(m, int) and beta > 0 and np.all(np.asarray(n)>=0)
    n = np.asarray(n, dtype=np.float64)
    k = n+m+1
    a = np.exp(sum(np.log(n+j) for j in range(1,m+1)) - k*np.log1p(2*beta))
    d = 2*np.log1p(beta)-np.log1p(2*beta)
    plus = a*(-np.expm1(-k*d))
    minus = a.copy()
    mask = n >= m
    if np.any(mask):
        q = n[mask]
        factlog = -sum(np.log1p((2*j-1)/(q-j+1)) for j in range(1,m+1))
        lr = factlog + (q+m+1)*np.log1p(2*beta)-2*(q+1)*np.log1p(beta)
        minus[mask] = a[mask]*(-np.expm1(np.minimum(lr,0)))
    return plus, minus

def hs_exact(m,b):
    return math.factorial(m)*((2*b)**(-m-1)-(b*(2+b))**(-m-1))

def gp(m,u):
    return math.exp(-u)*u**((m+1)/2)

def gm(m,u):
    return math.exp(-u)*u**((m-1)/2)*abs(u-m)

count=0
for m in [1,2,3]:
    for b in [0.2,0.07,0.02]:
        n=np.arange(math.ceil(55/b)+10,dtype=float)
        p,q=squared(m,b,n)
        exact=hs_exact(m,b)
        assert np.min(p)>=-1e-12 and np.min(q)>=-1e-12
        assert abs(p.sum()-exact)/exact < 3e-9,(m,b,p.sum(),exact)
        assert abs(q.sum()-exact)/exact < 3e-9,(m,b,q.sum(),exact)
        count += 6

for m in [1,2,3]:
    for u in [0.1, 0.45, 0.9, 1.2, 2.3, 4.6]:
        b=1e-5
        n=int(u/b)
        p,q=squared(m,b,np.asarray([float(n)]))
        sp= math.sqrt(float(p[0]))*b**((m-1)/2)
        sm= math.sqrt(float(q[0]))*b**((m-1)/2)
        assert abs(sp-gp(m,u))<0.0003, (m,u,sp,gp(m,u))
        assert abs(sm-gm(m,u))<0.001, (m,u,sm,gm(m,u))
        count += 2

for m in [1,2,3]:
    b=.002
    n=np.arange(int(34/b),dtype=float)
    p,q=squared(m,b,n)
    for power in [1.,1.5,2.,3.]:
        s=(m-1)*power/2+1
        cm=quad(lambda u:gm(m,u)**power,0,m,epsabs=1e-12)[0]+quad(lambda u:gm(m,u)**power,m,100,epsabs=1e-12)[0]
        cp=quad(lambda u:gp(m,u)**power,0,100,epsabs=1e-12)[0]
        ap=b**s *np.sum(p**(power/2))
        am=b**s *np.sum(q**(power/2))
        assert abs(ap-cp)/cp<0.04,(m,power,ap,cp)
        assert abs(am-cm)/cm<0.04,(m,power,am,cm)
        count+=2

for b in [0.007,0.002]:
    n=np.arange(int(30/b),dtype=float)
    p,q=squared(1,b,n)
    assert abs(b*np.sqrt(p).sum()-1)<0.04
    assert abs(b*np.sqrt(q).sum()-2/math.e)<0.04
    assert abs(math.sqrt(max(p))-1/math.e)<0.02
    assert abs(math.sqrt(max(q))-1)<0.02
    count+=4
print('PASS',count,'assertion groups')
for b in [0.1,0.02,0.005]:
    n=np.arange(int(30/b),dtype=float)
    p,q=squared(1,b,n)
    print('beta',b,'scaled trace +,-',round(b*np.sqrt(p).sum(),7),round(b*np.sqrt(q).sum(),7), 'norm +,-',round(np.sqrt(p.max()),7),round(np.sqrt(q.max()),7))
