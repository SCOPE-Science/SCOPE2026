#!/usr/bin/env python3
"""Exact polynomial checks for the indicated invariant polygon.
All coordinates are finite rational/symbolic expressions; no numerical convergence proof.
"""
import sympy as s
from fractions import Fraction as F
p,q=s.symbols('p q',real=True)
def poly_vertices(P,Q):
    X=s.Matrix([P-1,Q]); Y=s.Matrix([P,Q-1]); Z=s.Matrix([P,Q])
    A=s.Matrix([(P+2*Q)/3,(P+2*Q)/3])
    B=s.Matrix([2*(P-Q-1)/3,-(P-Q-1)/3])
    C=s.Matrix([(P-Q+1)/3,-2*(P-Q+1)/3])
    return [C+X,X,A+X,X+Z,B+Z,Z,C+Z,Y+Z,A+Y,Y,B+Y]
def moment(V,P,Q):
    # Signed polygon edge formula for the centered three-score quadratic.
    # Vertices are clockwise. Q2(z1,z2)=z1²+z2²+(z1+z2)².
    sh=s.Matrix([s.Rational(1,3)-P,s.Rational(1,3)-Q]); tot=0
    for i,a in enumerate(V):
        b=V[(i+1)%len(V)]
        det=s.det(s.Matrix.hstack(a,b))
        u=a+sh; v=b+sh
        # integral over triangular wedge (0,a,b) of squared affine scores,
        # with offset sh, using E[t]=1/3, E[t²]=1/6, E[tu]=1/12
        # Use direct triangle mean via vertices with original-score coordinates
        v0=sh;v1=u;v2=v
        def Q2(t):return 2*(t[0]**2+t[1]**2+t[0]*t[1])
        # E Q for uniform triangle = [sum_i Q(vi) + sum_{i<j} vi^T G vj]/6
        vv=[v0,v1,v2]
        cross=lambda a,b:2*(a[0]*b[0]+a[1]*b[1])+a[0]*b[1]+a[1]*b[0]
        ev=(sum(Q2(t) for t in vv)+sum(cross(vv[j],vv[k]) for j in range(3) for k in range(j+1,3)))/6
        tot+=-det/2*ev
    return s.factor(tot)
V=poly_vertices(p,q)
area=s.factor(-sum(s.det(s.Matrix.hstack(V[i],V[(i+1)%len(V)])) for i in range(len(V)))/2)
assert area==1,area
Fpoly=moment(V,p,q)
expected=s.Rational(5,18)+s.Rational(1,9)*(p-q)**2*(3-4*p-5*q)
assert s.simplify(Fpoly-expected)==0,(s.factor(Fpoly),expected)
for P,Q in [(F(7,24),F(1,4)),(F(8,25),F(13,50)),(F(1,3),F(1,3)),(F(1,2),F(0)),(F(1,6),F(1,6))]:
    assert s.simplify(moment(poly_vertices(s.Rational(P.numerator,P.denominator),s.Rational(Q.numerator,Q.denominator)),s.Rational(P.numerator,P.denominator),s.Rational(Q.numerator,Q.denominator))-expected.subs({p:s.Rational(P.numerator,P.denominator),q:s.Rational(Q.numerator,Q.denominator)}))==0
# Hexagonal Voronoi cell area and exact moment
Vh=poly_vertices(s.Rational(1,3),s.Rational(1,3))
assert s.simplify(moment(Vh,s.Rational(1,3),s.Rational(1,3))-s.Rational(5,18))==0
# Along p=q=t the polygon contains the same six extreme physical-score
# hexagon vertices; any additional listed points lie on its sides.
Vbase={tuple(z) for z in Vh}
for T in [s.Rational(1,6),s.Rational(1,4),s.Rational(1,3)]:
    vv=[z+s.Matrix([s.Rational(1,3)-T,s.Rational(1,3)-T]) for z in poly_vertices(T,T)]
    assert Vbase.issubset({tuple(z) for z in vv})
    assert all(max([z[0],z[1],-z[0]-z[1]])-min([z[0],z[1],-z[0]-z[1]])<=1 for z in vv)
print('PASS: symbolic area=1; exact centered second moment; rational substitution; Voronoi hexagon; three edge-plateau checks.')
print('integrated energy:',Fpoly)
