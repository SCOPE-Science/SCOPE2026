#!/usr/bin/env python3
"""Exact integral certificate for the transpose quotient of the 5x5 chessboard complex.
Run with Python 3 standard library only. All data are regenerated, no cached inputs.
"""
import itertools, collections, heapq, hashlib, json
N = 5
D = 4
faces = set()
for k in range(1, N + 1):
    for rr in itertools.combinations(range(N), k):
        for cc in itertools.permutations(range(N), k):
            faces.add(sum(1 << (N*r+c) for r, c in zip(rr,cc)))
assert len(faces) == 1545
assert [sum(f.bit_count() == d+1 for f in faces) for d in range(5)] == [25,200,600,600,120]
perm = [N*(j%N) + j//N for j in range(N*N)]
def transpose(mask):
    ans=0
    while mask:
        b=mask & -mask; mask-=b
        ans |= 1 << perm[b.bit_length()-1]
    return ans
trans = {f: transpose(f) for f in faces}
assert all(trans[trans[f]] == f for f in faces)

# The orbit of a strict face flag is a regular cell of the quotient of the
# barycentric subdivision. The group preserves the flag's increasing ranks.
chains=[[] for _ in range(D+1)]
index=[{} for _ in range(D+1)]
by_top={}
full_counts=[0]*(D+1)
fixed_counts=[0]*(D+1)
for f in sorted(faces, key=lambda x:(x.bit_count(),x)):
    part=[(f,)]
    sub=(f-1)&f
    while sub:
        part.extend(ch+(f,) for ch in by_top[sub]);sub=(sub-1)&f
    by_top[f]=part
    for ch in part:
        d=len(ch)-1
        full_counts[d]+=1
        t=tuple(trans[x] for x in ch)
        if t==ch: fixed_counts[d]+=1
        key=min(ch,t)
        if key not in index[d]:
            index[d][key]=len(chains[d]);chains[d].append(key)
assert [len(z) for z in chains] == [843,8340,22110,21900,7260]
assert [len(z) for z in chains] == [(u+v)//2 for u,v in zip(full_counts,fixed_counts)]
assert sum((-1)**d*len(chains[d]) for d in range(D+1)) == -27

# Oriented quotient boundary. Deleting flag vertex j has coefficient (-1)^j.
bdry=[None]
for d in range(1,D+1):
    vals=[]
    for ch in chains[d]:
        vals.append(tuple(index[d-1][min(ch[:j]+ch[j+1:],tuple(trans[x] for x in ch[:j]+ch[j+1:]))] for j in range(d+1)))
    bdry.append(vals)
# Verify the simplicial equation boundary squared = 0 on every cell.
for d in range(2,D+1):
    for bb in bdry[d]:
        coeff=collections.defaultdict(int)
        for j,lower in enumerate(bb):
            for k,twolower in enumerate(bdry[d-1][lower]):
                coeff[twolower]+=(-1)**(j+k)
        assert all(v==0 for v in coeff.values())

# Genuine elementary collapses, ordered by decreasing upper dimension.
alive=[bytearray(b'\x01')*len(ch) for ch in chains]
cofaces=[None]+[[set() for _ in chains[d-1]] for d in range(1,D+1)]
for d in range(1,D+1):
    for u,bb in enumerate(bdry[d]):
        for lower in bb:
            cofaces[d][lower].add(u)
topological=[0]*(D+1)
for d in range(D,0,-1):
    queue=collections.deque(i for i,x in enumerate(cofaces[d]) if len(x)==1)
    while queue:
        l=queue.pop()
        if not alive[d-1][l] or len(cofaces[d][l])!=1: continue
        u=next(iter(cofaces[d][l]))
        if not alive[d][u]: continue
        assert l in bdry[d][u]
        alive[d-1][l]=0;alive[d][u]=0
        topological[d]+=1
        for f in bdry[d][u]:
            cf=cofaces[d][f]
            cf.remove(u)
            if len(cf)==1: queue.append(f)
        if d>1:
            for f in bdry[d-1][l]: cofaces[d-1][f].remove(l)
assert topological == [0,173,2919,9156,7260], topological
assert [sum(v) for v in alive] == [670,5248,10035,5484,0]

# Exact integral cancellation over Z, only unit pivots. This determines the
# Smith data of the cellular chain complex, not a topological collapse.
columns=[None]+[{} for _ in range(D)]
rows=[None]+[{} for _ in range(D)]
for d in range(1,D+1):
    for u,bb in enumerate(bdry[d]):
        if not alive[d][u]:continue
        col={l:(-1 if j%2 else 1) for j,l in enumerate(bb) if alive[d-1][l]}
        columns[d][u]=col
        for l,v in col.items(): rows[d].setdefault(l,{})[u]=v
assert all(len(z)==0 for z in columns[D].values())
algebraic=[0]*(D+1)
for d in (3,2,1):
    C,R=columns[d],rows[d]
    heap=[]
    for u,col in C.items():
        for l,v in col.items():
            if abs(v)==1: heapq.heappush(heap,(len(col)*len(R[l]),l,u))
    while heap:
        heuristic,l,u=heapq.heappop(heap)
        if u not in C or l not in R or l not in C[u] or abs(C[u][l])!=1:continue
        score=len(C[u])*len(R[l])
        if score>2*heuristic and score>20:
            heapq.heappush(heap,(score,l,u));continue
        pivot=C[u][l]
        assert pivot in (1,-1)
        pivot_col=C[u].copy()
        row=R[l].copy()
        for w,a in row.items():
            if w==u:continue
            factor=a//pivot
            col=C[w]
            for i,b in pivot_col.items():
                old=col.get(i,0)
                new=old-factor*b
                if new:
                    col[i]=new;R[i][w]=new
                    if abs(new)==1:
                        heapq.heappush(heap,(len(col)*len(R[i]),i,w))
                elif old:
                    del col[i]; del R[i][w]
            assert l not in col
        del C[u]
        for i in pivot_col:
            R[i].pop(u)
            if not R[i]: del R[i]
        assert l not in R
        if d>=2:
            removed_lower=columns[d-1].pop(l,None)
            if removed_lower is not None:
                for i in removed_lower:
                    rows[d-1][i].pop(l)
                    if not rows[d-1][i]:del rows[d-1][i]
        if d<D:
            removed_upper=rows[d+1].pop(u,None)
            if removed_upper is not None:
                for z in removed_upper:
                    columns[d+1][z].pop(u)
        alive[d][u]=0;alive[d-1][l]=0
        algebraic[d]+=1
assert algebraic == [0,669,4579,5456,0], algebraic
assert [sum(v) for v in alive]==[1,0,0,28,0]
assert all(not col for d in range(1,D+1) for col in columns[d].values())
print('CHESSBOARD_TRANSPOSE_INTEGRAL_HOMOTOPY_OK')
print('original_faces=1545; quotient_flags=' + str([len(c) for c in chains]))
print('full_flags='+str(full_counts)+'; fixed_flags='+str(fixed_counts))
print('topological_collapses='+str(topological)+'; residual_cells='+str([670,5248,10035,5484,0]))
print('unit_pivot_cancellations='+str(algebraic)+'; final_chain_ranks=[1,0,0,28,0]')
