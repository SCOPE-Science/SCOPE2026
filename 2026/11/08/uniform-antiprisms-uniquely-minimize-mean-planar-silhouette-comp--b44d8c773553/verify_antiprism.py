"""Reproduce regular-antiprism silhouette minimizer (science-only geometric checks)."""
import math
import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull


def expect(n,h):
    c=math.cos(math.pi/n); d=1-c; M=4*h*h+d*d
    al=math.acos(d/math.sqrt(M))
    be=math.acos((4*h*h*c-d*d)/M)
    return 2*n*(al+be)/math.pi

def optimal(n):
    c=math.cos(math.pi/n)
    return math.sqrt((1-c)*(1+2*c)/2)

def vertices(n,h):
    phi=math.pi/n
    return np.array([(math.cos(2*j*phi),math.sin(2*j*phi),h) for j in range(n)] + [(math.cos((2*j+1)*phi),math.sin((2*j+1)*phi),-h) for j in range(n)])

def silhouette_count(n,h,normals):
    phi=math.pi/n; d=1-math.cos(phi); Z=np.asarray(normals).reshape(-1,3)
    top=np.array([[2*h*math.cos((2*j+1)*phi),2*h*math.sin((2*j+1)*phi),d] for j in range(n)])
    bottom=np.array([[2*h*math.cos(2*j*phi),2*h*math.sin(2*j*phi),-d] for j in range(n)])
    T=Z@top.T;B=Z@bottom.T
    cap=((Z[:,2,None]*T<0).sum(axis=1)+(-Z[:,2,None]*B<0).sum(axis=1))
    belt=((T*B<0).sum(axis=1)+(T*np.roll(B,-1,axis=1)<0).sum(axis=1))
    return cap+belt

def direct_hull(V,vector):
    u=np.cross(vector,np.array([1.,0.,0.]))
    if np.linalg.norm(u)<1e-5:u=np.cross(vector,np.array([0.,1.,0.]))
    u=u/np.linalg.norm(u);v=np.cross(vector,u)
    return len(ConvexHull(np.c_[V@u,V@v]).vertices)

c=sp.symbols('c',real=True); q=(1-c)*(1+2*c)/2; k=1+c
ss=sp.factor((4*q)/(4*q+(1-c)**2))
assert sp.simplify(ss-(4*k-2)/(3*k))==0
assert sp.factor((4*q+2*(1-c))-4*(1-c*c))==0
assert sp.factor((4*q*c-(1-c)**2)/(4*q+(1-c)**2)-(4*c-1)/3)==0
for n in [3,4,5,6,9,16,40]:
    hs=optimal(n)
    vals=[expect(n,h) for h in [hs/8,hs/4,hs/2,hs,hs*2,hs*4,hs*8]]
    assert vals[3] < min(vals[:3]+vals[4:])
    c0=math.cos(math.pi/n)
    al=math.acos(math.sqrt((1-c0)/(3*(1+c0))))
    be=math.acos((4*c0-1)/3)
    assert abs(expect(n,hs)-2*n*(al+be)/math.pi)<1e-11
    if n<=9:
        rng=np.random.default_rng(818*n)
        for h in [hs/2,hs,2*hs]:
            z=rng.standard_normal((45000,3));z/=np.linalg.norm(z,axis=1)[:,None]
            counts=silhouette_count(n,h,z)
            assert counts.min()>=3 and counts.max()<=2*n
            est=np.mean(counts)
            assert abs(est-expect(n,h))<0.035,(n,h,est,expect(n,h))
            V=vertices(n,h)
            for ni,ct in zip(z[:180],counts[:180]):
                assert int(ct)==direct_hull(V,ni),(n,h,ct,direct_hull(V,ni))
    print(f'n={n:2d} hstar={hs:.12f} mean_min={vals[3]:.12f} lim_tall={n+2}')
print('ANTIPRISM_SILHOUETTE_OK symbolic=3 tested_n=7 sightline_samples=675000 hull_reconstructions=2700')
