"""Reproduce finite spectral and sign comparisons for fractional graph heat on the four-vertex path.
Only numeric diagnostics; the all-parameter conclusions use the analytic proof in RESULT.md.
Run: python checker.py (requires NumPy/SciPy)."""
import math
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq

root2=math.sqrt(2.)
small=2.-root2; middle=2.; large=2.+root2
r=small/middle; q=large/middle
A=(2+root2)/8; C=(2-root2)/8
L=np.diag([1.,2.,2.,1.])
for i in range(3):
    L[i,i+1]=L[i+1,i]=-1.
eig,U=eigh(L)
assert np.max(np.abs(eig-np.array([0.,small,middle,large])))<1e-12

def formula(alpha,tau):
    p=math.exp(-(r**alpha)*tau)
    m=math.exp(-tau)
    h=math.exp(-(q**alpha)*tau)
    # normalized time tau = 2**alpha * physical time
    return dict(k13=.25-root2/8*p-.25*m+root2/8*h,
                k14=.25-A*p+.25*m-C*h,
                k12=.25*(1-m)+root2/8*(p-h),
                k23=.25*(1-p)+.25*(m-h)+root2/8*(p-h))

def numeric(alpha,tau):
    return (U*np.exp(-np.maximum(eig,0)**alpha*(tau/(2**alpha))))@U.T

checks=0
for alpha in [0.1,0.3,0.9,1.,1.001,1.05,1.2,1.5,1.99,2.,2.001,2.2,2.7,3.,4.,6.,10.,16.]:
    for tau in [0.001,0.03,0.1,0.3,0.5,math.log(2.),1.,2.,4.,10.,30.,100.]:
        f=formula(alpha,tau); X=numeric(alpha,tau)
        for (key,i,j) in [('k13',0,2),('k14',0,3),('k12',0,1),('k23',1,2)]:
            assert abs(f[key]-X[i,j])<3e-13,(alpha,tau,key,f[key],X[i,j]);checks+=1
        assert abs(np.sum(X[0])-1)<3e-13;checks+=1
        assert min(X[i,i] for i in range(4))>0;checks+=1
        assert f['k12']>0 and f['k23']>0;checks+=1

# Root count via log grid with careful treatment of tiny roots and far endpoints.
for alpha in [1.01,1.1,1.5,1.9,2.,2.05,2.5,3.,5.,10.,15.]:
    ff=lambda key,tau:formula(alpha,tau)[key]
    lo=1e-7
    hi=max(50.,80./r**alpha)
    grid=np.geomspace(lo,hi,4000)
    for key,expected in [('k13',1),('k14',2 if alpha>2 else 1)]:
        # Ignore tiny numerical cancellation roots below 1e-5 (not used by selected alphas).
        zz=np.array([ff(key,float(x)) for x in grid])
        roots=[]
        for k in range(len(grid)-1):
            if zz[k]*zz[k+1]<0 and grid[k]>1e-5:
                roots.append(brentq(lambda x:ff(key,x),grid[k],grid[k+1]))
        assert len(roots)==expected,(alpha,key,len(roots),roots)
        if key=='k13':
            assert 0<roots[0]<2.,(alpha,key,roots)
        if key=='k14' and alpha>=2:
            assert roots[-1]>2.,(alpha,key,roots)
        if key=='k14' and alpha>2:
            assert roots[0]<math.log(2.),(alpha,key,roots)
        checks+=len(roots)+1

# Check the two predicted separated scales for large exponents.
for alpha in [5.,8.,12.,15.]:
    t0=math.log(2.)/2
    s0=math.log(1+1/root2)
    h0=-math.log(1-1/root2)
    f14=lambda z:formula(alpha,z)['k14']
    f13=lambda z:formula(alpha,z)['k13']
    first=brentq(f14,0.1,0.5)
    k13=brentq(f13,0.7,2.)
    last=brentq(f14,2.,100./r**alpha)
    assert abs(first-t0)<.06
    assert abs(k13-h0)<.1
    assert abs((r**alpha)*last-s0)<.1
    checks+=3
print('PASS: %d direct spectral, sign, root, and scale comparisons' % checks)
