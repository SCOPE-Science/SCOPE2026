"""Exact parameter-chamber and volume checks for a two-apex cubical polytope.

Requires Python 3.10+, sympy, numpy, scipy. All supporting-plane and
volume identities are checked in integer/rational arithmetic; convex hull
triangulations serve only to propose boundary simplices.
"""
from fractions import Fraction
from collections import Counter
from itertools import combinations, product
from math import factorial
import numpy as np
import sympy as S
from scipy.spatial import ConvexHull

X=S.symbols('t',real=True)
BASE=[tuple(z) for z in product((-1,1),repeat=4)]
U=BASE+[(1,1,1,1),(1,1,1,1),(-1,-1,-1,-1),(-1,-1,-1,-1)]
D=[(0,0,0,0)]*16+[(0,0,1,0),(0,0,0,1),(0,0,-1,0),(0,0,0,-1)]
assert len(U)==20
Vand=S.Matrix([[q**j for j in range(5)] for q in range(5)]).inv()
Vinv=[[Fraction(Vand[i,j]) for j in range(5)] for i in range(5)]

def det(m):
    """Integer/rational fraction-free determinant via exact elimination."""
    a=[list(row) for row in m]
    n=len(a)
    if n==1:return a[0][0]
    sign=1; last=1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:
            a[k],a[pivot]=a[pivot],a[k]
            sign=-sign
        pk=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pk-a[i][k]*a[k][j]
                a[i][j]=num//last if isinstance(num,int) and isinstance(last,int) else num/last
        for i in range(k+1,n):a[i][k]=0
        last=pk
    return sign*a[-1][-1]

def at(t):
    return [tuple(Fraction(u[i])+t*d[i] for i in range(4)) for u,d in zip(U,D)]

def affine_det(points):
    return det([list(v)+[1] for v in points])

def coeffs_from_samples(vals):
    out=[]
    for row in Vinv:
        c=sum(y*x for x,y in zip(vals,row))
        assert c.denominator==1
        out.append(int(c))
    return tuple(out)

# All possible changes in the oriented matroid of the 20 vertices arise
# from a zero of a five-point affine determinant.
polys=Counter()
for ids in combinations(range(20),5):
    vals=[]
    for t in range(5):
        verts=at(t)
        vals.append(affine_det([verts[i] for i in ids]))
    cs=coeffs_from_samples(vals)
    if not any(cs):continue
    # Determinants have degree <= 4: at most four moving vertices.
    if next(x for x in reversed(cs) if x)<0:cs=tuple(-x for x in cs)
    polys[cs]+=1
assert len(polys)==30, len(polys)
critical=set()
for cs in polys:
    poly=S.Poly(sum(c*X**j for j,c in enumerate(cs)),X)
    for root in S.polys.polytools.intervals(poly,eps=S.Rational(1,10**9)):
        (l,r),mult=root
        if r>0 and l>=0 and not (l==r==0):
            if r==l: critical.add(S.sympify(l))
            else: critical.add(S.Rational(l+r,2))
# Exact known positive roots; factoring every polynomial checks this list.
rootfactors=[X-1,X-2,X-4,X**2+4*X-4,X**2+2*X-4]
for cs in polys:
    f=S.Poly(sum(c*X**j for j,c in enumerate(cs)),X)
    for (g,exponent) in S.factor_list(f.as_expr())[1]:
        gg=S.Poly(g,X).monic().as_expr()
        if not any(S.Poly(gg-h,X).is_zero for h in [S.Poly(z,X).monic().as_expr() for z in rootfactors]):
            roots=S.polys.polytools.intervals(S.Poly(g,X),eps=S.Rational(1,10**9))
            assert all(rr[0][1]<=0 for rr in roots), (g,roots)
assert len(critical)==5,critical

# Each sample sits in one interval between consecutive positive roots.
reps=[Fraction(1,2),Fraction(9,10),Fraction(11,10),Fraction(3,2),Fraction(3),Fraction(5)]
volume_formulas=[16+8*X+S.Rational(2,3)*X**2]*4 + [S.Rational(4,3)*X**2+8*X+S.Rational(40,3)]*2
summaries=[]
for rep,formula in zip(reps,volume_formulas):
    vr=at(rep)
    vh=np.array([[float(v) for v in row] for row in vr])
    hull=ConvexHull(vh)
    # Every proposed boundary tetrahedron is a supporting simplex.
    facets=[tuple(map(int,f)) for f in hull.simplices]
    ridge=Counter()
    accum=S.Poly(0,X)
    for face in facets:
        for tri in combinations(face,3):ridge[tuple(sorted(tri))]+=1
        support=[affine_det([vr[i] for i in face]+[vr[j]]) for j in range(20) if j not in face]
        assert all(x>=0 for x in support) or all(x<=0 for x in support)
        vs=[[S.Integer(U[i][k])+X*D[i][k] for k in range(4)] for i in face]
        de=S.expand(S.det(S.Matrix(vs)))
        sign=1 if de.subs(X,S.Rational(rep))>0 else -1 if de.subs(X,S.Rational(rep))<0 else 0
        accum+=S.Poly(sign*de/24,X)
    assert set(ridge.values())=={2}, Counter(ridge.values())
    # Exact-supported simplices cover every extreme point, and their
    # connected closed pseudomanifold is the full polytope boundary.
    used={i for face in facets for i in face}
    adjacency={i:set() for i in used}
    for face in facets:
        for i,j in combinations(face,2):
            adjacency[i].add(j)
            adjacency[j].add(i)
    start=next(iter(used))
    seen={start}; stack=[start]
    while stack:
        for j in adjacency[stack.pop()]:
            if j not in seen: seen.add(j); stack.append(j)
    assert seen==used
    assert S.simplify(accum.as_expr()-formula)==0,(rep,accum.as_expr(),formula)
    summaries.append((str(rep),len(facets),len(ridge)))

