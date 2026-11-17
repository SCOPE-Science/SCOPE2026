"""Independent Euclidean facet/ridge checks for layered order polytopes.

Requires NumPy and SciPy. Run: python verify_layered_order.py
This finite test does not replace the analytic all-dimensional proof.
"""
from itertools import combinations, product
from math import acos, factorial, isclose, pi, sqrt
import numpy as np
from scipy.spatial import ConvexHull


def evaluate(sizes):
    n = sum(sizes)
    r = len(sizes)
    offsets = [0]
    for a in sizes:
        offsets.append(offsets[-1] + a)
    vertices = set()
    for j, a in enumerate(sizes):
        for bits in product((0., 1.), repeat=a):
            vertices.add((0.,) * offsets[j] + bits + (1.,) * (n - offsets[j+1]))
    vertices = np.array(sorted(vertices))
    faces = []
    for i in range(sizes[0]):
        v = np.zeros(n); v[i] = -1
        faces.append(('L',v,0.))
    for i in range(offsets[-2],n):
        v = np.zeros(n); v[i] = 1
        faces.append(('U',v,1.))
    for j in range(r-1):
        for i in range(offsets[j],offsets[j+1]):
            for h in range(offsets[j+1],offsets[j+2]):
                v = np.zeros(n); v[i] = 1; v[h] = -1
                faces.append(('E',v,0.))
    volume = np.prod([factorial(a) for a in sizes]) / factorial(n)
    # Direct facet measure from projected convex hulls.
    boundary = 0.
    for kind, a, b in faces:
        poly = vertices[abs(vertices@a-b)<1.e-9]
        u,s,vh=np.linalg.svd(poly-poly.mean(axis=0),full_matrices=False)
        assert sum(s>1.e-8)==n-1
        boundary+=ConvexHull((poly-poly.mean(axis=0))@vh[:n-1].T).volume
    expected_surface=n*(2+(r-1)*sqrt(2))
    assert isclose(boundary/volume,expected_surface,rel_tol=2.e-9,abs_tol=1.e-8), (sizes,boundary/volume,expected_surface)
    curvature=0.; ridges=0; group={}
    for (typea,a,ba),(typeb,b,bb) in combinations(faces,2):
        match=(abs(vertices@a-ba)<1.e-9)&(abs(vertices@b-bb)<1.e-9)
        poly=vertices[match]
        if len(poly)<n-1:
            continue
        u,s,vh=np.linalg.svd(poly-poly.mean(axis=0),full_matrices=False)
        if sum(s>1.e-8)!=n-2:
            continue
        area=ConvexHull((poly-poly.mean(axis=0))@vh[:n-2].T).volume
        angle=acos(np.clip((a@b)/(np.linalg.norm(a)*np.linalg.norm(b)),-1.,1.))
        curvature+=area*angle/(2*pi*volume)
        ridges+=1
        group.setdefault((typea,typeb),0)
        group[(typea,typeb)]+=1
    k=r-1
    expected=n*(n-1)*(0.5+k*sqrt(2)/2+k*sqrt(3)/6+k*(k-1)/4)
    assert isclose(curvature,expected,rel_tol=2.e-9,abs_tol=1.e-7), (sizes,curvature,expected)
    return ridges

if __name__=='__main__':
    profiles=[(2,2),(2,3),(3,2),(3,3),(2,4),(4,2),(4,4),
              (2,2,2),(2,3,2),(3,2,2),(2,2,3),(2,3,3),(3,2,3),(3,3,2),
              (2,2,2,2),(2,2,2,2,2)]
    total=sum(evaluate(s) for s in profiles)
    print('LAYERED_STEINER_PASS', 'profiles='+str(len(profiles)), 'ridges='+str(total),
          'max_layers='+str(max(map(len,profiles))))
