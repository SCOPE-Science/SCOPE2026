#!/usr/bin/env python3
"""Exact sign-cell certificate for central sections of a regular truncated tetrahedron.

Only the Python standard library is required. All cell and edge counts use integer
arithmetic; trigonometric evaluations and Monte Carlo are ancillary checks.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from fractions import Fraction
from math import acos, pi, sqrt
import random

V=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
P=[tuple(2*V[i][k]+V[j][k] for k in range(3))
   for i in range(4) for j in range(4) if i!=j]
assert len(set(P))==12

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def tight(p):
    # Eight facets: -3 <= v.p <= 5 for four original tetrahedron normals.
    dp=[dot(v,p) for v in V]
    assert all(-3<=d<=5 for d in dp)
    return {(i,s) for i,d in enumerate(dp) for s,t in ((-1,-3),(1,5)) if d==t}
T=list(map(tight,P))
assert all(len(z)==3 for z in T)
# Independent H-representation vertex enumeration using Cramer's rule.
facets=[(v,level) for v in V for level in (-3,5)]
found=set()
for (v0,b0),(v1,b1),(v2,b2) in combinations(facets,3):
    den=dot(v0,cross(v1,v2))
    if den==0: continue
    y=tuple(Fraction(b0*t+b1*s+b2*w,den)
            for t,s,w in zip(cross(v1,v2),cross(v2,v0),cross(v0,v1)))
    if all(-3<=dot(v,y)<=5 for v in V):found.add(y)
assert len(found)==12
assert found=={tuple(Fraction(t) for t in p) for p in P}
# Two vertices share an edge exactly when they share two supporting facet planes.
E=[(i,j) for i,j in combinations(range(12),2) if len(T[i]&T[j])==2]
assert len(E)==18
assert set(dot(P[i],P[j]) for i,j in E)=={7}
assert set(dot(p,p) for p in P)=={11}
# All 12 vertex planes are distinct, and no triple intersects in a line.
assert all(dot(P[k],cross(P[i],P[j]))!=0
           for i,j,k in combinations(range(12),3))

pattern_corners=Counter()
angle_coeff=defaultdict(Counter)
count_classes={}
for i,j in combinations(range(12),2):
    ray=cross(P[i],P[j]); assert ray!=(0,0,0)
    dij=dot(P[i],P[j]); assert abs(dij)<11
    for sign in (-1,1):
        r=tuple(sign*t for t in ray)
        fixed={k:int(dot(P[k],r)>0) for k in range(12) if k not in (i,j)}
        for si,sj in product((0,1),repeat=2):
            q=[None]*12
            q[i],q[j]=si,sj
            for k,sgn in fixed.items():q[k]=sgn
            q=tuple(q)
            N=sum(q[a]!=q[b] for a,b in E)
            assert 4<=N<=6
            count_classes[q]=N
            pattern_corners[q]+=1
            x=-(2*si-1)*(2*sj-1)*dij
            angle_coeff[N][x]+=1

assert len(count_classes)==134 # 12 general-position great circles: F=m(m-1)+2
assert len(pattern_corners)==134
number_of_cells=Counter(count_classes.values())
assert number_of_cells=={4:30,5:72,6:32},number_of_cells
assert sum(pattern_corners.values())==528 # 132 spherical vertices, four sectors each
assert Counter(sum(pattern_corners[q] for q in count_classes if count_classes[q]==N)
               for N in (4,5,6))==Counter({144:1,264:1,120:1})
expected={
 4:{-9:24,-7:48,1:48,5:24},
 5:{-7:24,-5:48,-1:96,7:48,9:48},
 6:{-9:24,1:48,5:24,7:24},
}
assert all(angle_coeff[N]==expected[N] for N in (4,5,6))

angles={t:acos(t/11) for t in (1,5,7,9)}
a,b,c,d=(angles[i] for i in (1,5,7,9))
prob={4:-3+(12*a+6*b-12*c-6*d)/pi,
      5:12+(-24*a-12*b+6*c+12*d)/pi,
      6:-8+(12*a+6*b+6*c-6*d)/pi}
for N in (4,5,6):
    cc=sum(pattern_corners[q] for q in count_classes if count_classes[q]==N)
    raw=sum(v*acos(x/11) for x,v in angle_coeff[N].items())-(cc-2*number_of_cells[N])*pi
    assert abs(raw/(4*pi)-prob[N])<1e-13
assert abs(sum(prob.values())-1)<5e-14
assert abs(sum(N*prob[N] for N in prob)-18*c/pi)<5e-14

rng=random.Random(170029)
ns=180000
samples=Counter()
for _ in range(ns):
    u=tuple(rng.gauss(0,1) for k in range(3))
    s=[dot(v,u)>0 for v in P]
    samples[sum(s[i]!=s[j] for i,j in E)]+=1
assert samples.keys()=={4,5,6}
max_error=max(abs(samples[N]/ns-prob[N]) for N in (4,5,6))
assert max_error<0.008
print('VERIFY_OK 12_integer_vertices=1 18_exact_edges=1 no_triple_planes=1')
print('cells_4_5_6',tuple(number_of_cells[n] for n in (4,5,6)))
print('angles_by_class',dict((n,dict(sorted(angle_coeff[n].items()))) for n in (4,5,6)))
print('probabilities',tuple(f'{prob[n]:.15f}' for n in (4,5,6)))
print('mean_vertices',f'{18*c/pi:.15f}')
print('simulation_samples',ns,'max_error',f'{max_error:.9f}')
