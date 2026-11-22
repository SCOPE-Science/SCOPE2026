"""Exact-arithmetic checks for a three-season max-plus Lyness return map.

Requires Python 3 and SymPy for the independent polynomial identity.
The theorem and its all-level proof are given in RESULT.md; samples here do not
replace the all-level arguments.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import gcd
import sympy as sp

# The seven affine forms in the conserved maximum.
forms = [(1,0,1), (0,1,0), (1,-1,1), (-1,1,1),
         (0,-1,2), (-1,0,1), (-1,-1,1)]


def H(p):
    x,y=p
    return max(a*x+b*y+c for a,b,c in forms)


def T(a,p):
    x,y=p
    return y,max(a,y)-x


def F(p):
    for a in (0,1,1):
        p=T(a,p)
    return p


def polygon(h):
    vertices=set()
    for (a,b,c),(d,e,f) in combinations(forms,2):
        det=a*e-b*d
        if not det: continue
        p=(Q((h-c)*e-b*(h-f),det),
           Q(a*(h-f)-(h-c)*d,det))
        if H(p)==h: vertices.add(p)
    if len(vertices)<=1: return sorted(vertices)
    # Ordering without floating point: all these polygons are x/y monotone
    # and have a unique leftmost non-upper vertex for the CCW order.
    # For checks we explicitly use the two symbolic vertex families below.
    return list(vertices)


def expected_vertices(h):
    if h<Q(4,3):return []
    if h==Q(4,3):return [(Q(1,3),Q(2,3))]
    if h<=2:
        return [(3-2*h,2-h),(h-1,2-h),(h-1,2*h-2)]
    return [(1-h,0),(-1,2-h),(1,2-h),(h-1,0),(h-1,h),(1,h)]


def primitive_length(a,b):
    dx,dy=b[0]-a[0],b[1]-a[1]
    den=dx.denominator*dy.denominator//gcd(dx.denominator,dy.denominator)
    return Q(gcd(abs(int(dx*den)),abs(int(dy*den))),den)


def perimeter(vs):
    return sum((primitive_length(a,b) for a,b in zip(vs,vs[1:]+vs[:1])),Q(0))


def arc_coordinate(vs,p):
    ans=Q(0)
    for a,b in zip(vs,vs[1:]+vs[:1]):
        dx,dy=b[0]-a[0],b[1]-a[1]
        if ((p[0]-a[0])*dy==(p[1]-a[1])*dx
            and min(a[0],b[0])<=p[0]<=max(a[0],b[0])
            and min(a[1],b[1])<=p[1]<=max(a[1],b[1])):
            return ans+primitive_length(a,p)
        ans+=primitive_length(a,b)
    raise AssertionError(('off boundary',vs,p))


def integer_shell(m):
    vs=expected_vertices(Q(m))
    points=[]
    for a,b in zip(vs,vs[1:]+vs[:1]):
        dx,dy=b[0]-a[0],b[1]-a[1]
        assert dx.denominator==1 and dy.denominator==1
        k=gcd(abs(int(dx)),abs(int(dy)))
        assert k>0 and int(k)==k
        points.extend([(int(a[0]+dx*j/k),int(a[1]+dy*j/k)) for j in range(k)])
    assert len(points)==len(set(points))
    return points


def check_symbolic_integral():
    u,v,q=sp.symbols('u v q',positive=True)
    def R(a,p):
        x,y=p
        return y,(a+y)/x
    def V(p):
        x,y=p
        return (q*x*x*y+x*y*y+q*x*x+q*y*y+(1+q*q)*x+2*q*y+q)/(x*y)
    p=(u,v)
    for a in (1,q,q):p=R(a,p)
    assert sp.factor(V(p)-V((u,v)))==0
    assert sp.factor(p[0]-(1+q*u+v)/(u*v))==0
    assert sp.factor(p[1]-(1+q*u+v+q*u*v)/(v*(1+v)))==0
    print('Symbolic positive-rational first integral: exact identity verified')


def main():
    check_symbolic_integral()
    levels=[Q(a,b) for b in range(1,14) for a in range(1,10*b) if Q(a,b)>Q(4,3)]
    levels=sorted(set(levels))
    # Exact half-plane intersection and affine-perimeter/rotation checks.
    for h in levels:
        vs=expected_vertices(h)
        assert set(polygon(h))==set(vs),h
        assert all(H(v)==h for v in vs),h
        L=perimeter(vs)
        expectedL=9*h-12 if h<=2 else 5*h-4
        expectedDelta=3*h-4 if h<=2 else 2*h-2
        assert L==expectedL,(h,L,expectedL)
        anchor=vs[0]
        assert (arc_coordinate(vs,F(anchor))-arc_coordinate(vs,anchor))%L==expectedDelta
        for a,b in zip(vs,vs[1:]+vs[:1]):
            for k in (0,1,2,3,4,5,6,7):
                p=(a[0]+(b[0]-a[0])*Q(k,8),a[1]+(b[1]-a[1])*Q(k,8))
                assert H(F(p))==h,(h,p)
                d=(arc_coordinate(vs,F(p))-arc_coordinate(vs,p))%L
                assert d==expectedDelta,(h,p,d)
    print('Exact rational polygon and rotation checks:',len(levels),'energy levels')
    # Independently examine a grid of off-shell points.
    count=0
    for d in (1,2,3,7):
        for i in range(-50,51,3):
            for j in range(-50,51,4):
                p=(Q(i,d),Q(j,d))
                assert H(F(p))==H(p)
                count+=1
    print('Exact off-shell conservation checks:',count)
    for m in range(2,51):
        pts=integer_shell(m)
        L=5*m-4
        step=2*m-2
        assert len(pts)==L
        seen=set()
        lengths=[]
        for p in pts:
            assert H(p)==m
            assert F(p) in pts
            if p in seen:continue
            cyc=[]; z=p
            while z not in seen:
                seen.add(z);cyc.append(z)
                z=F(z)
            assert z==p
            lengths.append(len(cyc))
        g=gcd(L,step)
        assert len(lengths)==g and set(lengths)=={L//g},(m,lengths)
        assert g==gcd(m,2)
    print('Complete integer-shell orbit checks: energies 2..50')
    print('Total integer states examined:',sum(5*m-4 for m in range(2,51)))
    print('All checks passed')

if __name__=='__main__':main()
