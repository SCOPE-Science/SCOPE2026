#!/usr/bin/env python3
"""Exact self-contained face, discrete-Morse, signed boundary, dihedral character for five-vertex bidirected wheel."""
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from itertools import permutations

N=4
EDGES=sorted({tuple(sorted((i,(i+1)%4))) for i in range(4)} | {(4,i) for i in range(4)})
ARCS=sorted([(u,v) for u,v in EDGES]+[(v,u) for u,v in EDGES]); M=len(ARCS)
ORDER=[10,8,12,0,1,13,3,14,7,11,4,6,5,15,9,2]

def valid(s):
    ins=set();out=set();nxt={}
    for j,(u,v) in enumerate(ARCS):
        if s>>j&1:
            if u in out or v in ins: return False
            ins.add(v);out.add(u);nxt[u]=v
    for u in nxt:
        seen=set();cur=u
        while cur in nxt:
            if cur in seen:return False
            seen.add(cur);cur=nxt[cur]
    return True

F=sorted([s for s in range(1,1<<M) if valid(s)])
assert len(F)==260
assert Counter(s.bit_count()-1 for s in F)=={0:16,1:76,2:120,3:48}
S=set(F);unmatched=S.copy();pairs=[]
for v in ORDER:
    b=1<<v
    for a in sorted((s for s in unmatched if not s&b),key=lambda s:(s.bit_count(),s)):
        if a in unmatched and a|b in unmatched:
            unmatched.remove(a);unmatched.remove(a|b);pairs.append((a,a|b))
assert len(pairs)==116
assert Counter(x.bit_count()-1 for x in unmatched)=={0:1,2:19,3:8}
low_to_high=dict(pairs)
upper=set(low_to_high.values())

# Full directed face-incidence graph, down except reversed matched edges.
inc=0; adj={s:[] for s in F}; indeg={s:0 for s in F}
for s in F:
    for j in range(M):
        if s>>j&1:
            t=s^(1<<j)
            if not t:continue
            inc+=1
            if low_to_high.get(t)==s: a,b=t,s
            else:a,b=s,t
            adj[a].append(b);indeg[b]+=1
Q=[s for s in F if indeg[s]==0];visited=0
while Q:
    a=Q.pop();visited+=1
    for b in adj[a]:
        indeg[b]-=1
        if indeg[b]==0:Q.append(b)
assert visited==260

@lru_cache(None)
def boundary(s):
    xs=[j for j in range(M) if s>>j&1]
    return {s^(1<<j):(-1)**k for k,j in enumerate(xs)}

def add(dst, src, mult=1):
    for a,c in src.items():
        z=dst.get(a,0)+mult*c
        if z:dst[a]=z
        elif a in dst:del dst[a]

@lru_cache(None)
def project(s):
    if not s: return {}
    if s in unmatched:return {s:1}
    if s in upper:return {}
    h=low_to_high[s]; u=boundary(h)[s]
    z={}
    for t,c in boundary(h).items():
        if t!=s:
            add(z,project(t),-c*u)
    return z

crit3=sorted([s for s in unmatched if s.bit_count()==4]);crit2=sorted([s for s in unmatched if s.bit_count()==3]);crit0=sorted([s for s in unmatched if s.bit_count()==1]);
MORSE={s:{} for s in crit3}
for s in crit3:
    z={}
    for t,c in boundary(s).items():add(z,project(t),c)
    MORSE[s]=z
assert all(not z for z in MORSE.values()),MORSE
# Topological wedge: single critical zero-cell, no 1-cells, 19 2-cells and 8 3-cells, all degree maps vanish.

# Symmetries of a square on rim 0,1,2,3, hub 4.
arc_index={a:i for i,a in enumerate(ARCS)}

def acts(p,s):
    idx=[arc_index[(p[u],p[v])] for j,(u,v) in enumerate(ARCS) if s>>j&1]
    z=sum(1<<j for j in idx)
    inversions=sum(idx[i]>idx[j] for i in range(len(idx)) for j in range(i+1,len(idx)))
    # Need sign in canonical ordering. Original source arcs already sorted by index.
    return z,(-1)**inversions

