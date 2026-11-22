#!/usr/bin/env python3
"""Exact finite checker for the icosahedral two-independence symmetry quotient.

Uses Python's standard library. Integer row and column operations are unimodular.
"""
from itertools import combinations
from collections import Counter

# The icosahedral graph is specified here, not imported from a graph library.
ADJ = (
    (1, 5, 7, 8, 11),
    (0, 2, 5, 6, 8),
    (1, 3, 6, 8, 9),
    (2, 4, 6, 9, 10),
    (3, 5, 6, 10, 11),
    (0, 1, 4, 6, 11),
    (1, 2, 3, 4, 5),
    (0, 8, 9, 10, 11),
    (0, 1, 2, 7, 9),
    (2, 3, 7, 8, 10),
    (3, 4, 7, 9, 11),
    (0, 4, 5, 7, 10),
)
N = 12
assert len(ADJ)==N
EDGES = frozenset((min(i,j),max(i,j)) for i in range(N) for j in ADJ[i])
assert len(EDGES)==30 and all(len(ADJ[i])==5 for i in range(N))
assert all(i in ADJ[j] for i in range(N) for j in ADJ[i])
A = tuple(sum(1<<j for j in ADJ[i]) for i in range(N))

def valid(mask):
    return all((A[i]&mask).bit_count()<=1 for i in range(N) if mask&(1<<i))

# A second independent face predicate uses the forbidden connected triples.
forbidden = frozenset(
    (1<<i)|(1<<j)|(1<<k)
    for i,j,k in combinations(range(N),3)
    if sum((u,v) in EDGES for u,v in ((i,j),(i,k),(j,k)))>=2
)
assert len(forbidden)==80
for m in range(1<<N):
    assert valid(m)==all((m&t)!=t for t in forbidden)
FACES = tuple(m for m in range(1,1<<N) if valid(m))
assert len(FACES)==323
assert Counter(m.bit_count() for m in FACES)=={1:12,2:66,3:140,4:105}

# Two independently checkable vertex-fixed graph automorphisms.
X = (0, 1, 6, 3, 9, 8, 2, 11, 5, 4, 10, 7)
Y = (1, 2, 9, 10, 4, 6, 3, 0, 8, 7, 11, 5)
IDENTITY=tuple(range(N))

def compose(p,q):
    return tuple(p[q[i]] for i in range(N))

def perm_ok(p):
    return sorted(p)==list(range(N)) and {tuple(sorted((p[i],p[j]))) for i,j in EDGES}==EDGES
assert perm_ok(X) and perm_ok(Y)
assert X[0]==0 and Y[4]==4
GROUP={IDENTITY}
queue=[IDENTITY]
while queue:
    p=queue.pop()
    for g in (X,Y):
        q=compose(p,g)
        if q not in GROUP:
            GROUP.add(q);queue.append(q)
GROUP=tuple(sorted(GROUP))
assert len(GROUP)==120
assert all(perm_ok(p) for p in GROUP)
# For a fixed vertex its five neighbors are a pentagon. Thus the full
# automorphism group has size at most 12 * 5 * 2 = 120.
for v in range(N):
    ne=ADJ[v]
    assert all(sum((min(i,j),max(i,j)) in EDGES for j in ne if i!=j)==2 for i in ne)

# Show the original complex is simply connected, using the complete
# 1-skeleton and the triangle relations. A star spanning tree based at 0
# yields one generator for each edge among 1,...,11.
TRI=frozenset(tuple(i for i in range(N) if m&(1<<i)) for m in FACES if m.bit_count()==3)
unknown=set(combinations(range(1,N),2))
removed_rounds=[]
while unknown:
    removed=set()
    for a,b in sorted(unknown):
        if (0,a,b) in TRI:
            removed.add((a,b));continue
        if any(tuple(sorted((a,b,c))) in TRI
               and tuple(sorted((a,c))) not in unknown
               and tuple(sorted((b,c))) not in unknown
               for c in range(1,N) if c not in (a,b)):
            removed.add((a,b))
    if not removed:
        raise AssertionError('nontrivial generator not eliminated')
    unknown-=removed
    removed_rounds.append(len(removed))
assert removed_rounds==[35,20]
# Armstrong's orbit-space pi_1 formula now applies. The two fixed-vertex
# automorphisms generate the full group, so the quotient pi_1 is trivial.

