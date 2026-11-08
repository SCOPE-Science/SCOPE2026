#!/usr/bin/env python3
"""Exact integral discrete-Morse verifier for the Pappus two-independence complex.

Requires only Python 3.10+. All integers are exact. The graph uses its
published Hamiltonian LCF description [5,7,-7,7,-7,-5]^3.
"""
from collections import Counter, deque, defaultdict
from math import gcd
import random

N = 18
LCF = [5, 7, -7, 7, -7, -5] * 3
edges = set()
for v in range(N):
    edges.add(tuple(sorted((v, (v+1) % N))))
    edges.add(tuple(sorted((v, (v+LCF[v]) % N))))
edges = sorted(edges)
adj = [0] * N
for u, v in edges:
    assert u != v
    adj[u] |= 1 << v
    adj[v] |= 1 << u
assert len(edges) == 27 and all(x.bit_count() == 3 for x in adj)


def valid_direct(mask):
    for i in range(N):
        if mask & (1 << i) and (mask & adj[i]).bit_count() > 1:
            return False
    return True

# Enumerate by two mathematically distinct tests of admissibility.
faces = [m for m in range(1 << N) if valid_direct(m)]
face_set = set(faces)
dynamic = {0}
for m in range(1, 1 << N):
    bit = m & -m
    i = bit.bit_length()-1
    parent = m ^ bit
    neighbors = parent & adj[i]
    if parent in dynamic and neighbors.bit_count() <= 1:
        if not neighbors or (adj[neighbors.bit_length()-1] & parent) == 0:
            dynamic.add(m)
assert face_set == dynamic
f = Counter(m.bit_count()-1 for m in faces)
assert [f[i] for i in range(-1, 10)] == [1,18,153,762,2394,4806,6027,4428,1728,308,27]
assert len(faces) == 20652
print('VERTICES', N, 'EDGES', len(edges), 'FACES_INCLUDING_EMPTY', len(faces))
print('FACE_VECTOR_DIMENSIONS_MINUS_ONE_TO_NINE', *[f[i] for i in range(-1,10)])


def matching(order):
    unmatched = face_set.copy()
    pairs = []
    for v in order:
        b = 1 << v
        for m in faces:
            if m in unmatched and not (m & b) and (m | b) in unmatched:
                unmatched.remove(m)
                unmatched.remove(m|b)
                pairs.append((m,m|b))
    assert len(pairs)*2 + len(unmatched) == len(faces)
    return unmatched, pairs


def signed_boundary(m):
    out = []
    s = 1
    for i in range(N):
        if m & (1 << i):
            out.append((m^(1<<i),s))
            s = -s
    return out


def acyclic_certificate(pairs):
    matched = dict(pairs)
    ids = {m:i for i,m in enumerate(faces)}
    children = [[] for _ in faces]
    indeg = [0]*len(faces)
    incidences = 0
    for m in faces[1:]:
        hi = ids[m]
        for low,_ in signed_boundary(m):
            li = ids[low]
            u,v = (li,hi) if matched.get(low) == m else (hi,li)
            children[u].append(v)
            indeg[v] += 1
            incidences += 1
    ready = deque(i for i,d in enumerate(indeg) if d == 0)
    seen=0
    while ready:
        u=ready.popleft()
        seen+=1
        for v in children[u]:
            indeg[v]-=1
            if indeg[v]==0:
                ready.append(v)
    assert seen==len(faces)
    return incidences