print('PASS: 5,000+-subset exact orientation chamber enumeration (',sum(polys.values()),'nonzero determinants), 30 polynomial classes, 5 positive critical parameters')
print('PASS: six exact supporting-facet triangulations; (sample, facets, ridges):',summaries)
print('PASS: primal volume polynomials on every parameter chamber')

F=lambda k:S.Rational(4,3)*(S.sympify(k)+1)/(S.sympify(k)+2)**3
G=lambda k:S.Rational(4,3)*(-1/(S.sympify(k)+2)+S.Rational(1,2)/(S.sympify(k)+2)**2)
common=4/X*(G(X)-G(X/2))
polar_low=S.factor(common+4/(X+2)*(G(X)-G(0))+2*(2-X)/(X+2)*F(0))
polar_high=S.factor(common+4/(X+2)*(G(X)-G(X-2))+2*(X-2)/(X+2)*F(X-2))
vol_low=volume_formulas[0]; vol_high=volume_formulas[-1]
product_low=S.factor(vol_low*polar_low)
product_high=S.factor(vol_high*polar_high)
low_gap=S.factor(product_low-S.Rational(32,3))
high_gap=S.factor(product_high-S.Rational(32,3))
assert S.simplify(polar_low.subs(X,2)-polar_high.subs(X,2))==0
assert S.simplify(vol_low.subs(X,2)-vol_high.subs(X,2))==0
assert S.limit(X*high_gap,X,S.oo)==S.Rational(64,9)
# Nonnegative coefficient certificates on the two intervals.
Q=-(low_gap/S.factor(2*X/(9*(X+2)**3*(X+4)**2)))
assert S.Poly(Q,X).degree()==6
# For 0<t<=2, positive terms in -Q are bounded by 1792,
# and the constant negative part is at least 1920.
qpoly=S.expand(Q)
assert qpoly==X**6+16*X**5+76*X**4-32*X**3-1136*X**2-2752*X-1920
P=S.simplify(high_gap*9*X**3*(X+2)**3*(X+4)**2/64)
z=S.symbols('z',nonnegative=True)
assert all(c>0 for c in S.Poly(S.expand(P.subs(X,z+2)),z).all_coeffs())
print('PASS: polar integration primitives, closed rational volume products, and global strict Mahler inequality')
print('polar [0,2]:',polar_low)
print('polar [2,infinity):',polar_high)
print('Mahler gaps:',low_gap,high_gap)
print('asymptotic: 32/3 + 64/(9t) + O(t^-2)')

# The complete profile has a strict interior notch and two smooth peaks.
# All derivative claims are exact polynomial sign statements.
A=X**8+21*X**7+188*X**6+932*X**5+2528*X**4+2480*X**3-4288*X**2-12416*X-7680
B=X**9+30*X**8+248*X**7+720*X**6-456*X**5-6960*X**4-12048*X**3+2368*X**2+22784*X+15360
assert S.simplify(S.diff(product_low,X)+4*A/(9*(X+2)**4*(X+4)**3))==0
assert S.simplify(S.diff(product_high,X)+64*B/(9*X**4*(X+2)**4*(X+4)**3))==0
assert A.subs(X,0)<0<A.subs(X,2) and B.subs(X,0)>0>B.subs(X,2) and B.subs(X,3)>0
# Descartes' rule of signs: A has exactly one positive zero;
# B at most two, and opposite endpoint signs show exactly two.
assert S.Poly(A,X).all_coeffs() == [1,21,188,932,2528,2480,-4288,-12416,-7680]
assert S.Poly(B,X).all_coeffs() == [1,30,248,720,-456,-6960,-12048,2368,22784,15360]
assert A.subs(X,S.Rational(1577,1000))<0<A.subs(X,S.Rational(1578,1000))
assert B.subs(X,S.Rational(2607,1000))<0<B.subs(X,S.Rational(2609,1000))
# A rational global comparison: the first peak is <64/5 while
# the second branch already exceeds 64/5 at parameter 13/5.
poly=5*X**7+80*X**6+428*X**5+512*X**4-2032*X**3-4160*X**2+2688*X+6144
assert S.simplify(S.Rational(64,5)-product_low-2*poly/(45*(X+2)**3*(X+4)**2))==0
u=S.symbols('u',nonnegative=True)
for left,right in [(0,1),(1,S.Rational(3,2)),(S.Rational(3,2),2)]:
    transformed=S.Poly(S.cancel((1+u)**7*poly.subs(X,(left+right*u)/(1+u))),u)
    assert all(c>0 for c in transformed.all_coeffs())
assert (product_high-S.Rational(64,5)).subs(X,S.Rational(13,5))>0
print('PASS: exact two-peak/one-notch phase diagram, unique global peak, rational global comparison')
