"""Independent small-dimensional convex-hull checks for a signed-order polytope's Euclidean boundary."""
import numpy as np
from scipy.spatial import HalfspaceIntersection, ConvexHull
from math import sqrt, comb

def points_and_hull(a):
    n=len(a); hs=[]
    for i in range(n):
        h=np.zeros(n+1);h[i]=1;h[-1]=-1;hs.append(h)
    for i in range(n):
        for j in range(i+1,n):
            h=np.zeros(n+1);h[i]=h[j]=-1;hs.append(h)
    hs=np.array(hs)
    v=HalfspaceIntersection(hs,np.full(n,.5)).intersections
    v=np.unique(np.round(v,10),axis=0)
    hull=ConvexHull(v*np.array(a),qhull_options='Qx')
    return hull.volume,hull.area,len(v)

for n in range(2,6):
    for a in ([1.]*n, [1.3]+[1.0+0.2*j for j in range(1,n)]):
        vol,area,verts=points_and_hull(a)
        prod=np.prod(a)
        predicted_volume=2*prod
        inv=np.reciprocal(a)
        predicted_area=prod*(2*sum(inv)+2/(n-1)*sum(np.hypot(inv[i],inv[j]) for i in range(n) for j in range(i+1,n)))
        assert np.isclose(vol,predicted_volume,rtol=1e-8,atol=1e-8),(n,a,vol,predicted_volume)
        assert np.isclose(area,predicted_area,rtol=1e-8,atol=1e-8),(n,a,area,predicted_area)
        print(f'n={n} shape={"uniform" if max(a)==min(a) else "anisotropic"} vertices={verts} vol={vol:.12g} surface={area:.12g}')
print('SIGNED_PAIR_FACET_PASS n=2..5 scales=2')
