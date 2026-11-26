#!/usr/bin/env python3
"""Exact-rational polytope check for barycentrically capped tetrahedra.
Run with Python 3 standard library; no external packages required.
The proof, not finite checks, establishes all real parameters.
"""
from fractions import Fraction as F
from itertools import combinations


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
G=((F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1)),(F(-1),F(-1),F(-1)))
B=(F(0),F(0),F(0),F(1)) # lambda_i=dot(G[i],x)+B[i]

def solve3(rows,rhs):
    aa=[list(row)+[rhs[i]] for i,row in enumerate(rows)]
    for j in range(3):
        pivot=next((i for i in range(j,3) if aa[i][j]),None)
        if pivot is None:return None
        aa[j],aa[pivot]=aa[pivot],aa[j]
        a=aa[j][j]
        aa[j]=[v/a for v in aa[j]]
        for i in range(3):
            if i!=j:
                a=aa[i][j]
                aa[i]=[x-a*y for x,y in zip(aa[i],aa[j])]
    return tuple(aa[i][3] for i in range(3))

def vertices(t):
    planes=[(i,F(0)) for i in range(4)]+[(i,t) for i in range(4)]
    out=set()
    for three in combinations(planes,3):
        x=solve3([G[i] for i,z in three],[z-B[i] for i,z in three])
        if x is not None and all(0<=dot(g,x)+b<=t for g,b in zip(G,B)):
            out.add(x)
    return tuple(sorted(out))

def hull_2d(points):
    # Monotone chain works over exact ordered rational pairs.
    pts=sorted(set(points))
    if len(pts)<=2:return pts
    def c(a,b,z): return (b[0]-a[0])*(z[1]-a[1])-(b[1]-a[1])*(z[0]-a[0])
    lower=[]
    for x in pts:
        while len(lower)>=2 and c(lower[-2],lower[-1],x)<=0:lower.pop()
        lower.append(x)
    upper=[]
    for x in pts[::-1]:
        while len(upper)>=2 and c(upper[-2],upper[-1],x)<=0:upper.pop()
        upper.append(x)
    return lower[:-1]+upper[:-1]

def get_faces(vs,t):
    out=[]
    for i in range(4):
      for z,sgn in ((F(0),-1),(t,1)):
        on=[v for v in vs if dot(G[i],v)+B[i]==z]
        if len(on)<3:continue
        dims=[j for j in range(3) if j!=i] if i<3 else [0,1]
        points=hull_2d([(v[dims[0]],v[dims[1]]) for v in on])
        if len(points)<3:continue
        lookup={(v[dims[0]],v[dims[1]]):v for v in on}
        ring=[lookup[p] for p in points]
        sumcross=(F(0),F(0),F(0))
        for a,b in zip(ring,ring[1:]+ring[:1]):
            zc=cross(a,b)
            sumcross=tuple(x+y for x,y in zip(sumcross,zc))
        N=tuple(sgn*x for x in G[i])
        if dot(N,sumcross)<0:sumcross=tuple(-x for x in sumcross)
        assert dot(N,sumcross)>0,(t,i,z)
        out.append((N,ring,sumcross))
    return out

def areas(t):
    if t<=F(1,3):return F(0),(4*t-1)**2
    if t<=F(1,2):return (3*t-1)**2,(1-t)**2-3*(1-2*t)**2
    return 1-3*(1-t)**2,(1-t)**2

def check(t):
    vs=vertices(t); faces=get_faces(vs,t)
    vl=F(0);mix=F(0)
    for N,ring,s in faces:
        norm=dot(N,N)
        area_factor=dot(N,s)/norm
        vl+=dot(N,ring[0])*area_factor/F(6)
        mixed_support=max(-dot(N,v) for v in vs)
        mix+=mixed_support*area_factor/F(6)
    l,u=areas(t)
    if t<F(1,3):
        expected_vol=(4*t-1)**3/6
        expected_mix=3*expected_vol
    else:
        expected_vol=(l+(4*t-1)*u)/6
        expected_mix=((4*t-1)*l+u)/6
    assert vl==expected_vol,(t,'volume',vl,expected_vol)
    assert mix==expected_mix,(t,'mixed volume',mix,expected_mix)
    return len(vs),len(faces),vl,mix

def main():
    samples=[F(13,50),F(3,10),F(1,3),F(7,20),F(2,5),F(9,20),F(1,2),F(11,20),F(3,5),F(3,4),F(9,10),F(1)]
    for t in samples:
        n,f,v,m=check(t)
        print(f't={t}: vertices={n} facets={f} volume={v} mixed={m} ratio={m/v}')
    print(f'PASS: {len(samples)} exact-rational vertex/facet reconstructions; '
          f'{2*len(samples)} exact volume and mixed-volume equalities.')

if __name__=='__main__':main()
