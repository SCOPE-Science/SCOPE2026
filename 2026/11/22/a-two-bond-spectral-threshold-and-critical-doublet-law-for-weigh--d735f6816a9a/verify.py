"""Numerical consistency checks for a two-bond Jacobi spectral formula.

Not an exhaustive or computer-assisted infinite-dimensional proof.
"""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import brentq

def roots(m, a):
    beta=a*a-1.0
    fp=lambda z: a*a*z*z+beta*z**(m+1)-1.0
    zp=brentq(fp,1e-12,1.0,xtol=1e-14)
    zm=None
    if beta>2/(m-1):
        fm=lambda z: a*a*z*z-beta*z**(m+1)-1.0
        zm=brentq(fm,1.0/a,1.0-1e-11,xtol=1e-14)
    return zp,zm

def energy(z): return (z+1/z)/2

def finite(m,a,pad=130):
    n=2*pad+m+3
    b=np.ones(n-1)/2
    b[pad]=a/2
    b[pad+m]=a/2
    return eigh_tridiagonal(np.zeros(n),b,select='i',select_range=(n-3,n-1),eigvals_only=True)

count=0
for m in (2,3,4,5,8,12,20):
 for a in (1.05,1.2,1.4,1.7,2.0,2.6):
    zp,zm=roots(m,a)
    assert 0<zp<1/a
    assert (zm is not None)==(a*a-1 > 2/(m-1))
    v=finite(m,a)
    ep=energy(zp)
    if ep>1.0005:
      assert abs(ep-v[-1])<2e-6,(m,a,ep,v[-1])
    if zm is not None and energy(zm)>1.001:
      assert abs(energy(zm)-v[-2])<2e-6,(m,a,energy(zm),v[-2])
    count+=1
print('Finite Jacobi comparisons and thresholds:',count)

for a in (1.3,1.7,2.0):
 for m in (12,16,20):
    zp,zm=roots(m,a)
    pred=(a*a-1)**2/(2*a**(m+2))
    diff=energy(zp)-energy(zm)
    assert abs(diff/pred-1)<0.28,(a,m,diff/pred)
    print('split',a,m, 'ratio',round(diff/pred,9))

def kappa(gamma,sign):
    f=lambda x: 2*x-gamma*(1+sign*math.exp(-x))
    if sign==1: return brentq(f,1e-12,2*gamma+2)
    assert gamma>2
    return brentq(f,1e-8,2*gamma+2)
for gamma in (0.5,1.5,2.0,3.0,5.0):
 kp=kappa(gamma,1)
 for m in (80,160,320):
    a=math.sqrt(1+gamma/m)
    zp,zm=roots(m,a)
    ap=m*m*(energy(zp)-1)
    assert abs(ap-kp*kp/2)<0.25
    if gamma>2:
      km=kappa(gamma,-1)
      assert zm is not None
      am=m*m*(energy(zm)-1)
      assert abs(am-km*km/2)<0.25
    else:
      assert zm is None
 print('critical gamma',gamma,'plus limit',kp*kp/2)
print('CHECKS PASSED')
