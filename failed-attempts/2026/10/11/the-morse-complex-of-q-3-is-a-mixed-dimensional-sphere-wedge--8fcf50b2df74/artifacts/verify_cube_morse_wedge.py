#!/usr/bin/env python3
from itertools import product
from collections import defaultdict, deque
from fractions import Fraction

# Q_3 on integers 0,...,7, adjacent when binary XOR has one bit.
V = list(range(8))
E = []
for u in V:
    for bit in (1,2,4):
        v = u ^ bit
        if u < v:
            E.append((u,v))
E.sort()
assert len(E) == 12

# Primitive discrete vector fields: (tail vertex, undirected edge index).
# They encode directed edges tail -> the other endpoint.
P = []
for ei,(u,v) in enumerate(E):
    P.append((u,ei))
    P.append((v,ei))
assert len(P) == 24

head = {}
for pi,(tail,ei) in enumerate(P):
    u,v = E[ei]
    head[pi] = v if tail == u else u

# A graph discrete vector field is a partial orientation with no repeated tail,
# no repeated undirected edge, and no directed cycle.
def valid(face):
    tails=set(); edges=set(); nxt={}
    for pi in face:
        t,ei=P[pi]
        if t in tails or ei in edges:
            return False
        tails.add(t); edges.add(ei); nxt[t]=head[pi]
    # Since every tail has outdegree <=1, detect directed cycles directly.
    for s in list(nxt):
        seen=set(); x=s
        while x in nxt:
            if x in seen:
                return False
            seen.add(x); x=nxt[x]
    return True

# Exhaustive 3^12 edge-state enumeration: absent, u->v, v->u.
faces=set()
for states in product((0,1,2), repeat=12):
    f=[]; tails=set(); ok=True
    for ei,st in enumerate(states):
        if st==0: continue
        pi=2*ei+(st-1)
        t,_=P[pi]
        if t in tails:
            ok=False; break
        tails.add(t); f.append(pi)
    if ok and valid(f):
        faces.add(tuple(f))
assert () in faces
nonempty=sorted((f for f in faces if f), key=lambda x:(len(x),x))
assert len(nonempty)==23624
fvec=tuple(sum(1 for f in nonempty if len(f)==k+1) for k in range(7))
EXPECTED_F=(24,240,1296,4080,7488,7424,3072)
assert fvec==EXPECTED_F,(fvec,EXPECTED_F)

# Independent rooted-forest face count via all subsets of graph edges and roots.
# A forest with components of sizes s_i supports product(s_i) orientations toward
# a chosen root in each component, and has one primitive for each forest edge.
rooted_counts=[0]*8
for mask in range(1<<len(E)):
    parent=list(range(8))
    def find(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]; a=parent[a]
        return a
    def union(a,b):
        a,b=find(a),find(b)
        if a==b: return False
        parent[b]=a; return True
    m=0; ok=True
    for ei,(u,v) in enumerate(E):
        if mask>>ei&1:
            m+=1
            if not union(u,v): ok=False; break
    if not ok: continue
    comps=defaultdict(int)
    for v in V: comps[find(v)]+=1
    ways=1
    for s in comps.values(): ways*=s
    rooted_counts[m]+=ways
assert tuple(rooted_counts[:7])==(1,)+EXPECTED_F[:6]
# Seven oriented forest edges would require a spanning tree and gives 3072.
assert rooted_counts[7]==3072

# Sequential element-toggle matching on nonempty face poset.
face_set=set(nonempty)
unmatched=set(nonempty)
matched_up={}   # lower -> upper
matched_down={} # upper -> lower
for p in range(24):
    for f in sorted(list(unmatched), key=lambda x:(len(x),x)):
        if f not in unmatched or p in f:
            continue
        g=tuple(sorted(f+(p,)))
        if g in unmatched:
            matched_up[f]=g; matched_down[g]=f
            unmatched.remove(f); unmatched.remove(g)
critical=sorted(unmatched,key=lambda x:(len(x),x))
crit_counts=defaultdict(int)
for f in critical: crit_counts[len(f)-1]+=1
EXPECTED_CRIT={0:1,5:44,6:179}
assert dict(crit_counts)==EXPECTED_CRIT,dict(crit_counts)
assert len(matched_up)==11700

# Full Hasse-orientation acyclicity check for the matching.
id_of={f:i for i,f in enumerate(nonempty)}
adj=[[] for _ in nonempty]
indeg=[0]*len(nonempty)
for upper in nonempty:
    if len(upper)==1: continue
    ui=id_of[upper]
    for j in range(len(upper)):
        lower=upper[:j]+upper[j+1:]
        li=id_of[lower]
        if matched_up.get(lower)==upper:
            a,b=li,ui  # matched cover reversed: lower -> upper
        else:
            a,b=ui,li  # unmatched cover: upper -> lower
        adj[a].append(b); indeg[b]+=1
