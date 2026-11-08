"""Numerical cross-check independent of the algebraic sign-cone certificate."""
import numpy as np
from scipy.spatial import ConvexHull
from collections import Counter
p=(1+5**.5)/2
v=[]
for a in (-1,1):
 for b in (-1,1):
  v.extend(((0.,a,b*p),(a,b*p,0.),(b*p,0.,a)))
v=np.asarray(v)
E=[(i,j) for i in range(12) for j in range(i+1,12) if abs(np.sum((v[i]-v[j])**2)-4)<1e-9]
w=np.array([(2*v[i]+v[j])/3 for i,j in E]+[(v[i]+2*v[j])/3 for i,j in E])
edges=[(i,j) for i in range(60) for j in range(i+1,60) if abs(np.sum((w[i]-w[j])**2)-4/9)<1e-9]
assert len(E)==30 and len(edges)==90
edges=np.array(edges)
rng=np.random.default_rng(72936)
N=250000
cnt=Counter()
for batch in range(0,N,5000):
 n=rng.normal(size=(min(5000,N-batch),3));n/=np.linalg.norm(n,axis=1)[:,None]
 s=n@w.T
 nside=np.count_nonzero((s[:,edges[:,0]]*s[:,edges[:,1]])<0,axis=1)
 cnt.update(nside.tolist())
ref={10:.4858721452639934,12:.2934108266237144,14:.1652249833720431,16:.0254674039434962,18:.0300246407967538}
assert set(cnt)==set(ref)
for k in sorted(cnt):
    obs=cnt[k]/N; err=abs(obs-ref[k]); bound=5*(ref[k]*(1-ref[k])/N)**.5
    assert err < bound,(k,obs,bound)
    print('MC',k,obs,ref[k],err)

for _ in range(100):
 n=rng.normal(size=3);n=n/np.linalg.norm(n)
 s=w@n
 cross=np.where(s[edges[:,0]]*s[edges[:,1]]<0)[0]
 I=[]
 for ix in cross:
  a,b=edges[ix]; t=-s[a]/(s[b]-s[a]);I.append(w[a]+t*(w[b]-w[a]))
 I=np.array(I)
 helper=np.eye(3)[np.argmin(abs(n))];u=helper-n*(n@helper);u/=np.linalg.norm(u); vv=np.cross(n,u)
 xy=np.column_stack((I@u,I@vv))
 h=ConvexHull(xy)
 assert len(h.vertices)==len(cross),(len(h.vertices),len(cross))
print('INDEPENDENT_CHECK_OK',N,'directions',100,'independent convex hulls')
