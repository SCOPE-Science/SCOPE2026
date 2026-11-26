#!/usr/bin/env python3
"""Exact self-contained finite verifier for the independence complex of C8 x K4.
Requires Python >=3.10 and SymPy. All arithmetic integral.
"""
from collections import Counter, deque, defaultdict
from functools import lru_cache
from sympy import zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form

N, K = 8, 4
NV = N*K
adj=[]
for i in range(N):
    for c in range(K):
        adj.append(sum(1 << (j*K+d) for j in ((i-1)%N,(i+1)%N)
                       for d in range(K) if d != c))
assert len(adj)==NV and all(not (adj[i] & (1<<i)) for i in range(NV))
assert all(bool(adj[i] & (1<<j)) == bool(adj[j] & (1<<i)) for i in range(NV) for j in range(NV))

# Independent-set generation by adding one vertex at a time, each eligible face once.
faces=[0]
for v in range(NV):
    faces += [s | (1<<v) for s in faces if not s & adj[v]]
F=set(faces)
assert len(F)==len(faces)
fc=Counter(s.bit_count() for s in faces)
assert sum(fc.values())==196227
assert max(fc)==16

# Independent cross-check: exact column transfer count, tracking the number of selected vertices.
compat=lambda a,b: (a==0 or b==0 or (a==b and a.bit_count()==1))
transfer=Counter()
for first in range(1<<K):
    dp={(first,first.bit_count()):1}
    for _ in range(1,N):
        nx=defaultdict(int)
        for (last,d),ways in dp.items():
            for b in range(1<<K):
                if compat(last,b):nx[(b,d+b.bit_count())]+=ways
        dp=nx
    for (last,d),ways in dp.items():
        if compat(last,first):transfer[d]+=ways
assert transfer==fc, (transfer,fc)
print('VERIFY_OK faces=%d face_vector=%r'%(len(F),[fc[d] for d in range(1,17)]),flush=True)

# Vertex-ordered matching. Exclude empty face to retain the ordinary Morse 0-cell.
unpaired=set(F)-{0}
up={};down={}
for v in range(NV):
    bit=1<<v
    for s in faces:
        t=s|bit
        if s and not s&bit and s in unpaired and t in unpaired:
            up[s]=t; down[t]=s
            unpaired.remove(s);unpaired.remove(t)
critical=unpaired
crit_counts=Counter(s.bit_count()-1 for s in critical)
assert crit_counts=={0:1,4:24,5:27},crit_counts
assert len(up)==len(down)==98087
print('VERIFY_OK matched_pairs=%d critical_cells=%r'%(len(up),dict(crit_counts)),flush=True)

# Complete directed Hasse graph: matched incidences point upward, others downward.
# Compute degrees and enumerate outgoing edges without storing the incidence graph.
def facets(s):
    t=s
    i=0
    while t:
        b=t & -t
        t-=b
        yield s^b,(-1 if i%2 else 1)
        i+=1
indeg={s:0 for s in F if s}
incidence_count=0
for s in faces:
    if not s:continue
    for t,_ in facets(s):
        if not t:continue
        incidence_count+=1
        if down.get(s)==t:
            indeg[s]+=1
        else:
            indeg[t]+=1
queue=deque(s for s in indeg if indeg[s]==0)
visited=0
while queue:
    s=queue.popleft();visited+=1
    if s in up:
        t=up[s];indeg[t]-=1
        if indeg[t]==0:queue.append(t)
    for t,_ in facets(s):
        if t and t!=down.get(s):
            indeg[t]-=1
            if indeg[t]==0:queue.append(t)
assert visited==len(F)-1,(visited,len(F)-1)
assert incidence_count==sum(d*n for d,n in fc.items() if d>=2)
print('VERIFY_OK oriented_Hasse_DAG=%d incidence_count=%d'%(visited,incidence_count),flush=True)

# Exact signed Morse differential from critical five-cells to critical four-cells.
C4=sorted(s for s in critical if s.bit_count()==5)
C5=sorted(s for s in critical if s.bit_count()==6)
i4={s:i for i,s in enumerate(C4)}
@lru_cache(None)
def project4(s):
    if s in i4:return {i4[s]:1}
    if s in down:return {}
    t=up[s]
    incidence=next(a for f,a in facets(t) if f==s)
    result=defaultdict(int)
    for f,a in facets(t):
        if f==s:continue
        for i,c in project4(f).items():result[i]-=incidence*a*c
    return {i:c for i,c in result.items() if c}
A=zeros(len(C4),len(C5))
for j,t in enumerate(C5):
    for f,a in facets(t):
        for i,c in project4(f).items(): A[i,j]+=a*c
assert A.shape==(24,27)
D=smith_normal_form(A,domain=ZZ)
invariants=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
assert invariants==[1]*21,invariants
# A 21-by-21 maximal minor of determinant -1 separately witnesses no torsion.
cols=list(A.rref()[1])
rows=list(A[:,cols].T.rref()[1])
assert len(rows)==len(cols)==21
minor=int(A.extract(rows,cols).det())
assert minor==-1,minor
assert sum(1 for x in A if x)!=0
assert len(C4)-len(invariants)==3 and len(C5)-len(invariants)==6
# Independent reduced Euler-characteristic cross-check.
reduced_euler=sum((-1)**(d-1)*fc[d] for d in fc) # d=0 contributes -1
assert reduced_euler==(-1)**4*3+(-1)**5*6==-3
print('VERIFY_OK Morse_boundary=24x27 rank=21 Smith_nonunits=none unimodular_minor=-1')
print('VERIFY_OK reduced_H4=Z^3 reduced_H5=Z^6 wedge=3S4+6S5 reduced_euler=-3')
print('ALL_VERIFY_OK')
