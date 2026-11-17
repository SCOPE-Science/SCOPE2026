#!/usr/bin/env python3
"""Exact standalone finite certificate for the matching complex of P4 □ P5.

Requires Python 3.10+ and SymPy. Run: python verify_grid_4x5.py
"""
from collections import Counter, deque
from functools import lru_cache
from hashlib import sha256
import itertools
import json
import math
import sympy as sp
from sympy.polys.domains import ZZ
from sympy.matrices.normalforms import smith_normal_form

R, C = 4, 5
edges = []
for r in range(R):
    for c in range(C):
        v = r*C+c
        if r+1 < R:
            edges.append((v, (r+1)*C+c))
        if c+1 < C:
            edges.append((v, v+1))
assert len(edges) == 31 and len(set(edges)) == 31
occupied = [(1<<u)|(1<<v) for u, v in edges]
faces = []
def enumerate_faces(edge_mask, used_vertices, begin):
    faces.append(edge_mask)
    for k in range(begin, len(edges)):
        if not (occupied[k] & used_vertices):
            enumerate_faces(edge_mask | (1<<k), used_vertices | occupied[k], k+1)
enumerate_faces(0, 0, 0)
assert len(set(faces)) == len(faces)
face_index = {face:i for i,face in enumerate(faces)}
f_counts = [0]*11
for mask in faces:
    f_counts[mask.bit_count()] += 1
EXPECTED_F = [1,31,395,2696,10769,25835,36771,29580,12181,2111,95]
assert f_counts == EXPECTED_F, (f_counts, EXPECTED_F)

# Independently enumerate matching-polynomial coefficients via vertex deletion.
neighbors = [0]*(R*C)
for u,v in edges:
    neighbors[u] |= 1<<v
    neighbors[v] |= 1<<u
@lru_cache(None)
def matching_polynomial(available):
    if not available:
        return (1,)
    low = available & -available
    v = low.bit_length()-1
    rest = available ^ low
    total = list(matching_polynomial(rest))
    adjacency = neighbors[v] & rest
    while adjacency:
        bit = adjacency & -adjacency
        adjacency ^= bit
        poly = matching_polynomial(rest ^ bit)
        while len(total) <= len(poly):
            total.append(0)
        for i,x in enumerate(poly):
            total[i+1] += x
    return tuple(total)
assert list(matching_polynomial((1<<(R*C))-1)) == f_counts

# Forman matching, in fixed edge order; empty face remains unmatched (unaugmented).
mate = [-1]*len(faces)
pivot_counts = []
for k in range(len(edges)):
    bit = 1<<k
    number = 0
    for i,mask in enumerate(faces):
        if mask and mate[i]<0 and not (mask & bit):
            j = face_index.get(mask | bit)
            if j is not None and mate[j]<0:
                mate[i], mate[j] = j, i
                number += 1
    pivot_counts.append(number)
EXPECTED_PIVOTS = [31297,15629,0,0,4150,2839,1569,1624,973,0,0,632,91,172,0,266,185,204,260,54,49,29,59,23,26,12,29,15,3,6,9]
assert pivot_counts == EXPECTED_PIVOTS
assert sum(pivot_counts) == 60205
critical = {i for i in range(1, len(faces)) if mate[i]<0}
critical_by_dim = {}
for i in sorted(critical):
    d = faces[i].bit_count()-1
    critical_by_dim.setdefault(d,[]).append(i)
assert {d:len(items) for d,items in critical_by_dim.items()} == {0:1,5:5,6:47,7:1}
assert len(faces)-1 == 2*sum(pivot_counts)+len(critical)

# Check matching acyclicity by topological sort of the FULL Hasse orientation:
# matched covers point up; all other covers point down.
in_degree = [0]*len(faces)
for i,mask in enumerate(faces):
    for k in range(len(edges)):
        bit=1<<k
        if mask&bit:
            lower=face_index[mask^bit]
            if mate[lower]==i:
                in_degree[i]+=1
            else:
                in_degree[lower]+=1
