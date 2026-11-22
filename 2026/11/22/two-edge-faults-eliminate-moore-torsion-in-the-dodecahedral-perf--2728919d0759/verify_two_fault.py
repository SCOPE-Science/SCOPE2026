#!/usr/bin/env python3
"""Exact, dependency-free certificate for two-edge faults in GP(10,2)."""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

N = 20
V = range(N)
raw = []
for i in range(10):
    raw.extend([(i, (i+1)%10), (i, 10+i), (10+i, 10+(i+2)%10)])
EDGES = tuple(sorted(tuple(sorted(e)) for e in raw))
assert len(EDGES) == len(set(EDGES)) == 30
EDGE_ID = {e:i for i,e in enumerate(EDGES)}
ADJ = [set() for _ in V]
for a,b in EDGES:
    ADJ[a].add(b); ADJ[b].add(a)
assert all(len(n) == 3 for n in ADJ)

# Exhaustive edge-covering perfect-matchings enumeration.
def perfect_matchings():
    result = []
    def recur(covered,mask):
        if covered == (1<<N)-1:
            result.append(mask);return
        u = next(i for i in V if not (covered>>i)&1)
        for v in sorted(ADJ[u]):
            if not (covered>>v)&1:
                j = EDGE_ID[tuple(sorted((u,v)))]
                recur(covered | (1<<u) | (1<<v),mask | (1<<j))
    recur(0,0)
    assert len(result) == len(set(result)) == 36
    assert all(x.bit_count()==10 for x in result)
    return tuple(result)
MATCHINGS = perfect_matchings()

# Exhaustive adjacency-preserving vertex bijections, with exact pruning.
def automorphisms():
    out = []
    def visit(mapping,used):
        if len(mapping) == N:
            out.append(tuple(mapping[i] for i in V));return
        u = max((sum(w in mapping for w in ADJ[i]),i)
                for i in V if i not in mapping)[1]
        for v in V:
            if v in used: continue
            if all((w in ADJ[u])==(mapping[w] in ADJ[v]) for w in mapping):
                mapping[u]=v;used.add(v)
                visit(mapping,used)
                used.remove(v);del mapping[u]
    for v in V: visit({0:v},{v})
    assert len(out)==len(set(out))==120
    return out

def edge_pair_orbits():
    maps=[]
    for phi in automorphisms():
        maps.append(tuple(EDGE_ID[tuple(sorted((phi[a],phi[b])))] for a,b in EDGES))
    remaining=set(combinations(range(30),2)); orbs=[]
    while remaining:
        a,b=min(remaining)
        orb={tuple(sorted((perm[a],perm[b]))) for perm in maps}
        assert orb <= remaining
        remaining-=orb
        orbs.append(((a,b),orb))
    assert sum(map(lambda x:len(x[1]),orbs))==435
    assert sorted(len(orb) for _,orb in orbs)==[15]+[60]*7
    return orbs

def faces(fault):
    deleted=sum(1<<i for i in fault)
    facets=[m for m in MATCHINGS if not(m&deleted)]
    by_size=[set() for _ in range(11)]
    for facet in facets:
        sub=facet
        while sub:
            by_size[sub.bit_count()].add(sub)
            sub=(sub-1)&facet
    return facets,by_size

def bit_indices(x):
    while x:
        b=x&-x;yield b.bit_length()-1;x-=b

def boundary(x):
    return [(x^(1<<i), -1 if j&1 else 1)
            for j,i in enumerate(bit_indices(x))]

# Greedy full vertex-element matchings on successive residual face posets.
# This is the standard sequential element-matching construction.
def morse(fault):
    facets,graded=faces(fault)
    active=set().union(*graded[1:]) | {0}
    original=active.copy()
    pairs=[]
    while True:
        best=[]; best_vertex=None
        for v in range(30):
            bit=1<<v
            pp=[(x,x|bit) for x in active if not x&bit and (x|bit) in active]
            if len(pp)>len(best):best=pp;best_vertex=v
        if not best: break
        for a,b in best:
            assert a in active and b in active
            active.remove(a);active.remove(b)
        pairs.extend(best)
    assert len(active)+2*len(pairs)==len(original)
    return facets,graded,original,active,pairs