q=deque(i for i,d in enumerate(indeg) if d==0)
seen=0
while q:
    x=q.popleft(); seen+=1
    for y in adj[x]:
        indeg[y]-=1
        if indeg[y]==0:q.append(y)
assert seen==len(nonempty), (seen,len(nonempty))

# Oriented simplicial incidence coefficient [lower:upper].
def incidence(lower, upper):
    # tuples are sorted vertex labels. lower must be a codim-1 face.
    i=j=0
    while i<len(upper):
        if j>=len(lower) or upper[i]!=lower[j]:
            return -1 if i%2 else 1
        i+=1; j+=1
    raise AssertionError('not a facet')

critical5=sorted([f for f in critical if len(f)==6])
critical6=sorted([f for f in critical if len(f)==7])
row_index={f:i for i,f in enumerate(critical5)}

# Algebraic Morse projection of a 5-cell onto critical 5-cells.
from functools import lru_cache
@lru_cache(None)
def project5(cell):
    if cell in row_index:
        return {row_index[cell]:1}
    if cell in matched_down:
        # An upper member of a matched pair is eliminated.
        return {}
    up=matched_up.get(cell)
    assert up is not None, ('unclassified cell',cell)
    c=incidence(cell,up)
    out={}
    for j in range(len(up)):
        other=up[:j]+up[j+1:]
        if other==cell: continue
        d=-incidence(other,up)*c  # c^{-1}=c for c=±1
        for r,a in project5(other).items():
            out[r]=out.get(r,0)+d*a
            if out[r]==0: del out[r]
    return out

# Morse boundary C_6^M -> C_5^M, matrix 44 x 179.
M=[[0]*len(critical6) for _ in critical5]
for col,cell in enumerate(critical6):
    total={}
    for j in range(len(cell)):
        lower=cell[:j]+cell[j+1:]
        s=-1 if j%2 else 1
        for r,a in project5(lower).items():
            total[r]=total.get(r,0)+s*a
            if total[r]==0: del total[r]
    for r,a in total.items(): M[r][col]=a
nnz=sum(a!=0 for row in M for a in row)
maxabs=max(abs(a) for row in M for a in row)
assert nnz==195,(nnz,maxabs)
assert maxabs==1

# Exact rational rank.
def rank_Q(A):
    A=[[Fraction(x) for x in row] for row in A]
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        v=A[r][c]
        A[r]=[x/v for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r
assert rank_Q(M)==40

# Exact rank modulo p, used also as a coefficient-field check.
def rank_mod(A,p):
    rows=[{j:(x%p) for j,x in enumerate(row) if x%p} for row in A]
    r=0; piv={}
    for row in rows:
        v=dict(row)
        while v:
            c=min(v)
            if c not in piv:
                inv=pow(v[c],-1,p)
                v={j:(x*inv)%p for j,x in v.items() if (x*inv)%p}
                piv[c]=v; r+=1; break
            f=v[c]
            for j,x in piv[c].items():
                y=(v.get(j,0)-f*x)%p
                if y:v[j]=y
                else:v.pop(j,None)
    return r
assert rank_mod(M,2)==40 and rank_mod(M,3)==40

# Certificate of a unimodular 40x40 minor. A determinant ±1 proves that all
# nonzero Smith invariant factors of the rank-40 integer matrix are units.
PIVCOL=(0,1,3,4,5,6,7,8,9,10,11,12,13,26,27,28,29,30,32,34,36,53,54,55,57,79,80,81,82,87,88,89,90,92,95,96,97,98,99,101)
PIVROW=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43)
minor=[[M[i][j] for j in PIVCOL] for i in PIVROW]

def det_bareiss(A):
    A=[row[:] for row in A]
    n=len(A); sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            s=next((i for i in range(k+1,n) if A[i][k]),None)
            assert s is not None
            A[k],A[s]=A[s],A[k]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num%prev==0
                A[i][j]=num//prev
        prev=pivot
        for i in range(k+1,n): A[i][k]=0
        for j in range(k+1,n): A[k][j]=0
    return sign*A[-1][-1]
det=det_bareiss(minor)
assert abs(det)==1,det

# Consequences of the Morse CW chain complex: 1 critical 0-cell, 44 critical
# 5-cells, 179 critical 6-cells, rank-40 unit Smith boundary.
assert 44-40==4 and 179-40==139
print('CUBE_MORSE_WEDGE_VERIFY_OK')
print('faces',len(nonempty),'f_vector',fvec)
print('matching_pairs',len(matched_up),'critical',dict(crit_counts))
print('morse_boundary','shape',(44,179),'nnz',nnz,'rank_Q',40,'unit_minor_det',det)
print('wedge','4*S^5 + 139*S^6')
