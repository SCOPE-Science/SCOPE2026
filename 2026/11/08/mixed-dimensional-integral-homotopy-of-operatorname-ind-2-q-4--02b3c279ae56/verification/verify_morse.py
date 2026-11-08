#!/usr/bin/env python3
"""Finite discrete-Morse certificate for P3-free vertex subsets of the 4-cube.
Run: python3 q4_morse.py (Python 3.9+; standard library only).
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

N=16
adj = [sum(1 << (v ^ (1 << j)) for j in range(4)) for v in range(N)]
face=bytearray(1<<N)
face[0]=1
for s in range(1,1<<N):
    v=(s & -s).bit_length()-1
    t=s^(1<<v)
    # Each induced component is a vertex or an edge exactly when all induced degrees <=1.
    face[s]=(face[t] and (t & adj[v]).bit_count()<=1 and all((s&adj[u]).bit_count()<=1 for u in range(N) if s>>u&1))
faces=[s for s in range(1,1<<N) if face[s]]
all_faces=[0]+faces
counts=Counter(s.bit_count()-1 for s in all_faces)
assert len(all_faces)==3055
assert [counts[i] for i in range(-1,8)] == [1,16,120,464,964,960,440,80,10]
# Independent face construction: no chosen three-vertex path (two different neighbors of a centre).
paths=set()
for v in range(N):
    ns=[u for u in range(N) if adj[v]>>u&1]
    for a,b in combinations(ns,2):paths.add((1<<v)|(1<<a)|(1<<b))
assert len(paths)==N*6 # no triangle-induced duplicates in a cube
for s in range(1<<N):
    assert bool(face[s])== (not any((s&p)==p for p in paths))

# Monotone vertex-toggling Morse matching, with vertex 0 deliberately protected.
matched_down={}
used={1} # preserve one critical zero-cell
for v in range(N):
    bit=1<<v
    for s in faces:
        if s in used or s & bit:continue
        t=s|bit
        if face[t] and t not in used:
            matched_down[s]=t
            used.add(s);used.add(t)

def critical(mp):
    used=set(mp)|set(mp.values())
    return sorted(set(faces)-used, key=lambda s:(s.bit_count(),s))

def acyclic(mp):
    # All Hasse incidences included, oriented upward only along matched pairs.
    # The unique 0-dimensional cell and all other simplices are checked directly.
    indeg={s:0 for s in faces}
    outs=defaultdict(list)
    edgecount=0
    for s in faces:
        t=s
        while t:
            w=t&-t;t-=w
            r=s^w
            if r==0:continue
            if mp.get(r)==s:a,b=r,s
            else:a,b=s,r
            outs[a].append(b);indeg[b]+=1;edgecount+=1
    q=deque(s for s in faces if indeg[s]==0)
    seen=0
    while q:
        a=q.popleft();seen+=1
        for b in outs[a]:
            indeg[b]-=1
            if indeg[b]==0:q.append(b)
    return seen==len(faces),edgecount

assert len(set(matched_down.values()))==len(matched_down)
assert all((b^a).bit_count()==1 and face[b] for a,b in matched_down.items())
ok,num_edges=acyclic(matched_down)
assert ok and num_edges==13568 # nonempty poset, omit 16 singleton->empty incidences
initial_crit=critical(matched_down)
assert Counter(s.bit_count()-1 for s in initial_crit)=={0:1,3:17,4:6,5:4}

# Count all directed alternating Morse gradient paths, and find a unique path when requested.
# A path alternates critical upper U -> facet a -> its matched upper ... -> critical lower L.
def matching_paths(U,L,mp,limit=2):
    p=U.bit_count()-1
    target_lower_size=p # lower dimension p-1
    out=[]
    def dfs(upper,forbidden,path):
        if len(out)>=limit:return
        a=upper
        while a:
            bit=a&-a;a-=bit
            low=upper^bit
            if low==forbidden:continue
            if low==L:
                out.append(path+[(upper,low)])
                if len(out)>=limit:return
            elif low in mp and mp[low].bit_count()==p+1:
                dfs(mp[low],low,path+[(upper,low)])
                if len(out)>=limit:return
    dfs(U,-1,[])
    return out

# Cancel critical 5-cells against critical 4-cells, then a critical 4-cell against a 3-cell.
# Each selected path is proved unique in the current matching; after reversal recertify acyclicity.
steps=[]
for dimension in [5,5,5,5,4]:
    crit=critical(matched_down)
    ups=[s for s in crit if s.bit_count()-1==dimension]
    lows=[s for s in crit if s.bit_count()-1==dimension-1]
    found=None
    for upper in ups:
        for lower in lows:
            pp=matching_paths(upper,lower,matched_down)
            if len(pp)==1:
                found=(upper,lower,pp[0]);break
        if found:break
    assert found is not None, f'no unique gradient path in dimension {dimension}'
    U,L,path=found
    # Remove all old matches affected along the path and reverse its alternating edges.
    for u,l in path[:-1]:
        assert l in matched_down
        del matched_down[l]
    assert path[-1][1] == L
    for u,l in path:
        assert l not in matched_down
        matched_down[l]=u
    assert len(set(matched_down.values()))==len(matched_down)
    assert all((b^a).bit_count()==1 and face[b] for a,b in matched_down.items())
    ok,covers=acyclic(matched_down)
    assert ok and covers==num_edges
    steps.append((dimension, U,L, len(path)))

final=critical(matched_down)
assert Counter(s.bit_count()-1 for s in final)=={0:1,3:16,4:1}
# No 5-cells remain. Compute exact signed Morse differential of the lone 4-cell.
upper_cells=set(matched_down.values())
@lru_cache(None)
def reduce_cell(s):
    if s in upper_cells:return {}
    if s not in matched_down:return {s:1}
    u=matched_down[s];v=(u^s).bit_length()-1
    sgn=(-1)**((u&((1<<v)-1)).bit_count())
    ans=defaultdict(int)
    for j in range(N):
        if u>>j&1 and j!=v:
            facet=u^(1<<j)
            c=(-1)**((u&((1<<j)-1)).bit_count())
            for t,a in reduce_cell(facet).items():ans[t]-=sgn*c*a
    return {t:a for t,a in ans.items() if a}

def morse_boundary(s):
    ans=defaultdict(int)
    for j in range(N):
        if s>>j&1:
            t=s^(1<<j)
            c=(-1)**((s&((1<<j)-1)).bit_count())
            for f,a in reduce_cell(t).items():ans[f]+=c*a
    return {t:a for t,a in ans.items() if a}
crit4=[s for s in final if s.bit_count()-1==4]
assert len(crit4)==1 and morse_boundary(crit4[0])=={}
print('SOURCE_GRAPH_VERTICES',N,'EDGES',sum(m.bit_count() for m in adj)//2)
print('FORBIDDEN_INDUCED_P3_TRIPLES',len(paths))
print('FACE_VECTOR_INCLUDING_EMPTY', [counts[i] for i in range(-1,8)])
print('NONEMPTY_CELLS',len(faces),'HASSE_INCIDENCES',num_edges)
print('INITIAL_MATCHED_PAIRS',len(initial_crit) and (len(faces)-len(initial_crit))//2)
print('INITIAL_CRITICAL', sorted(Counter(s.bit_count()-1 for s in initial_crit).items()))
for d,U,L,pathlen in steps:print('UNIQUE_PATH_CANCELLATION',d,'UPPER_MASK',U,'LOWER_MASK',L,'PATH_LENGTH',pathlen)
print('FINAL_MATCHED_PAIRS',len(matched_down))
print('FINAL_CRITICAL', sorted(Counter(s.bit_count()-1 for s in final).items()))
print('FINAL_4_BOUNDARY',morse_boundary(crit4[0]))
print('ALL_CHECKS_PASS')
