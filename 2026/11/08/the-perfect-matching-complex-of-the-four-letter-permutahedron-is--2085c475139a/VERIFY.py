#!/usr/bin/env python3
"""Reproduce the integral Morse certificate for a four-letter permutahedral perfect-matching complex.

Python >=3.10; standard library only. Run: python VERIFY.py
The graph has one vertex per permutation of 0,1,2,3 and one edge per swap of adjacent positions.
Bit i denotes edge i of its lexicographically sorted edge list.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from fractions import Fraction
from itertools import permutations

V = list(permutations(range(4)))
vid = {p:i for i,p in enumerate(V)}
E = sorted({tuple(sorted((i,vid[p[:j]+(p[j+1],p[j])+p[j+2:]])))
            for i,p in enumerate(V) for j in range(3)})
assert len(V)==24 and len(E)==36
adj = {i:set() for i in range(24)}
for a,b in E:
    adj[a].add(b); adj[b].add(a)
assert all(len(adj[v])==3 for v in adj)
eid = {e:i for i,e in enumerate(E)}

@lru_cache(None)
def number_of_perfect_matchings(remaining):
    if not remaining:
        return 1
    a = (remaining & -remaining).bit_length()-1
    return sum(number_of_perfect_matchings(remaining^(1<<a)^(1<<b))
               for b in adj[a] if remaining & (1<<b))

def enumerate_perfect_matchings(remaining, edge_mask=0):
    if not remaining:
        yield edge_mask
        return
    a = (remaining & -remaining).bit_length()-1
    for b in sorted(adj[a]):
        if remaining & (1<<b):
            edge_index = eid[tuple(sorted((a,b)))]
            yield from enumerate_perfect_matchings(
                remaining^(1<<a)^(1<<b),edge_mask|(1<<edge_index))

facets = sorted(enumerate_perfect_matchings((1<<24)-1))
assert len(facets)==number_of_perfect_matchings((1<<24)-1)==169
assert len(set(facets))==169 and all(f.bit_count()==12 for f in facets)
faces = {0}
for f in facets:
    sub = f
    while sub:
        faces.add(sub)
        sub=(sub-1)&f
f_vector = tuple(sum(1 for f in faces if f.bit_count()==d+1) for d in range(12))
assert len(faces)==379056
assert f_vector==(36,558,4656,21003,54360,87928,94440,69003,34020,10854,2028,169)

def rank_over_q(M):
    if not M:
        return 0
    a = [[Fraction(v) for v in row] for row in M]
    m,n=len(a),len(a[0]);r=0
    for c in range(n):
        pivot=next((i for i in range(r,m) if a[i][c]!=0),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        w=a[r][c]
        for j in range(c,n):a[r][j]/=w
        for i in range(r+1,m):
            if a[i][c]:
                z=a[i][c]
                for j in range(c,n):a[i][j]-=z*a[r][j]
        r+=1
        if r==m:break
    return r

def det_bareiss(A):
    n=len(A)
    if not n:return 1
    assert all(len(row)==n for row in A)
    a=[row[:] for row in A]
    sign=1;prev=1
    for k in range(n-1):
        if a[k][k]==0:
            p=next((j for j in range(k+1,n) if a[j][k]!=0),None)
            if p is None:return 0
            a[k],a[p]=a[p],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numer=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numer%prev==0
                a[i][j]=numer//prev
        for i in range(k+1,n):a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

def multiply_is_zero(A,B):
    return all(sum(A[i][k]*B[k][j] for k in range(len(B)))==0
               for i in range(len(A)) for j in range(len(B[0])))

def certificate(order):
    remaining=set(faces)
    upper={}; lower={}
    for v in order:
        bit=1<<v
        for a in list(remaining):
            if not a&bit and (a|bit) in remaining:
                b=a|bit
                remaining.remove(a);remaining.remove(b)
                upper[a]=b;lower[b]=a
    assert len(upper)==len(lower)
    assert 2*len(upper)+len(remaining)==len(faces)
    assert all((upper[a]^a).bit_count()==1 for a in upper)

    # Exhaustively topologically sort the oriented Hasse graph: matched covers
    # point up, and unmatched covers point down.
    indegree=dict.fromkeys(faces,0)
    incidences=0
    for cell in faces:
        todo=cell
        while todo:
            bit=todo&-todo;todo^=bit
            face=cell^bit
            if upper.get(face)==cell:indegree[cell]+=1
            else:indegree[face]+=1
            incidences+=1
    queue=deque(cell for cell in faces if indegree[cell]==0)
    visited=0
    while queue:
        cell=queue.popleft();visited+=1
        todo=cell
        while todo:
            bit=todo&-todo;todo^=bit
            face=cell^bit
            if upper.get(face)!=cell:
                indegree[face]-=1
                if indegree[face]==0:queue.append(face)
        if cell in upper:
            partner=upper[cell]
            indegree[partner]-=1
            if indegree[partner]==0:queue.append(partner)
    assert incidences==2550660
    assert visited==len(faces)

    @lru_cache(None)
    def reduction(cell):
        if cell in remaining:return {cell:1}
        if cell in lower:return {}
        partner=upper[cell]
        coordinates=[i for i in range(36) if partner & (1<<i)]
        pivot_pos=coordinates.index((partner^cell).bit_length()-1)
        out=defaultdict(int)
        for pos,i in enumerate(coordinates):
            if pos==pivot_pos:continue
            for critical,coef in reduction(partner^(1<<i)).items():
                out[critical]-=((-1)**(pos+pivot_pos))*coef
        return {k:v for k,v in out.items() if v}

    dims=Counter(cell.bit_count()-1 for cell in remaining)
    matrices={}
    for d in sorted(dims):
        bottom=sorted(cell for cell in remaining if cell.bit_count()==d)
        top=sorted(cell for cell in remaining if cell.bit_count()==d+1)
        if not bottom or not top:continue
        pos={cell:i for i,cell in enumerate(bottom)}
        M=[[0]*len(top) for _ in bottom]
        for j,cell in enumerate(top):
            for q,i in enumerate(v for v in range(36) if cell & (1<<v)):
                for lower_cell,coef in reduction(cell^(1<<i)).items():
                    M[pos[lower_cell]][j]+=((-1)**q)*coef
        matrices[d]=M
    for d in matrices:
        if d+1 in matrices:assert multiply_is_zero(matrices[d],matrices[d+1])
    return len(upper),dict(sorted(dims.items())),matrices,visited

forward_pairs,forward_critical,forward,forward_visited=certificate(range(36))
reverse_pairs,reverse_critical,reverse,reverse_visited=certificate(reversed(range(36)))
assert forward_pairs==189500 and forward_critical=={3:10,4:40,5:6}
assert reverse_pairs==189499 and reverse_critical=={3:7,4:40,5:10,6:1}
assert (len(forward[4]),len(forward[4][0]))==(10,40)
assert (len(forward[5]),len(forward[5][0]))==(40,6)
assert rank_over_q(forward[4])==10 and rank_over_q(forward[5])==5
assert [rank_over_q(reverse[d]) for d in (4,5,6)]==[7,8,1]
# Explicit unit-determinant maximal-rank submatrices certify primitive images.
rows4=tuple(range(10))
cols4=(0,3,4,6,7,16,20,24,32,37)
rows5=(0,5,8,9,19)
cols5=(1,2,3,4,5)
minor4=det_bareiss([[forward[4][r][c] for c in cols4] for r in rows4])
minor5=det_bareiss([[forward[5][r][c] for c in cols5] for r in rows5])
assert (minor4,minor5)==(1,-1)
assert multiply_is_zero(forward[4],forward[5])
# A one-dimensional 5-cycle and 25 four-cycles remain after integral cancellations.
h4=(40-10)-5
h5=6-5
assert (h4,h5)==(25,1)
print('graph: vertices=24 edges=36 perfect_matchings=169')
print('faces_including_empty=379056 facets=169 dimension=11')
print('f_vector='+','.join(map(str,f_vector)))
print('oriented_hasse_incidences=2550660 forward_and_reverse_acyclic=PASS')
print('ascending_pairs=189500 critical={3:10,4:40,5:6}')
print('ascending_boundary_ranks={4:10,5:5} composition_zero=PASS')
print('ascending_unit_minor_10x10=1 ascending_unit_minor_5x5=-1')
print('descending_pairs=189499 critical={3:7,4:40,5:10,6:1}')
print('descending_boundary_ranks={4:7,5:8,6:1} compositions_zero=PASS')
print('integral_reduced_homology: H4=Z^25 H5=Z all_others_zero')
print('homotopy: wedge(25,S4) wedge S5 (CW cancellation)')
print('PERMUTOHEDRAL_PERFECT_MATCHING_WEDGE_VERIFIED')
