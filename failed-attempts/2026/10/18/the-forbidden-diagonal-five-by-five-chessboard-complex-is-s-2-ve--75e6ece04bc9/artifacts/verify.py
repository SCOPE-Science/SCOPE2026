#!/usr/bin/env python3
"""Exact finite certificate for the five-by-five off-diagonal rook complex.
Only Python standard library required. The complex uses square indices in row-major order.
"""
import itertools, collections, json
from fractions import Fraction
N=5
SQUARES=[(i,j) for i in range(N) for j in range(N) if i!=j]
EDGE_INDEX={a:k for k,a in enumerate(SQUARES)}
TOGGLES=[(2,4),(0,2),(3,1),(1,3),(4,0),(4,3),(2,0),(3,4),(4,2),(2,1),(0,4),(1,0),(3,2),(3,0),(1,2),(2,3),(4,1),(0,3),(1,4),(0,1)]
assert sorted(TOGGLES)==sorted(SQUARES)

def enum_permutations():
    faces={0}
    for k in range(1,N+1):
        for rr in itertools.combinations(range(N),k):
            for cc in itertools.permutations(range(N),k):
                if all(r!=c for r,c in zip(rr,cc)):
                    faces.add(sum(1<<EDGE_INDEX[r,c] for r,c in zip(rr,cc)))
    return faces

def enum_recursive():
    faces=set()
    def go(row,mask,used_cols):
        if row==N:
            faces.add(mask)
            return
        go(row+1,mask,used_cols)
        for col in range(N):
            if col!=row and not(used_cols>>col&1):
                go(row+1,mask|(1<<EDGE_INDEX[row,col]),used_cols|(1<<col))
    go(0,0,0)
    return faces

F=enum_permutations()
assert F==enum_recursive()
assert len(F)==780
by={k:sorted(f for f in F if f.bit_count()==k+1) for k in range(-1,N)}
fvec=[len(by[k]) for k in range(N)]
assert fvec==[20,130,320,265,44],fvec
for f in F:
    for j in range(len(SQUARES)):
        if f>>j&1:assert (f^(1<<j)) in F

UNMATCHED=set(F)-{0}
PAIRS=[]
ALL=sorted(UNMATCHED)
for row,col in TOGGLES:
    b=1<<EDGE_INDEX[row,col]
    for f in ALL:
        if f not in UNMATCHED or f&b:continue
        hi=f|b
        if hi in UNMATCHED:
            UNMATCHED.remove(f);UNMATCHED.remove(hi)
            PAIRS.append((f,hi))
assert len(PAIRS)==382,len(PAIRS)
critical=collections.Counter(f.bit_count()-1 for f in UNMATCHED)
assert dict(critical)=={0:1,2:1,3:13},critical
assert len(UNMATCHED)+2*len(PAIRS)==len(F)-1

# Check acyclicity of the entire reversed-matching face-poset digraph.
P=set(PAIRS)
indeg={s:0 for s in ALL}
out={s:[] for s in ALL}
edge_count=0
for hi in ALL:
    x=hi
    while x:
        t=x&-x;x-=t
        lo=hi^t
        if lo==0:continue
        if (lo,hi) in P:src,dst=lo,hi
        else:src,dst=hi,lo
        out[src].append(dst)
        indeg[dst]+=1
        edge_count+=1
assert edge_count==2500,edge_count
Q=collections.deque([s for s in ALL if indeg[s]==0]);visited=0
while Q:
    x=Q.popleft();visited+=1
    for y in out[x]:
        indeg[y]-=1
        if indeg[y]==0:Q.append(y)
assert visited==len(ALL),(visited,len(ALL))

# Independent exact rank computation over Q, using sparse Fraction row pivots.
idx={k:{f:i for i,f in enumerate(by[k])} for k in range(N)}
def bdry(f,k):
    x=f;r=0;a={}
    while x:
        b=x&-x;x-=b
        a[idx[k-1][f^b]]=Fraction(1 if r%2==0 else -1)
        r+=1
    return a

def rank_Q(k):
    piv={}
    for f in by[k]:
        v=bdry(f,k)
        while v:
            t=min(v)
            if t not in piv:
                inv=1/v[t]
                piv[t]={j:c*inv for j,c in v.items()}
                break
            a=v[t]
            for j,c in piv[t].items():
                w=v.get(j,0)-a*c
                if w:v[j]=w
                elif j in v:del v[j]
    return len(piv)
rank={k:rank_Q(k) for k in range(1,N)}
assert rank=={1:19,2:111,3:208,4:44},rank
betti={k:len(by[k])-rank.get(k,0)-rank.get(k+1,0) for k in range(N)}
assert betti=={0:1,1:0,2:1,3:13,4:0},betti
# The 15-critical-cell Forman CW model has only a zero-cell,
# one 2-cell and thirteen 3-cells. Its degree-3 attaching matrix
# must be zero over Q since H_3 has rank 13, hence zero over Z.
# Pi_2(S^2) = H_2(S^2;Z) then nulls every attaching map.
print('DERANGED_CROWN_5_VERIFY_OK')
print('squares=20 faces_nonempty=779 f_vector='+str(fvec))
print('matching_pairs=382 critical=(0:1,2:1,3:13) hasse_incidence=2500 acyclic=True')
print('rational_signed_boundary_ranks=(19,111,208,44) betti=(1,0,1,13,0)')
print('homotopy=S2_wedge_13_S3')
