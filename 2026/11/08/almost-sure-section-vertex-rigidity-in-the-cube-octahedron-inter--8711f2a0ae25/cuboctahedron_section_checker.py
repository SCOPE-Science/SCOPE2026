"""Exact rational cross-section checker for cube–octahedron intersections.

All arithmetic is rational. Section polygons are formed directly from pairs of
supporting planes, without consulting the 3D polyhedron edge graph.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import gcd
import random

FACETS = ([(tuple(s if j == i else 0 for j in range(3)), F(1))
           for i in range(3) for s in (-1, 1)] +
          [(s, None) for s in product((-1, 1), repeat=3)])

def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]

def section_vertices(t, n):
    t=F(t)
    a,b,c = map(F, n)
    assert a != 0 and F(1) <= t <= F(3)
    lines=[]
    for normal, rhs in FACETS:
        p,q,r=normal
        A=F(q)-F(p)*b/a
        B=F(r)-F(p)*c/a
        D=t if rhs is None else rhs
        lines.append((A,B,D))
    pts=set()
    for (A,B,D),(E,G,H) in combinations(lines,2):
        det=A*G-B*E
        if not det: continue
        y=(D*G-B*H)/det
        z=(A*H-D*E)/det
        if all(A0*y+B0*z<=D0 for A0,B0,D0 in lines):
            pts.add((y,z))
    P=sorted(pts)
    if len(P)<=2:return P
    lower=[]
    for p in P:
        while len(lower)>=2 and cross((lower[-1][0]-lower[-2][0], lower[-1][1]-lower[-2][1]),(p[0]-lower[-1][0],p[1]-lower[-1][1]))<=0:
            lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(P):
        while len(upper)>=2 and cross((upper[-1][0]-upper[-2][0], upper[-1][1]-upper[-2][1]),(p[0]-upper[-1][0],p[1]-upper[-1][1]))<=0:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

def main():
    for t in (F(1), F(11,10), F(3,2), F(19,10), F(2), F(21,10), F(5,2), F(29,10), F(3)):
        directions=((1,1,1),(10000,3,2),(173,53,11),(173,151,139))
        sizes=[len(section_vertices(t,n)) for n in directions]
        print('parameter',t,'counts',sizes)
        assert sizes[0]==6 if t!=2 else sizes[0] in (4,6,8)
        if t==1: assert sizes[1]==6
        elif t<2: assert sizes[1]>=8
        elif t>2: assert sizes[1]==4
        else:assert sizes[1:]==[8,8,8]
    r=random.Random(1062026)
    checked=0
    for _ in range(2000):
        n=[r.randint(-97,97) for j in range(3)]
        if n[0]==0 or len({abs(j) for j in n})!=3: continue
        assert len(section_vertices(F(2),n))==8,(n,len(section_vertices(F(2),n)))
        checked+=1
    assert checked>1500
    for _ in range(500):
        n=[r.randint(-43,43) for j in range(3)]
        if n[0]==0 or 0 in n: continue
        assert len(section_vertices(F(1),n))==6
    assert len(section_vertices(F(3),(100,3,2)))==4
    assert len(section_vertices(F(3),(1,1,1)))==6
    print('OCTAGONAL_RIGIDITY_EXACT_RATIONAL_CHECK_OK',checked)
if __name__=='__main__': main()
