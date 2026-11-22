#!/usr/bin/env python3
"""Exact integer/radical verification of the honeycomb spacing 2/sqrt(39) obstruction.
No external dependencies. Coordinates are (a,b) for a+b*omega, omega^2+omega+1=0.
"""
from collections import defaultdict

def N(z):
    a,b=z; return a*a-a*b+b*b

def cmp(A,B,U,V):
    """Sign of A+B*sqrt(U/V), with integer A,B and U>=0,V>0."""
    if U==0 or B==0:return (A>0)-(A<0)
    if A==0:return (B>0)-(B<0)
    if (A>0)==(B>0):return (A>0)-(A<0)
    d=A*A*V-B*B*U
    if d==0:return 0
    return ((d>0)-(d<0))*((A>0)-(A<0))

def H_points():
    # Norm<=24 suffices: all points in a radius sqrt(39)/2 disk whose center
    # lies in the fundamental translation parallelogram have norm below 25.
    return [(a,b) for a in range(-6,7) for b in range(-6,7)
            if (a+b)%3 and N((a,b))<=24]

def in_tile(p,q,eps):
    a,b=q[0]-p[0],q[1]-p[1]
    m=N((a,b)); U=39-m;V=3*m
    da,db=a-2*b,2*a-b
    A=p[0]+q[0];B=p[1]+q[1]
    # c=(p+q + eps*sqrt((39-m)/(3*m))*(da,db))/2.
    uA,uB=2*A-B,eps*(2*da-db)  # 6u
    vA,vB=A+B,eps*(da+db)      # 6v
    return (cmp(uA,uB,U,V)>=0 and cmp(uA-6,uB,U,V)<0 and
            cmp(vA,vB,U,V)>=0 and cmp(vA-6,vB,U,V)<0)

def within(r,p,q,eps):
    a,b=q[0]-p[0],q[1]-p[1]
    m=N((a,b)); U=39-m;V=3*m
    W=(2*r[0]-p[0]-q[0],2*r[1]-p[1]-q[1])
    det=a*W[1]-b*W[0]
    return cmp(N(W)-m,-3*eps*det,U,V)<=0

def rational_center(p,q,eps):
    # For the qualifying centers U/V happens to be a perfect rational square.
    from math import isqrt
    a,b=q[0]-p[0],q[1]-p[1]
    m=N((a,b)); U,V=39-m,3*m
    nu,den=isqrt(U*V),V
    assert nu*nu==U*V
    # center coordinates doubled, scaled to denominator 2*den
    return ((p[0]+q[0])*den+eps*nu*(a-2*b),
            (p[1]+q[1])*den+eps*nu*(2*a-b),2*den)

def canon(c):
    x,y,d=c
    # tile 6u=(2x-y)*3/d etc; point center in tile; represent 6*u,6*v
    from fractions import Fraction
    aa,bb=Fraction(2*x-y,3*d),Fraction(x+y,3*d)
    return (aa,bb)

H=H_points()
assert len(H)>50
counts=defaultdict(int)
maxn=0
maxcenters=set(); witnesses={}
candidate_count=0
for i,p in enumerate(H):
    for q in H[i+1:]:
        m=N((q[0]-p[0],q[1]-p[1]))
        if m>39:continue
        for eps in ((1,) if m==39 else (-1,1)):
            if not in_tile(p,q,eps):continue
            candidate_count+=1
            inside=[r for r in H if within(r,p,q,eps)]
            n=len(inside)
            counts[n]+=1
            assert n<=26,(p,q,eps,n)
            if n==26:
                c=rational_center(p,q,eps)
                # rational normalization; every such center is half integral in E
                assert (2*c[0])%c[2]==0 and (2*c[1])%c[2]==0
                c2=(2*c[0]//c[2],2*c[1]//c[2])
                maxcenters.add(c2)
                witnesses[c2]=tuple(inside)
                maxn=max(maxn,n)
assert maxn==26
# Expected half-coordinate representatives in 1-omega,1+2omega fundamental parallelogram
assert maxcenters=={(1,1),(1,0),(3,1),(3,2),(2,-1),(2,3)},maxcenters
assert len(witnesses)==6
# Each 26-point disk includes two pairs at squared distance 39 (diametral),
# belonging to the two nonassociate orientation classes of norm-39 vectors.
rot=lambda a,b:(a-b,a)
norm39={(a,b) for a in range(-8,9) for b in range(-8,9) if N((a,b))==39}
assert len(norm39)==12
orbits=[]
while norm39:
    w=next(iter(norm39));o=set();v=w
    for _ in range(6):o.add(v);v=rot(*v)
    assert v==w
    orbits.append(o);norm39-=o
assert len(orbits)==2
# Arithmetic collision check: for each possible norm-39 center lattice v*Z[omega],
# the 26 points in each candidate disk fail to represent all residue classes.
vecs=sorted(o for orbit in orbits for o in orbit)
def same_mod_v(p,q,v):
    a,b=v; x,y=p[0]-q[0],p[1]-q[1]
    m=N(v)
    return ((a-b)*x+b*y)%m==0 and (a*y-b*x)%m==0
for c2,pts in witnesses.items():
    diam={tuple(sorted((pts[i],pts[j]))) for i in range(len(pts)) for j in range(i+1,len(pts))
          if N((pts[i][0]-pts[j][0],pts[i][1]-pts[j][1]))==39}
    assert len(diam)==2,(c2,diam)
    dd={(b[0]-a[0],b[1]-a[1]) for a,b in diam}
    assert all(any(x in o for x in dd) for o in orbits)
    for v in vecs:
        assert any(same_mod_v(pts[i],pts[j],v)
                   for i in range(len(pts)) for j in range(i+1,len(pts)))
# Each potential hexagonal packing in maximal centers has min distance sqrt(39).
# Every difference lies in (1/6)T, so 6*nearest vector is an Eisenstein integer
# of norm 36*39=1404. All such solutions have both Eisenstein coordinates
# multiples of 6, hence every hexagonal center lattice lies in T.
V=[(a,b) for a in range(-50,51) for b in range(-50,51)
   if N((a,b))==36*39]
assert len(V)==12 and all(a%6==0 and b%6==0 for a,b in V)
# If center lattice is a sublattice of T, its min vector is norm39 and is
# one of the two orbits. Because both diametral orientations occur, one pair
# of honeycomb points in each 26-disk has a difference in the center lattice.
# Both endpoints then lie in distinct tangent disks (centers differ by that
# diameter vector): each 26-disk double-counts boundary honeycomb points.
# This contradicts density equality, which requires 26 distinct residues per cell.
print('PASS: exact pair-intersection candidates',candidate_count)
print('PASS: max occupancy',maxn,'at half-coordinate centers',sorted(maxcenters))
print('PASS: orientation orbits lengths',list(map(len,orbits)))
print('PASS: norm1404 vectors',sorted(V))
print('PASS: 72 center/orientation combinations each have a congruence collision')
print('PASS: each maximizer has two antipodal contact pairs, one in each orbit')
print('THEOREM: honeycomb at d=2/sqrt(39) is not coverable')