def lef(p):
    return sum((-1)**(s.bit_count()-1)*acts(p,s)[1] for s in F if acts(p,s)[0]==s)-1

# Need H3 basis exact nullspace of signed d3 matrix (∂_3: C3 -> C2).
F3=sorted([s for s in F if s.bit_count()==4]);F2=sorted([s for s in F if s.bit_count()==3]);row={s:i for i,s in enumerate(F2)}
D=[[Fraction(0) for _ in F3] for _ in F2]
for j,s in enumerate(F3):
    for t,c in boundary(s).items(): D[row[t]][j]=Fraction(c)
piv=[];rr=0
for j in range(len(F3)):
    rowpivot=next((q for q in range(rr,len(F2)) if D[q][j]),None)
    if rowpivot is None: continue
    D[rr],D[rowpivot]=D[rowpivot],D[rr]
    val=D[rr][j]
    D[rr]=[x/val for x in D[rr]]
    for q in range(len(F2)):
        if q!=rr and D[q][j]:
            val=D[q][j]; D[q]=[a-val*b for a,b in zip(D[q],D[rr])]
    piv.append(j);rr+=1
free=[j for j in range(len(F3)) if j not in piv]
assert len(free)==8
basis=[]
for j in free:
    v=[Fraction(int(q==j)) for q in range(len(F3))]
    for i,p in enumerate(piv):v[p]=-D[i][j]
    basis.append(v)
assert all(basis[j][free[i]]==(1 if i==j else 0) for j in range(8) for i in range(8))
F3_index={s:i for i,s in enumerate(F3)}

def top_trace(p):
    trace=0
    for i,v in enumerate(basis):
        chosen=F3[free[i]]
        pre=0
        for s in F3:
            image,sgn=acts(p,s)
            if image==chosen:pre+=sgn*v[F3_index[s]]
        trace+=pre
    assert trace.denominator==1,trace
    return int(trace)

for kind in ('r','s'):
    for k in range(4):
        p=tuple((((i+k)%4 if kind=='r' else (k-i)%4) for i in range(4)))+(4,)
        l=lef(p);h3=top_trace(p);h2=l+h3
        print('SYM',kind,k,'TRACE_H2',h2,'TRACE_H3',h3,'LEFSCHETZ',l)

# Character orthogonality in class order identity, half turn, quarter turns,
# vertex-axis reflections, edge-axis reflections, with class sizes 1,1,2,2,2.
chars2=[19,3,-1,1,1]
chars3=[8,0,0,0,0]
irreps={'A1':[1,1,1,1,1], 'A2':[1,1,1,-1,-1],
        'B1':[1,1,-1,1,-1], 'B2':[1,1,-1,-1,1],
        'E':[2,-2,0,0,0]}
class_sizes=[1,1,2,2,2]
def decompose(c):
    return {k:sum(a*b*w for a,b,w in zip(c,ch,class_sizes))//8
            for k,ch in irreps.items()}
assert decompose(chars2)=={'A1':3,'A2':2,'B1':3,'B2':3,'E':4}
assert decompose(chars3)=={'A1':1,'A2':1,'B1':1,'B2':1,'E':2}
print('D4_H2',decompose(chars2),'D4_H3',decompose(chars3))

# Independent mod-two ranks from full simplicial boundaries.
rank2={}
for dim in (1,2,3):
    cols=[s for s in F if s.bit_count()==dim+1]
    lower={s:i for i,s in enumerate(x for x in F if x.bit_count()==dim)}
    pivots={}
    for s in cols:
        col=0
        for t in boundary(s):col^=1<<lower[t]
        while col:
            bit=col.bit_length()-1
            if bit in pivots:col^=pivots[bit]
            else:pivots[bit]=col;break
    rank2[dim]=len(pivots)
assert rank2=={1:15,2:61,3:40}
print('MOD2_BOUNDARY_RANKS',rank2)
print('WHEEL_MULTIPATH_EXACT_PASS', 'faces',len(F),'incidences',inc,'matching',len(pairs),'critical',dict(Counter(s.bit_count()-1 for s in unmatched)),'morse3to2', 'zero')