# All nonempty strictly increasing chains of faces in the face poset.
sub={f:[s for s in FACES if s!=f and (s&f)==s] for f in FACES}
flags=set()
for f in FACES:
    stack=[(f,)]
    while stack:
        flag=stack.pop();flags.add(flag)
        stack.extend((s,)+flag for s in sub[flag[0]])
assert len(flags)==9905

def move(mask,p):
    out=0
    while mask:
        b=mask & -mask
        i=b.bit_length()-1
        out|=1<<p[i]
        mask^=b
    return out

transport={f:tuple(move(f,p) for p in GROUP) for f in FACES}
lookup={}
ORBIT_FLAGS=[]
for flag in sorted(flags,key=lambda z:(len(z),z)):
    if flag in lookup:continue
    k=len(ORBIT_FLAGS);ORBIT_FLAGS.append(flag)
    for t in range(len(GROUP)):
        img=tuple(transport[f][t] for f in flag)
        if img in lookup:assert lookup[img]==k
        else: lookup[img]=k
assert len(lookup)==len(flags)
assert len(ORBIT_FLAGS)==118
assert Counter(len(z)-1 for z in ORBIT_FLAGS)=={0:10,1:35,2:49,3:24}
FACES_OF={i:tuple(lookup[flag[:j]+flag[j+1:]] for j in range(len(flag)))
          for i,flag in enumerate(ORBIT_FLAGS) if len(flag)>1}

# Rank and Smith diagonal using integer unimodular operations ONLY.
# If all nonzero invariant factors are 1, a unit-pivot elimination yields
# a diagonal of ones followed by a zero block.
def unit_pivot_smith(M):
    if not M:return 0
    m=len(M);n=len(M[0]);A=[list(map(int,row)) for row in M]
    k=0
    while k<min(m,n):
        pivot=next(((i,j) for i in range(k,m) for j in range(k,n)
                    if abs(A[i][j])==1),None)
        if pivot is None:
            assert all(A[i][j]==0 for i in range(k,m) for j in range(k,n)), \
                'nonunit elementary divisor: cannot certify all Smith factors 1'
            break
        i,j=pivot
        A[k],A[i]=A[i],A[k]
        for r in range(m):A[r][k],A[r][j]=A[r][j],A[r][k]
        assert abs(A[k][k])==1
        if A[k][k]==-1:A[k]=[-x for x in A[k]]
        for r in range(k+1,m):
            t=A[r][k]
            if t:A[r]=[a-t*b for a,b in zip(A[r],A[k])]
        for c in range(k+1,n):
            t=A[k][c]
            if t:
                for r in range(m):A[r][c]-=t*A[r][k]
        assert A[k][k]==1
        assert all(A[r][k]==0 for r in range(m) if r!=k)
        assert all(A[k][c]==0 for c in range(n) if c!=k)
        k+=1
    assert all(A[r][c]==(1 if r==c and r<k else 0)
               for r in range(m) for c in range(n))
    return k

indices={d:[i for i,flag in enumerate(ORBIT_FLAGS) if len(flag)==d+1] for d in range(4)}
boundaries={}
for d in range(1,4):
    pos={cid:r for r,cid in enumerate(indices[d-1])}
    M=[[0 for c in indices[d]] for r in indices[d-1]]
    for c,cid in enumerate(indices[d]):
        for j,fid in enumerate(FACES_OF[cid]):
            M[pos[fid]][c]+=(-1)**j
    boundaries[d]=M
    assert max(abs(a) for row in M for a in row)<=1
for d in (2,3):
    L=boundaries[d-1]; R=boundaries[d]
    assert all(sum(L[i][k]*R[k][j] for k in range(len(R)))==0
               for i in range(len(L)) for j in range(len(R[0])))
rank={d:unit_pivot_smith(boundaries[d]) for d in (1,2,3)}
assert rank=={1:9,2:26,3:23}
# 0: Z; 1 and 2: zero; 3: Z, with NO integral torsion.
assert len(indices[0])-rank[1]==1
assert len(indices[1])-rank[1]-rank[2]==0
assert len(indices[2])-rank[2]-rank[3]==0
assert len(indices[3])-rank[3]==1
print('ICOSAHEDRAL_TWO_INDEPENDENCE_FULL_QUOTIENT_S3_OK')
print('faces=323 automorphisms=120 flags=9905 quotient_cells=10,35,49,24')
print('integer_smith_unit_ranks=9,26,23 pi1=trivial H3=Z')
