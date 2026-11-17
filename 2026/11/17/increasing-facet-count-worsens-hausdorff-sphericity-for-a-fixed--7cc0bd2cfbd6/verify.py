"""Reproduce geometric and cubature checks for latitude-ring Minkowski bipyramids.

Requires numpy and scipy. Executable: python verify.py
"""
import math
import numpy as np
from scipy.spatial import ConvexHull

SQRT3=math.sqrt(3.0)

def model(n):
    assert n>=4
    alpha=math.pi/n
    a=math.sqrt(4*math.pi/(n*SQRT3*math.sin(2*alpha)))
    b=math.sqrt(2)*a*math.cos(alpha)
    theta=2*math.pi*np.arange(n)/n
    X=np.array([[math.sqrt(2/3)*math.cos(t),math.sqrt(2/3)*math.sin(t),z/SQRT3]
      for z in (-1,1) for t in theta])
    angles=theta-alpha
    V=np.array([[a*math.cos(t),a*math.sin(t),0.0] for t in angles]+[[0,0,b],[0,0,-b]])
    return a,b,X,V

count=0
for n in range(4,41):
    a,b,X,V=model(n)
    # All polynomial moments of total degree <=3, from first principles.
    for i in range(4):
      for j in range(4-i):
       for k in range(4-i-j):
        degree=i+j+k
        # normalized sphere moments through degree 3
        target=1.0 if degree==0 else (1/3 if degree==2 and max(i,j,k)==2 else 0.0)
        value=np.mean(X[:,0]**i*X[:,1]**j*X[:,2]**k)
        assert abs(value-target)<4e-14, (n,i,j,k,value,target)
        count+=1
    assert abs(np.mean(X[:,2]**4)-1/9)<2e-14
    assert abs(np.mean(X[:,2]**4)-1/5)>0.08
    count+=2
    H=ConvexHull(V)
    # Each triangular facet; hull equations n.x + offset <=0, equidistant.
    assert len(H.simplices)==2*n, (n,len(H.simplices))
    count+=1
    surf=0.0
    for face,eq in zip(H.simplices,H.equations):
        p,q,r=V[face]
        area=np.linalg.norm(np.cross(q-p,r-p))/2
        surf+=area
        normal=eq[:3]; offset=eq[3]
        assert abs(-offset-b/SQRT3)<2e-12
        assert min(np.linalg.norm(normal-z) for z in X)<2e-12
        count+=2
    assert abs(surf-4*math.pi)<2e-11, (n,surf)
    vol=(4*math.pi/(3*SQRT3))*b
    assert abs(H.volume-vol)<1e-11, (n,H.volume,vol)
    assert abs(max(np.linalg.norm(v) for v in V)-b)<2e-12
    assert abs(b*b-(4*math.pi/(n*SQRT3))*1/math.tan(math.pi/n))<2e-12
    assert abs(b/SQRT3-min(-eq[3] for eq in H.equations))<2e-12
    assert b-1>1-b/SQRT3
    count+=6
    # Direct support function samples, independently from all vertices.
    rng=np.random.default_rng(n)
    dirs=rng.normal(size=(150,3));dirs/=np.linalg.norm(dirs,axis=1)[:,None]
    for u in dirs:
        support=max(V@u)
        assert b/SQRT3-1e-11<=support<=b+1e-11
        assert abs(support-1)<=b-1+1e-11
        count+=2

last=0.0
for n in range(4,301):
    _,b,_,_=model(n)
    assert b>last
    assert b<2/(3**0.25)+1e-12
    last=b
    count+=2
assert abs(np.mean(model(4)[2][:,2]**4)-1/9)<1e-14
print('PASS',count,'checks; n=4..40 hulls; n=4..300 monotonicity')
print('n=4:',model(4)[1]-1,'lim:',2/3**0.25-1)
