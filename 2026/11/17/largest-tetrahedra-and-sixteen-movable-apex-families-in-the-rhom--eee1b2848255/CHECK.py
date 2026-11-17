#!/usr/bin/env python3
"""Exact finite certificate for the rhombicuboctahedron tetrahedron theorem.
No numerical tolerances, third-party packages, or floating-point comparisons.
A pair (a,b) denotes a+b*sqrt(2); all determinant comparisons are exact.
"""
from itertools import combinations, product
from collections import Counter, defaultdict
from math import comb

ZERO=(0,0)
ONE=(1,0)
L=(1,1)
T=(3,1) # L+2

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def sign(x):
    a,b=x
    if a==0: return (b>0)-(b<0)
    if b==0: return (a>0)-(a<0)
    if a*b>0: return (a>0)-(a<0)
    d=a*a-2*b*b
    assert d!=0 # irrationality of sqrt(2) unless both zero
    return ((d>0)-(d<0))*((a>0)-(a<0))
def cmp(x,y):return sign(sub(x,y))
def positive_abs(x):return x if sign(x)>=0 else neg(x)
def cross(u,v):
    return (sub(mul(u[1],v[2]),mul(u[2],v[1])),
            sub(mul(u[2],v[0]),mul(u[0],v[2])),
            sub(mul(u[0],v[1]),mul(u[1],v[0])))
def dot(u,v):
    x=ZERO
    for a,b in zip(u,v):x=add(x,mul(a,b))
    return x
def determinant(a,b,c):return dot(a,cross(b,c))
def offset(a,b):return tuple(sub(x,y) for x,y in zip(a,b))

V=[]
for position in range(3):
    for signs in product((-1,1),repeat=3):
        V.append(tuple(mul((signs[j],0), L if j==position else ONE) for j in range(3)))
assert len(V)==24 and len(set(V))==24
N=len(V)
spectrum=Counter()
maxdet=ZERO
max_tetra=[]
for ids in combinations(range(N),4):
    a,b,c,d=(V[i] for i in ids)
    det=positive_abs(determinant(offset(b,a),offset(c,a),offset(d,a)))
    spectrum[det]+=1
    relation=cmp(det,maxdet)
    if relation>0:
        maxdet=det
        max_tetra=[ids]
    elif relation==0:
        max_tetra.append(ids)
assert sum(spectrum.values())==comb(24,4)==10626
# The following independently expected table is expressed in the basis (1,L).
expected_L=[
 (0,0,876),(4,0,384),(-4,4,816),(8,0,216),(0,4,816),
 (4,4,1776),(-4,8,96),(8,4,240),(0,8,1416),(4,8,864),
 (-4,12,48),(8,8,672),(0,12,144),(4,12,1056),(8,12,192),
 (0,16,114),(12,12,48),(4,16,192),(8,16,408),(4,20,48),
 (16,16,12),(8,20,144),(12,20,48)]
expected={(a+b,b):count for a,b,count in expected_L}
assert spectrum==expected, 'Exact tetrahedral determinant spectrum is different'
assert len(spectrum)==23
assert maxdet==(32,20) and len(max_tetra)==48
# independently reproduce the absolute spectrum using only tetrahedra through V[0]:
anchored=Counter()
for b,c,d in combinations(range(1,N),3):
    val=positive_abs(determinant(offset(V[b],V[0]),offset(V[c],V[0]),offset(V[d],V[0])))
    anchored[val]+=1
assert sum(anchored.values())==comb(23,3)==1771
assert all(spectrum[value]==6*freq for value,freq in anchored.items())
assert len(anchored)==len(spectrum)
# All eight triangular faces and their two independent maximizing base triangles.
faces=set()
for signs in product((-1,1),repeat=3):
    normal=tuple((s,0) for s in signs)
    heights=[dot(normal,v) for v in V]
    assert all(cmp(h,T)<=0 for h in heights)
    face=tuple(i for i,h in enumerate(heights) if cmp(h,T)==0)
    assert len(face)==3
    faces.add(face)
assert len(faces)==8
apices=defaultdict(set)
for ids in max_tetra:
    for missing in range(4):
        base=ids[:missing]+ids[missing+1:]
        apices[base].add(ids[missing])
families=[]
for base, apexset in apices.items():
    if len(apexset)==3:
        face=tuple(sorted(apexset))
        assert face in faces
        a,b,c=(V[i] for i in base)
        signed=[determinant(offset(b,a),offset(c,a),offset(V[i],a)) for i in face]
        assert len(set(signed))==1
        assert positive_abs(signed[0])==maxdet
        families.append((base,face))
assert len(families)==16
assert Counter(face for base,face in families)==Counter({f:2 for f in faces})
assert Counter(len(s) for s in apices.values())==Counter({1:96,2:24,3:16})
# The 48 maximizing four-vertex tetrahedra are partitioned as
# the 16 base-triangle / apex-face families, with 3 vertices per face.
covered={tuple(sorted(base+(i,))) for base,face in families for i in face}
assert len(covered)==48 and covered==set(max_tetra)
print('RHOMBICUBOCTAHEDRON_TETRA_PASS vertices=24 quadruples=10626 spectrum=23 max_tetra=48')
print('max_6volume=32+20sqrt(2); max_volume=(16+10sqrt(2))/3')
print('face_families=16 triangular_faces=8 area_fraction=(1+5sqrt(2))/56')
for a,b,count in expected_L:
    print(f'{a:+d}{b:+d}L  {count}')
