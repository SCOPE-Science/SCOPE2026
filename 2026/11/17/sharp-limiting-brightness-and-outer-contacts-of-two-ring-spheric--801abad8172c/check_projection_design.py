"""Independent finite tests for the latitude-design brightness theorem.
Requires Python 3, NumPy and SciPy. The infinite-dimensional conclusions
follow from the written analytic proof, not these numerical checks.
"""
import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar

def sites(n):
    theta=2*math.pi*np.arange(n)/n
    c=math.sqrt(2/3); h=1/math.sqrt(3)
    ring=np.column_stack((c*np.cos(theta), c*np.sin(theta)))
    return np.vstack((np.column_stack((ring,np.full(n,h))),
                      np.column_stack((ring,np.full(n,-h)))))

def brightness(X,v):
    return math.pi/(len(X)/2)*np.abs(X @ v).sum()

def facet_inradius(X):
    """Enumerate all facet normals as generator cross products."""
    best=float('inf')
    for i in range(len(X)):
        for j in range(i+1,len(X)):
            v=np.cross(X[i],X[j]); norm=np.linalg.norm(v)
            if norm<1e-10: continue
            best=min(best,brightness(X,v/norm))
    return best

u=brentq(lambda x:x-math.sin(2*x),0.1,1.5,xtol=1e-15)
t=math.sin(u); c=math.sqrt(2/3)
fstar=4*c/math.pi*(math.cos(u)+u*t)/math.sqrt(1+2*t*t)
rstar=math.pi*fstar
zstar=math.sqrt(2)*t/math.sqrt(1+2*t*t)
rmax=2*math.pi/math.sqrt(3)
rng=np.random.default_rng(271828)
tests=0
for n in range(4,31):
    X=sites(n)
    assert X.shape==(2*n,3)
    assert np.max(np.abs(X.mean(axis=0)))<1e-13
    assert np.max(np.abs(X.T@X/(2*n)-np.eye(3)/3))<2e-13
    # All third moments vanish: the double-ring set is a 3-design.
    T=np.einsum('ni,nj,nk->ijk',X,X,X)/(2*n)
    assert np.max(np.abs(T))<3e-13
    assert abs(np.mean(X[:,2]**4)-1/5)>0.08 # not a 4-design
    tests+=4
    assert abs(brightness(X,np.array([0.,0.,1.]))-rmax)<1e-12
    tests+=1
    for j in range(65):
        v=rng.normal(size=3);v/=np.linalg.norm(v)
        assert brightness(X,v)<rmax+5e-12
        tests+=1
    rin=facet_inradius(X)
    assert abs(rin-rstar) <= math.pi**2*c/n+1e-11
    assert rin>0
    tests+=2
    if n in (4,5,6,8,10,16,24,30):
        print(f'n={n:2d}, finite_inradius={rin:.12f}, finite/norm_pi={rin/math.pi:.12f}, limit={rstar:.12f}')
# Direct integration and minimization of the axisymmetric limit.
def norm_bright(z):
    a=math.sqrt(2/3)*math.sqrt(1-z*z)
    b=z/math.sqrt(3)
    if b>=a:return 2*b
    t=b/a
    return 4/math.pi*(a*math.sqrt(1-t*t)+b*math.asin(t))
res=minimize_scalar(norm_bright,bounds=(0,1),method='bounded',options={'xatol':1e-13})
assert abs(res.fun-fstar)<5e-11 and abs(res.x-zstar)<2e-6
tests+=2
# At n=4 the extra maximum-brightness axes are horizontal diagonals.
X=sites(4)
for v in ((1/math.sqrt(2),1/math.sqrt(2),0.),(1/math.sqrt(2),-1/math.sqrt(2),0.)):
    assert abs(brightness(X,np.array(v))-rmax)<1e-12
    tests+=1
print('LATITUDE_DESIGN_BRIGHTNESS_OK',tests,'u',u,'zstar',zstar,'limit_inradius',rstar,'outer',rmax)
