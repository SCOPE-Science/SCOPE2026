#!/usr/bin/env python3
"""Exact chamber classification and independent numerical checks for random central
sections of the regular truncated octahedron. Requires Python 3 standard library.
"""
import itertools
import math
import random
from fractions import Fraction as F

V = sorted({tuple(s*a for s,a in zip(signs,perm))
            for perm in set(itertools.permutations((0,1,2)))
            for signs in itertools.product((-1,1),repeat=3)})
E = [(i,j) for i in range(len(V)) for j in range(i+1,len(V))
     if sum((p-q)**2 for p,q in zip(V[i],V[j])) == 2]
assert len(V)==24 and len(E)==36
assert all(sum(i==e[0] or i==e[1] for e in E)==3 for i in range(24))
# Facets are six coordinate caps and eight diagonal caps.
facets = [(i,s,2) for i in range(3) for s in (-1,1)]
facets += [(s,None,3) for s in itertools.product((-1,1),repeat=3)]
def tight(v,f):
    k,s,b=f
    if isinstance(k,int):return s*v[k]==b
    return sum(a*t for a,t in zip(k,v))==b
# correct facet tuples are (coordinate,s,2) and (signs,None,3)
for i,j in E:
    assert sum(tight(V[i],f) and tight(V[j],f) for f in facets)==2

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def det(a,b,c):return dot(a,(b[1]*c[2]-b[2]*c[1], b[2]*c[0]-b[0]*c[2], b[0]*c[1]-b[1]*c[0]))
def solid_angle(a,b,c):
    aa,bb,cc=(math.sqrt(dot(v,v)) for v in (a,b,c))
    den=aa*bb*cc + dot(a,b)*cc+dot(b,c)*aa+dot(c,a)*bb
    return 2*math.atan2(abs(det(a,b,c)),den)

rays={'A':(1,0,0),'E':(2,1,0),'B':(4,2,1),'C':(2,1,1),'D':(2,2,1)}
a,b,c,d,e=(rays[k] for k in ('A','B','C','D','E'))
Om_I=solid_angle(a,e,b)
Om_II=solid_angle(a,b,c)
Om_IV=solid_angle(b,c,d)
Om_I_expected=2*math.atan(1/(math.sqrt(105)+2*math.sqrt(21)+10+4*math.sqrt(5)))
Om_II_expected=2*math.atan(1/(math.sqrt(126)+4*math.sqrt(6)+11+2*math.sqrt(21)))
Om_IV_expected=2*math.atan(2/(3*math.sqrt(126)+33+7*math.sqrt(21)+13*math.sqrt(6)))
assert abs(Om_I-Om_I_expected)<1e-14
assert abs(Om_II-Om_II_expected)<1e-14
assert abs(Om_IV-Om_IV_expected)<1e-14
P10=12*Om_II/math.pi
P8=12*(Om_I+Om_IV)/math.pi
P6=1-P8-P10
assert abs(P6+P8+P10-1)<1e-14 and min(P6,P8,P10)>0

def n_cross(u):
    ds=[dot(u,v) for v in V]
    return sum(ds[i]*ds[j]<0 for i,j in E)

def intersections(u):
    ds=[dot(u,v) for v in V]
    pts=set()
    for i,j in E:
        if ds[i]*ds[j]<0:
            den=ds[i]-ds[j]
            pts.add(tuple((F(ds[i])*V[j][k]-F(ds[j])*V[i][k])/den for k in range(3)))
    return len(pts)

# Each cell of the normal chamber is connected; no vertex hyperplane other
# than y=x/2, z=x/2, z=y/2 meets its interior.
chamber=[
 ((F(1),F(1,4),F(1,16)), 8),  # y<x/2, z<y/2
 ((F(1),F(1,4),F(3,16)), 10), # y<x/2, z>y/2
 ((F(1),F(3,4),F(1,8)), 6),   # y>x/2, z<y/2
 ((F(1),F(3,4),F(7,16)), 8),  # y>x/2, y/2<z<x/2
 ((F(1),F(3,4),F(5,8)), 6),   # z>x/2
]
for u,ans in chamber:
    assert n_cross(u)==ans and intersections(u)==ans

# Independent 1D quadrature of spherical area in projective chart u=(1,y,z).
def primitive(z,y):return z/((1+y*y)*math.sqrt(1+y*y+z*z))
def simpson(lo,hi,zlo,zhi,N=6000):
    h=(hi-lo)/N
    acc=0.0
    for j in range(N+1):
        y=lo+j*h
        f=primitive(zhi(y),y)-primitive(zlo(y),y)
        acc+=(1 if j in (0,N) else 4 if j%2 else 2)*f
    return acc*h/3
O_i=simpson(0,.5,lambda y:0,lambda y:y/2)
O_ii=simpson(0,.5,lambda y:y/2,lambda y:y)
O_iv=simpson(.5,1,lambda y:y/2,lambda y:.5)
assert max(abs(O_i-Om_I),abs(O_ii-Om_II),abs(O_iv-Om_IV))<2e-13
assert abs(simpson(0,1,lambda y:0,lambda y:y)-math.pi/12)<2e-13

rng=random.Random(62324)
counts={6:0,8:0,10:0}
M=180000
for _ in range(M):
    xyz=sorted([abs(rng.gauss(0,1)) for _ in range(3)],reverse=True)
    u=(1.,xyz[1]/xyz[0],xyz[2]/xyz[0])
    n=n_cross(u)
    assert n in counts
    counts[n]+=1
for key,p in ((6,P6),(8,P8),(10,P10)):
    assert abs(counts[key]/M-p)<0.008
print('VERIFY_OK vertices=24 edges=36 facets=14 chambers=5 exact_crossing_classes=5 spherical_cones=3 quadratures=4',
      'sample_normals='+str(M), 'P6=%.12f P8=%.12f P10=%.12f'%(P6,P8,P10),
      'max_sampling_deviation=%.9f'%max(abs(counts[k]/M-p) for k,p in ((6,P6),(8,P8),(10,P10))))
