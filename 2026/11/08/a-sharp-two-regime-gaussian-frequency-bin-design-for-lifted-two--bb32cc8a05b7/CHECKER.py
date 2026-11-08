import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar
from numpy.linalg import svd
N=4000
th=2*math.pi*np.arange(N)/N
S=math.asinh(1/math.sqrt(2))
a0=math.sqrt(S/(4*math.pi*math.sqrt(3)))
checks=0
for a in [0.02,.07,.12,a0, .19,.3,.6,1]:
    xc=S/(4*math.pi*a)
    xd=brentq(lambda x:x*math.tanh(4*math.pi*a*x)-a,1e-12,10)
    xo=min(xc,xd)
    u=math.exp(-math.pi*(xo+a)**2); v=math.exp(-math.pi*(xo-a)**2)
    sig=np.array([u*u+v*v,v*v-u*u,math.sqrt(2)*u*v,math.sqrt(2)*u*v]);
    assert abs(min(sig) - min(v*v-u*u, math.sqrt(2)*u*v))<1e-13;checks+=1
    # exact numerical lifted measurement matrix on basis E00 E11 (E01+E10)/sqrt2 i(E01-E10)/sqrt2
    A=[]
    for U,V in [(u,v),(v,u)]:
        A.append(np.array([np.ones(N)*U*U,np.ones(N)*V*V,math.sqrt(2)*U*V*np.cos(th),math.sqrt(2)*U*V*np.sin(th)]))
    AA=np.concatenate([b.T for b in A],axis=0)/math.sqrt(N)
    ss=svd(AA,compute_uv=False)
    # NOTE offdiag coefficient should 2UV ReZ for normalized coordinate sqrt2 ReZ, so sqrt2 UV correct.  L2 norms yields sqrt2UV
    assert np.allclose(sorted(ss),sorted(sig),atol=1e-12,rtol=1e-12), (a,ss,sig);checks+=1
    num=min(sig)
    for k in np.linspace(0, max(1,xo*2),181):
      uu=math.exp(-math.pi*(k+a)**2); vv=math.exp(-math.pi*(k-a)**2)
      sm=min(vv*vv-uu*uu,math.sqrt(2)*uu*vv)
      assert sm<=num+1e-10,(a,xo,k,sm,num)
      checks+=1
    print('a',a,'cross',xc,'DCpeak',xd,'opt',xo,'minsv',num)
assert a0>0
print('CHECKS_PASS',checks,'critical',a0)