queue=deque(i for i,degree in enumerate(in_degree) if degree==0)
seen=0
while queue:
    i=queue.popleft()
    seen+=1
    mask=faces[i]
    up=mate[i]
    if up>=0 and faces[up].bit_count()==mask.bit_count()+1:
        in_degree[up]-=1
        if in_degree[up]==0:
            queue.append(up)
    for k in range(len(edges)):
        bit=1<<k
        if mask&bit:
            lower=face_index[mask^bit]
            if mate[lower]!=i:
                in_degree[lower]-=1
                if in_degree[lower]==0:
                    queue.append(lower)
assert seen == len(faces), (seen, len(faces))

# Signed algebraic Morse reduction on the actual integral simplicial boundary.
@lru_cache(None)
def reduce_face(i):
    if i in critical:
        return {i:1}
    j = mate[i]
    if j<0:  # empty face; never encountered from positive-dimensional boundaries
        return {}
    mask=faces[i]
    upper=faces[j]
    if upper.bit_count()<mask.bit_count():
        return {}
    bits=[k for k in range(len(edges)) if (upper>>k)&1]
    removed=(upper^mask).bit_length()-1
    pivot_sign=(-1)**bits.index(removed)
    result={}
    for position,k in enumerate(bits):
        lower=upper^(1<<k)
        if lower==mask:
            continue
        coefficient=-pivot_sign*((-1)**position)
        for a,v in reduce_face(face_index[lower]).items():
            result[a]=result.get(a,0)+coefficient*v
    return {a:v for a,v in result.items() if v}

def morse_boundary(i):
    mask=faces[i]
    bits=[k for k in range(len(edges)) if (mask>>k)&1]
    result={}
    for position,k in enumerate(bits):
        for a,v in reduce_face(face_index[mask^(1<<k)]).items():
            result[a]=result.get(a,0)+((-1)**position)*v
    return {a:v for a,v in result.items() if v}

five=critical_by_dim[5]
six=critical_by_dim[6]
seven=critical_by_dim[7]
M=sp.zeros(len(five),len(six))
for j,i in enumerate(six):
    boundary=morse_boundary(i)
    assert set(boundary).issubset(set(five))
    for a,v in boundary.items():
        M[five.index(a),j]=v
V=sp.Matrix([morse_boundary(seven[0]).get(i,0) for i in six])
assert M*V==sp.zeros(5,1)
assert Counter(int(x) for x in M)==Counter({0:197,-1:23,1:15})
assert [(i,int(x)) for i,x in enumerate(V) if x] == [(14,1),(34,-1),(36,1),(43,1),(44,1)]
assert int(M[:,[0,1,2,15,19]].det())==-1
assert [abs(int(smith_normal_form(M,domain=ZZ)[i,i])) for i in range(5)] == [1]*5
assert math.gcd(*(abs(int(x)) for x in V))==1
assert sum((-1)**k*x for k,x in enumerate(f_counts)) == -41 # minus the reduced Euler characteristic
print('4x5 Cartesian grid: vertices=20, edges=31')
print('Matching polynomial coefficients:', f_counts)
print('Independent deletion-contraction census: PASS')
print('Nonempty simplices:', len(faces)-1)
print('Matched pairs:', sum(pivot_counts))
print('Pivot-stage counts:', pivot_counts)
print('Full oriented Hasse DAG: acyclic, visited', seen)
print('Critical cells by dimension:', {d:len(v) for d,v in sorted(critical_by_dim.items())})
print('Integral Morse boundary (C6 -> C5): 5x47; unit minor -1 on columns [0,1,2,15,19]')
print('Integral Morse boundary (C7 -> C6): five unit entries, primitive')
print('Boundary composition: zero; H6 rank = 47 - 5 - 1 = 41')
print('Homotopy: wedge of 41 six-spheres, via primitive higher-cell cancellations')
print('All exact checks: PASS')
