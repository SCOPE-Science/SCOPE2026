"""Exact component certificate and independent plane-section check.

Dependencies: Python 3, SymPy, NumPy and SciPy. Run: python checker.py
"""
from itertools import product
from collections import Counter
import json
from pathlib import Path
import random
import math
import sympy as S
import numpy as np
from scipy.spatial import ConvexHull

x, y, z = S.symbols('x y z')
vertices = [(1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (0, 0, 4)]
heights = [a*x+b*y+c*z for a,b,c in vertices]
tetrahedra = ((0,1,2,4), (0,2,3,4))
edges = ((0,1),(1,2),(2,3),(3,0),(0,4),(1,4),(2,4),(3,4))

def signs_at(nx,ny,nz):
    return tuple(1 if (a*nx+b*ny+c*nz)>0 else -1 for a,b,c in vertices)

def density_rational(signs):
    q=S.Integer(0)
    for tet in tetrahedra:
        for i in tet:
            if signs[i]>0:
                q+=heights[i]**2/S.prod(heights[i]-heights[j] for j in tet if j!=i)
    return S.cancel(q)

def polynomial(signs):
    numer,denom = S.fraction(density_rational(signs))
    return S.Poly(S.expand(denom-10*numer),x,y,z)

classes = {}
for sz in (-1,1):
    for i,j in product((-3,0,3),repeat=2):
        # x+y = i*z, x-y = j*z
        xx, yy, zz = S.Rational(sz*(i+j),2), S.Rational(sz*(i-j),2), S.Integer(sz)
        s=signs_at(xx,yy,zz)
        assert s not in classes
        classes[s]=(xx,yy,zz)
assert len(classes)==18
assert Counter(S.total_degree(polynomial(s).as_expr()) for s in classes)==Counter({3:8,4:2,5:8})

surfaces=[]
for signs in classes:
    R=density_rational(signs)
    N,D=S.fraction(R)
    assert S.gcd(N,D)==1
    assert S.total_degree(D)==S.total_degree(N)+1
    f=polynomial(signs)
    # Rational factorization is an additional check; absolute irreducibility
    # follows separately from the primitive linear homogenization below.
    assert len(S.factor_list(f.as_expr())[1]) == 1
    # degree-d part equals D; degree-(d-1) part equals -10N. Thus
    # the homogenization D-10wN is primitive and linear in w,
    # proving absolute irreducibility, not merely factorization over Q.
    surfaces.append((signs,N,D,f))
assert len(surfaces)==18
certificate=json.loads((Path(__file__).parent/'CERTIFICATE.json').read_text(encoding='utf-8'))
assert len(certificate['components'])==18
assert certificate['polytope_vertices']==[list(v) for v in vertices]
for (sg,N,D,F), entry in zip(surfaces,certificate['components']):
    assert entry['height_signs']==''.join('+' if t>0 else '-' for t in sg)
    assert S.expand(S.sympify(entry['numerator'])-N)==0
    assert S.expand(S.sympify(entry['denominator'])-D)==0
    assert entry['component_degree']==F.total_degree()
# Equality of defining hypersurfaces forces equality of their reduced
# homogeneous rational functions, by comparing degree-d and degree-(d-1)
# parts of their normalized irreducible equations.
for i in range(18):
    for j in range(i):
        assert S.cancel(surfaces[i][1]/surfaces[i][2] - surfaces[j][1]/surfaces[j][2])!=0

assert sum(f.total_degree() for *_,f in surfaces)==72
assert sum(1 for *_,f in surfaces if f.total_degree()==1)==0

# Independent Euclidean section-area construction: intersect eight ORIGINAL
# pyramid edges with the exact plane; compute a planar convex hull. This
# does not use the tetrahedra or any B-spline formula.
V=np.asarray(vertices,dtype=float)
def direct_area(u):
    u=np.asarray(u,dtype=float)
    t=V@u
    pts=[]
    for a,b in edges:
        if t[a]*t[b]<0:
            r=t[a]/(t[a]-t[b]); pts.append(V[a]+r*(V[b]-V[a]))
    if len(pts)<3:return 0.
    unit=u/np.linalg.norm(u)
    tmp=np.array([1.,0.,0.]) if abs(unit[0])<.9 else np.array([0.,1.,0.])
    e=tmp - np.dot(tmp,unit)*unit; e/=np.linalg.norm(e)
    f=np.cross(unit,e)
    P=np.array([[p@e,p@f] for p in pts]);return float(ConvexHull(P).volume)

def predicted_area(u,signs):
    R=density_rational(signs)
    fn=S.lambdify((x,y,z),R,'numpy')
    return float(10*fn(*u)*np.linalg.norm(u))

rng=random.Random(81235)
checked=0
for signs, center in classes.items():
    for k in range(10):
        # Perturb within chart by a small relative amount and avoid boundary.
        a=float(center[0])+rng.uniform(-.09,.09)
        b=float(center[1])+rng.uniform(-.09,.09)
        c=float(center[2])+rng.uniform(-.035,.035)
        u=np.array([a,b,c])
        assert signs_at(*u)==signs
        direct=direct_area(u)
        pred=predicted_area(u,signs)
        assert abs(direct-pred)<2e-8*max(1.,direct), (signs,u,direct,pred)
        checked+=1
# Direct exact vertical slice: height 0 is 1/5 above base of height 5,
# hence similar-square side length 2*(4/5).
assert abs(direct_area((0.,0.,1.))-64/25)<1e-10
assert abs(predicted_area((0.,0.,1.),signs_at(0,0,1))-64/25)<1e-10

print('PASS: 18 exhaustive nonempty chambers via 3x3 on each half-space')
print('PASS: irreducible component degree multiset',dict(sorted(Counter(f.total_degree() for *_,f in surfaces).items())))
print('PASS: 153 pairwise distinctions, reduced homogeneous numerator/denominator')
print('PASS: 180 independent Euclidean plane-section comparisons')
print('PASS: exact vertical section, 18 embedded polynomial certificates and total algebraic degree 72')
for signs,N,D,f in surfaces:
    print(''.join('+' if q>0 else '-' for q in signs),f.total_degree(),S.total_degree(N),S.total_degree(D))