def gradient_matrix(crit,pairs,degree=5):
    lower = sorted(x for x in crit if x.bit_count()-1 == degree)
    upper = sorted(x for x in crit if x.bit_count()-1 == degree+1)
    downpair = {lo:hi for lo,hi in pairs if lo.bit_count()-1 == degree}
    # Dependencies on the lower matched faces, for exact unit-pivot elimination.
    nexts = {lo:set() for lo in downpair}
    indeg = {lo:0 for lo in downpair}
    for lo,hi in downpair.items():
        for v,_ in signed_boundary(hi):
            if v != lo and v in downpair:
                assert v != lo
                if v not in nexts[lo]:
                    nexts[lo].add(v)
                    indeg[v] += 1
    queue=deque(lo for lo,d in indeg.items() if d==0)
    topo=[]
    while queue:
        lo=queue.popleft();topo.append(lo)
        for nxt in nexts[lo]:
            indeg[nxt]-=1
            if indeg[nxt]==0:queue.append(nxt)
    assert len(topo)==len(downpair)

    # Independent recursion: each degree-d face maps to a vector of
    # critical degree-d generators. Eliminated upper d-cells map to zero.
    lower_index={v:i for i,v in enumerate(lower)}
    reductions={v:tuple(int(i==j) for i in range(len(lower))) for v,j in lower_index.items()}
    for lo in reversed(topo):
        hi=downpair[lo]
        B=signed_boundary(hi)
        pivot=dict(B)[lo]
        assert pivot in (-1,1)
        coeff=[0]*len(lower)
        for v,s in B:
            if v==lo:continue
            vvec=reductions.get(v)
            if vvec:
                for k,w in enumerate(vvec):coeff[k]-=s*pivot*w
        reductions[lo]=tuple(coeff)
    # Other degree-d cells are paired as upper cells of dimension d-1.
    def projection(v):
        return reductions.get(v, (0,)*len(lower))
    matrix2=[]
    for hi in upper:
        coeff=[0]*len(lower)
        for v,s in signed_boundary(hi):
            for k,w in enumerate(projection(v)):
                coeff[k]+=s*w
        matrix2.append(coeff)

    # Separate direct chain reduction, not using computed projections.
    matrix1=[]
    for hi in upper:
        C=defaultdict(int)
        for lo,s in signed_boundary(hi):C[lo]+=s
        for lo in topo:
            num=C[lo]
            if num:
                hi2=downpair[lo]
                sign=dict(signed_boundary(hi2))[lo]
                for v,s in signed_boundary(hi2):
                    C[v]-=num*s*sign
        assert all(C[lo]==0 for lo in downpair)
        matrix1.append([C[lo] for lo in lower])
    assert matrix1==matrix2
    return lower,upper,matrix1,len(downpair)


def one_run(name,order,expected_counts,expected_matrix=None):
    crit,pairs=matching(order)
    counts=Counter(c.bit_count()-1 for c in crit)
    assert dict(counts)==expected_counts
    hasse=acyclic_certificate(pairs)
    assert hasse==120240
    lower,upper,M,np=gradient_matrix(crit,pairs)
    print('MATCHING',name,'PAIRS',len(pairs),'CRITICAL_DIMENSIONS',sorted(counts.items()),'HASSE',hasse)
    print('MORSE_BOUNDARY_COLUMNS',name,M)
    if expected_matrix is not None:
        assert M==expected_matrix
    return lower,upper,M

# The empty face is paired in both runs; by Forman's theorem this adds
# one basepoint in dimension zero to the Morse CW model.
lo1,hi1,m1=one_run('natural', list(range(N)), {5:9,6:1}, [[0]*9])
alt=list(range(N));random.Random(0).shuffle(alt)
lo2,hi2,m2=one_run('alternate',alt,{5:10,6:2})
# Alternate Morse boundary must have Smith invariants (1,0).
col1,col2=m2
rank2=any(col1[i]*col2[j]-col1[j]*col2[i] for i in range(10) for j in range(i+1,10))
content=0
for c in col1+col2:content=gcd(content,abs(c))
assert not rank2 and content==1
print('ALTERNATE_SMITH',1,0)
# An exact sanity-check: reduced Euler characteristic is -8.
red_euler=-1+sum((-1)**i*f[i] for i in range(0,10))
assert red_euler==-8 # one empty face contributes -1 in the reduced Euler sum
print('EULER',red_euler)
print('INTEGRAL_HOMOTOPY', 'wedge(9*S5,S6)')
print('ALL_CHECKS_PASS')
