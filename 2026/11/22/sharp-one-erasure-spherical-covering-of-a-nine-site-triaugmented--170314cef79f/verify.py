"""Exact algebraic verification of supporting facets and one-erasure covering radii.

Requirements: Python 3 with SymPy. All sign tests concern the full open interval
1/2 < r < 1; numerical samples are not used to certify continuity.
"""
from itertools import combinations
import sympy as sp

r, h = sp.symbols('r h', positive=True, real=True)
q = sp.sqrt(3)
V = [sp.Matrix(t) for t in [
    (1,0,0),(-sp.Rational(1,2),q/2,0),(-sp.Rational(1,2),-q/2,0),
    (r/2,q*r/2,h),(-r,0,h),(r/2,-q*r/2,h),
    (r/2,q*r/2,-h),(-r,0,-h),(r/2,-q*r/2,-h)
]]
# A quadrilateral is written once with four vertex indices.
FACES = {
    0: {
        'F':[(3,5,6,8)],
        'E':[(3,4,5),(6,7,8)],
        'C':[(1,3,4),(1,6,7),(2,4,5),(2,7,8)],
        'D':[(1,3,6),(1,4,7),(2,4,7),(2,5,8)]},
    3: {
        'A':[(0,1,4,5)],
        'B':[(0,1,6)],
        'C':[(0,6,8),(1,6,7),(2,4,5),(2,7,8)],
        'D':[(0,5,8),(1,4,7),(2,4,7),(2,5,8)],
        'E':[(6,7,8)]}
}
A=(1-r)/(5-3*r)
B=(1-r*r)/(5-4*r)
C=4*(1-r*r)/(8-4*r-3*r*r)
D=3*r*r/(4*(r*r-r+1))
E=1-r*r
F=r*r/4
DIST={'A':A,'B':B,'C':C,'D':D,'E':E,'F':F}

def sign_on(p,left=sp.Rational(1,2),right=sp.S.One):
    p=sp.factor(p)
    if p==0: return 0
    poly=sp.Poly(p,r)
    while poly.eval(left)==0: poly=poly.quo(sp.Poly(r-left,r))
    while poly.eval(right)==0: poly=poly.quo(sp.Poly(r-right,r))
    assert poly.count_roots(left,right)==0, (p,left,right)
    test=(left+right)/2
    return int(sp.sign(p.subs(r,test)))

for deleted, classes in FACES.items():
    available=[i for i in range(9) if i!=deleted]
    assert sum(len(v) for v in classes.values()) == 11
    for label,faces in classes.items():
        for face in faces:
            a,b,c=(V[i] for i in face[:3]); n=(b-a).cross(c-a)
            assert n.dot(n)!=0
            # Each listed site is coplanar with its facet.
            assert all(sp.expand((V[i]-a).dot(n))==0 for i in face)
            signs=[]
            for j in available:
                if j in face:continue
                det=sp.factor(sp.expand((V[j]-a).dot(n)))
                assert det!=0, (deleted,label,face,j)
                # Positive factors sqrt(3) and h do not affect sign.
                p=sp.factor(det.subs(h,1)/q)
                signs.append(sign_on(p))
            assert len(set(signs))==1,(deleted,label,face,signs)
            # The origin is strictly on the interior side.
            inward=sp.factor(-a.dot(n))
            assert sign_on(sp.factor(inward.subs(h,1)/q))==signs[0]
            d2=sp.factor((a.dot(n))**2 / n.dot(n))
            d2=sp.factor(d2.subs(h**2,1-r*r))
            assert sp.simplify(d2-DIST[label])==0, (deleted,label,face,d2)
    # There are eight vertices and eleven distinct facets, one quadrilateral:
    # 2e>=3f+1 and Euler imply f<=2v-5=11. Thus these are exhaustive.

# Exact strict rational-function sign checks, including the singularity-free
# boundaries used by the piecewise minimum proof.
ineqs=[(B-A,sp.Rational(1,2),1), (C-A,sp.Rational(1,2),1),
       (D-A,sp.Rational(1,2),1), (E-A,sp.Rational(1,2),1),
       (D-F,sp.Rational(1,2),1),
       (C-F,sp.Rational(1,2),sp.Rational(2,3)),
       (C-E,sp.Rational(2,3),1),
       (A-E,sp.Rational(1,2),1)]
for expr,lo,hi in ineqs:
    num,den=map(sp.factor,sp.fraction(sp.factor(expr)))
    assert sign_on(num,lo,hi)*sign_on(den,lo,hi) !=0
    # Last one A-E is negative; all preceding differences are positive.
    expected = -1 if expr==A-E else 1
    assert sign_on(num,lo,hi)*sign_on(den,lo,hi)==expected,(expr,lo,hi)
assert sp.factor(A-F)==sp.factor(-(r-2)*(r+1)*(3*r-2)/(4*(3*r-5)))
assert sp.simplify(A.subs(r,sp.Rational(2,3))-sp.Rational(1,9))==0
assert sp.simplify(F.subs(r,sp.Rational(2,3))-sp.Rational(1,9))==0
assert sp.simplify(sp.diff(A,r)+2/(5-3*r)**2)==0
print('VERIFY_OK: all symbolic facet, distance, inequality and threshold checks passed')
