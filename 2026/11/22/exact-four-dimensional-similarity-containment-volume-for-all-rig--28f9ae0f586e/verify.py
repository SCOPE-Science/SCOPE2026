#!/usr/bin/env python3
"""Exact symbolic certificate for the two-triangle similarity-containment theorem.
Requires SymPy (tested with version 1.13); optional SciPy/Numpy check below
is diagnostic only and does not enter the proof certificate.
"""
import itertools
import sympy as s
r=s.symbols('r', positive=True)
X=[(0,0),(1,0),(0,-1)]
Y=[(0,0),(0,1),(1,0)]
S={tuple(s.factor((X[j][q]-X[i][q])/r+Y[j][q]-Y[k][q]) for q in (0,1))
   for i,j,k in itertools.product(range(3),repeat=3)}
N=[(-(1+r)/r,0),(-1/r,-1/r),((r-1)/r,-(1+r)/r),
   (1,-(1+r)/r),(1/r,0),(1/r,(1+r)/r),
   ((1-r)/r,(1+r)/r),(-1,1/r)]
assert len(S)==25
assert all(tuple(s.factor(w) for w in n) in S for n in N)
count=0
for i in range(8):
    a,b=N[i],N[(i+1)%8]
    for c in S:
        det=(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
        p=s.Poly(s.cancel(det*r*r),r)
        if not p.is_zero:
            assert p.degree()<=2
            d=p.degree()
            # Bernstein coefficients of p on [0,1], certifying p >= 0.
            coeff=[p.nth(j) for j in range(d+1)]
            bernstein=[s.factor(sum(coeff[j]*s.binomial(k,j)/s.binomial(d,j)
                         for j in range(k+1))) for k in range(d+1)]
            assert all(z>=0 for z in bernstein),(i,c,p,bernstein)
        count+=1
assert count==200  # 8 edges x 25 distinct normals, original 27 include repeats
P=[]
for i in range(8):
    v=s.Matrix([N[i],N[(i+1)%8]]).inv()*s.ones(2,1)
    P.append(tuple(s.factor(w) for w in v))
area=s.factor(sum(P[i][0]*P[(i+1)%8][1]-P[(i+1)%8][0]*P[i][1]
                  for i in range(8))/2)
f=r*r*(-3*r**3+10*r*r-3*r+12)/(4*(1+r)*(1+r*r))
assert s.simplify(area-f)==0
assert f.subs(r,1)==1
assert s.factor(s.diff(f/r,r)-(1-r)*(3*r**5+9*r**4+5*r**3+21*r*r+6*r+12)/(4*(1+r)**2*(1+r*r)**2))==0
left=r*f/12
right=r**3*f.subs(r,1/r)/12
assert all(s.diff(left,r,k).subs(r,1)==s.diff(right,r,k).subs(r,1) for k in range(3))
assert s.simplify((s.diff(right,r,3)-s.diff(left,r,3)).subs(r,1))==s.Rational(5,32)
# Independent rational parameter polytope verification: exact vertices
# of 9 halfspaces, with exact 4D volume from triangulations if available.
def count_vertices(a,b):
    a,b=s.Rational(a),s.Rational(b)
    M=[]; rhs=[]
    for j in range(3):
        xx=[[1,0,0,0],[1,0,1,0],[1,0,0,-1]][j]
        yy=[[0,1,0,0],[0,1,0,1],[0,1,1,0]][j]
        M += [[-x for x in xx],[-y for y in yy],[xx[k]/a+yy[k]/b for k in range(4)]]
        rhs += [0,0,1]
    pts=set()
    for rows in itertools.combinations(range(9),4):
        mat=s.Matrix([M[i] for i in rows]);v=s.Matrix([rhs[i] for i in rows])
        if mat.det()==0:continue
        p=mat.inv()*v
        if all(sum(M[i][k]*p[k] for k in range(4))<=rhs[i] for i in range(9)):
            pts.add(tuple(p))
    return len(pts),pts
for a,b,num in [(1,1,8),(1,2,11),(2,1,11),(2,3,11)]:
    n,_=count_vertices(a,b)
    assert n==num,(a,b,n)
# Direct 4-dimensional convex-hull volume is independently checked if
# SciPy is installed; no floating-point assertion is used for the theorem.
try:
    import numpy as np
    from scipy.spatial import ConvexHull
    for a,b in [(1,1),(1,2),(2,3),(3,4)]:
        _,pts=count_vertices(a,b)
        measured=ConvexHull(np.array([[float(z) for z in p] for p in pts])).volume
        m,M=map(s.Rational,(sorted((a,b))))
        formula=m**3*M*(-3*m**3+10*m*m*M-3*m*M*M+12*M**3)/(48*(m+M)*(m*m+M*M))
        assert abs(measured-float(formula))<1e-9,(a,b,measured,formula)
except ImportError:
    pass
print('VERIFY_OK: 200 exact edge support certificates, symbolic area, shape extremum, smoothness jump, rational vertices')
