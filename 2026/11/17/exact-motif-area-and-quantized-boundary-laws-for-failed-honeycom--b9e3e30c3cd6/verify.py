"""Independent numerical checks for honeycomb unit-disk erasure formulas.

Run with Python 3, numpy and scipy. Only finite sampling is used;
this checker does not certify infinite-plane mathematical identities.
"""
import math
import numpy as np
from scipy.spatial import cKDTree
from scipy.stats import qmc

SQ3=math.sqrt(3.0)
A=np.array([1.5,SQ3/2])
B=np.array([1.5,-SQ3/2])
centers=np.array([i*A+j*B for i in range(-7,8) for j in range(-7,8)])
centers=np.vstack((centers, centers+[1.0,0.0]))
assert len(centers)==450

def find(p):
    inds=np.where(np.linalg.norm(centers-np.asarray(p),axis=1)<1e-8)[0]
    assert len(inds)==1, (p,inds)
    return int(inds[0])

origin=find((0,0)); east=find((1,0)); upper=find((-.5,SQ3/2))
lowereast=find((1.5,-SQ3/2)); far=find((3,0));
c2=1.5*SQ3-2*math.pi/3
c3=math.pi/3-SQ3/2
rho=4/(3*SQ3)

# In a period parallelogram, directly count disk multiplicity.
xy=qmc.Sobol(2,scramble=True,seed=403).random_base2(18)@np.vstack((A,B))
counts=np.zeros(len(xy), dtype=np.uint8)
for p in centers:
    counts+=np.sum((xy-p)**2,axis=1)<1-1e-10
assert set(counts).issubset({2,3}), np.unique(counts,return_counts=True)
p2=3-rho*math.pi
p3=rho*math.pi-2
assert abs(np.mean(counts==2)-p2)<.003
assert abs(np.mean(counts==3)-p3)<.003
for q in [0.12,0.31,0.68,0.9]:
    emp=np.mean(q**counts)
    exact=p2*q*q+p3*q*q*q
    assert abs(emp-exact)<.003

# Independent geometry quadrature: deleted-site configurations.
cases = [ [origin], [origin,east], [origin,east,upper],
          [origin,east,lowereast], [origin,east,upper,lowereast],
          [find((0,0)),find((1,0)),find((1.5,SQ3/2)),find((1,SQ3)),find((0,SQ3)),find((-.5,SQ3/2))] ]
for case in cases:
    S=set(case)
    V=centers[np.array([i not in S for i in range(len(centers))])]
    tree=cKDTree(V)
    ep=[]; deg={i:0 for i in S}
    for i in S:
        for j in S:
            if i<j and abs(np.linalg.norm(centers[i]-centers[j])-1)<1e-8:
                ep.append((i,j));deg[i]+=1;deg[j]+=1
    E=len(ep)
    P=sum(d*(d-1)//2 for d in deg.values())
    area_expected=c2*E+c3*P
    length_expected=(2*math.pi/3)*(2*E-P)
    assert abs((area_expected+(0.5-3*SQ3/(4*math.pi))*length_expected)-SQ3*E/2)<1e-10
    shape=np.array([centers[i] for i in S]);lo=shape.min(axis=0)-1.1;hi=shape.max(axis=0)+1.1
    pt=lo+(hi-lo)*qmc.Sobol(2,scramble=True,seed=923+len(case)).random_base2(19)
    dist=tree.query(pt, workers=1)[0]
    area_est=np.prod(hi-lo)*np.mean(dist>1+1e-10)
    assert abs(area_est-area_expected)<max(.018,0.018*area_expected),(area_est,area_expected)
    # Each boundary arc is sampled directly on surviving unit-circle boundaries.
    k=3600;theta=2*math.pi*(np.arange(k)+.5)/k
    dirs=np.stack((np.cos(theta),np.sin(theta)),axis=1)
    length_est=0
    for v in V:
        if np.linalg.norm(v-shape,axis=1).min()>2.05:continue
        positions=v+dirs
        # nearest other surviving disk, excluding the current center.
        others=V[np.linalg.norm(V-v,axis=1)>.1]
        unmasked=cKDTree(others).query(positions,workers=1)[0]>1+1e-10
        length_est+=2*math.pi*np.mean(unmasked)
    assert abs(length_est-length_expected)<.055,(length_est,length_expected)
    print(f'sites={len(S)} edges={E} paths={P} area={area_est:.6f}/{area_expected:.6f} perimeter={length_est:.6f}/{length_expected:.6f}')
print('HONEYCOMB_ERASURE_AREA_PERIMETER_CHECK_OK',len(cases),'finite deletion cases')