def check_dag(original,pairs):
    pairset=set(pairs)
    outgoing=defaultdict(list)
    indeg={x:0 for x in original}
    for upper in original:
        for lower,_ in boundary(upper):
            if (lower,upper) in pairset:
                a,b=lower,upper
            else:
                a,b=upper,lower
            outgoing[a].append(b);indeg[b]+=1
    queue=deque(x for x in original if indeg[x]==0)
    visited=0
    while queue:
        a=queue.popleft();visited+=1
        for b in outgoing[a]:
            indeg[b]-=1
            if indeg[b]==0:queue.append(b)
    assert visited==len(original),('cyclic_matching',visited,len(original))
    return visited

def morse_matrix(critical,pairs):
    lower={a:b for a,b in pairs}
    upper={b:a for a,b in pairs}
    c2=sorted(x for x in critical if x.bit_count()==3)
    c3=sorted(x for x in critical if x.bit_count()==4)
    assert all(x.bit_count() in (3,4) for x in critical)
    @lru_cache(None)
    def projection(x):
        if x in upper:return {}
        if x in critical:return {x:1}
        y=lower[x]
        by=boundary(y)
        eps=next(sign for face,sign in by if face==x)
        accum=defaultdict(int)
        for face,sign in by:
            if face==x:continue
            for z,v in projection(face).items():
                accum[z]-=eps*sign*v
        return {z:v for z,v in accum.items() if v}
    d=[]
    for c in c3:
        accum=defaultdict(int)
        for face,sign in boundary(c):
            for z,v in projection(face).items():
                accum[z]+=sign*v
        d.append([accum[x] for x in c2])
    return c2,c3,[list(row) for row in zip(*d)] if d else []

def rank_mod(rows,cols,p):
    pos={x:i for i,x in enumerate(rows)}
    pivots={};rank=0
    for col in cols:
        d={}
        for face,sign in boundary(col):
            k=pos[face];v=sign%p
            if v:d[k]=v
        while d:
            k=max(d)
            if k not in pivots:
                inv=pow(d[k],-1,p)
                pivots[k]={j:v*inv%p for j,v in d.items()}
                rank+=1;break
            z=d[k]
            for j,v in pivots[k].items():
                t=(d.get(j,0)-z*v)%p
                if t:d[j]=t
                elif j in d:del d[j]
    return rank

def rank_small_mod(matrix,p):
    if not matrix:return 0
    a=[[(v%p) for v in row] for row in matrix]
    R=len(a);C=len(a[0]);i=0
    for j in range(C):
        ii=next((k for k in range(i,R) if a[k][j]),None)
        if ii is None:continue
        a[i],a[ii]=a[ii],a[i]
        inv=pow(a[i][j],-1,p)
        a[i]=[(v*inv)%p for v in a[i]]
        for k in range(R):
            if k==i or not a[k][j]: continue
            z=a[k][j]
            a[k]=[(x-z*y)%p for x,y in zip(a[k],a[i])]
        i+=1
        if i==R:break
    return i

def main():
    orbs=edge_pair_orbits()
    print('20 vertices; 30 edges; 36 perfect matchings; 120 automorphisms; 435 edge-pairs; 8 orbits')
    for (a,b),orb in orbs:
        fac,graded,original,critical,pairs=morse((a,b))
        dag=check_dag(original,pairs)
        c2,c3,d3=morse_matrix(critical,pairs)
        r2=rank_mod(sorted(graded[2]),sorted(graded[3]),2)
        r3_2=rank_mod(sorted(graded[3]),sorted(graded[4]),2)
        r3_3=rank_mod(sorted(graded[3]),sorted(graded[4]),3)
        beta2_2=len(graded[3])-r2-r3_2
        beta2_3=len(graded[3])-r2-r3_3
        assert beta2_2==len(c2)-rank_small_mod(d3,2)
        assert beta2_3==len(c2)-rank_small_mod(d3,3)
        assert all(len(row)==len(c3) for row in d3)
        print(f'pair=({a},{b}) edges=({EDGES[a]},{EDGES[b]}) orbit={len(orb)} '
              f'facets={len(fac)} faceposet={dag} crit=({len(c2)},{len(c3)}) '
              f'Morse_D3={d3} H2mod2={beta2_2} H2mod3={beta2_3}')
    print('PASS: exact combinatorial and integral Morse certificates')
if __name__=='__main__':main()
