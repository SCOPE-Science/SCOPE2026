#!/usr/bin/env python3
"""Exact, standard-library check of a multipath-complex integral homology calculation.
The graph, face predicates, Morse matchings, acyclicity tests, and integer
boundary computations are constructed independently from explicit definitions.
"""
from collections import Counter,defaultdict,deque
from functools import lru_cache
from itertools import combinations
from hashlib import sha256
import json

VERTICES=list(combinations(range(5),2))
EDGES=tuple((a,b) for a in range(10) for b in range(a+1,10)
            if set(VERTICES[a]).isdisjoint(VERTICES[b]))
ARCS=tuple(sorted([(u,v) for u,v in EDGES]+[(v,u) for u,v in EDGES]))
assert len(EDGES)==15 and len(ARCS)==30


def enumerate_dfs():
    """Complete enumeration: add arcs in increasing index, rejecting local degree/cycle violations."""
    nxt=[-1]*10; prev=[-1]*10
    result=[]
    def visit(start,mask):
        result.append(mask)
        for a in range(start,30):
            u,v=ARCS[a]
            if nxt[u]!=-1 or prev[v]!=-1:
                continue
            w=v
            while w!=-1 and w!=u:
                w=nxt[w]
            if w==u:
                continue
            nxt[u]=v;prev[v]=u
            visit(a+1,mask|(1<<a))
            nxt[u]=-1;prev[v]=-1
    visit(0,0)
    return sorted(result)


def valid_graph(mask):
    """Separate check: indegrees/outdegrees and full directed topological sort."""
    out=[0]*10; indeg=[0]*10; adj=[[] for _ in range(10)]
    while mask:
        bit=mask&-mask;mask-=bit
        u,v=ARCS[bit.bit_length()-1]
        out[u]+=1;indeg[v]+=1
        if out[u]>1 or indeg[v]>1:return False
        adj[u].append(v)
    q=deque(v for v in range(10) if indeg[v]==0)
    reached=0
    while q:
        u=q.popleft();reached+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    return reached==10


def enumerate_dynamic():
    """Independent full enumeration by 30 successive binary include/exclude stages."""
    current=[0]
    for a in range(30):
        extra=[f|(1<<a) for f in current if valid_graph(f|(1<<a))]
        current+=extra
    return sorted(current)


def toggles(faces,order):
    """Iterated elementary matchings along arc coordinates."""
    allfaces=set(faces)
    paired={}
    for arc in order:
        bit=1<<arc
        for s in faces:
            if s & bit or s in paired:continue
            t=s|bit
            if t in allfaces and t not in paired:
                paired[s]=t;paired[t]=s
    critical=tuple(s for s in faces if s not in paired)
    assert len(paired)+len(critical)==len(faces)
    return paired,critical


def acyclic_hasse(faces,paired):
    """Exact topological sort of the oriented Hasse graph, no sampling."""
    idx={m:i for i,m in enumerate(faces)}
    forward=[[] for _ in faces]
    indeg=[0]*len(faces)
    incidences=0
    for f in faces:
        high=idx[f]
        bits=f
        while bits:
            b=bits&-bits;bits-=b
            low=idx[f^b]
            if paired.get(f^b)==f:
                x,y=low,high
            else:
                x,y=high,low
            forward[x].append(y)
            indeg[y]+=1;incidences+=1
    que=deque(i for i,d in enumerate(indeg) if d==0)
    finished=0
    while que:
        u=que.popleft();finished+=1
        for v in forward[u]:
            indeg[v]-=1
            if indeg[v]==0:que.append(v)
    assert finished==len(faces),('cycle',finished,len(faces))
    return incidences


def make_morse(critical,paired):
    by_degree={d:tuple(x for x in critical if x.bit_count()-1==d)
               for d in range(-1,10)}
    @lru_cache(maxsize=None)
    def projection(face):
        if face not in paired:return {face:1}
        mate=paired[face]
        if mate.bit_count()<face.bit_count():return {}
        chosen=(mate^face).bit_length()-1
        eps=(-1)**((mate & ((1<<chosen)-1)).bit_count())
        ans=defaultdict(int)
        b=mate
        while b:
            bit=b&-b;b-=bit
            if bit.bit_length()-1==chosen:continue
            sign=(-1)**((mate & (bit-1)).bit_count())
            for q,c in projection(mate^bit).items():
                ans[q]-=eps*sign*c
        return {i:x for i,x in ans.items() if x}
    boundaries={}
    for dim in range(0,10):
        cols=by_degree[dim];rows=by_degree[dim-1]
        if not cols or not rows:continue
        pos={f:i for i,f in enumerate(rows)}
        mat=[[0 for _ in cols] for _ in rows]
        for j,f in enumerate(cols):
            bits=f
            while bits:
                bit=bits&-bits;bits-=bit
                sign=(-1)**((f & (bit-1)).bit_count())
                for target,val in projection(f^bit).items():
                    mat[pos[target]][j]+=sign*val
        boundaries[dim]=mat
    return by_degree,boundaries,projection.cache_info()


def integer_unit_rank(src):
    """Exact integral unit-pivot reduction by unimodular row/column operations.
    Reaching zero remainder after only unit pivots gives the integral SNF
    as a sequence of 1's and 0's; no external CAS is assumed.
    """
    mat=[list(row) for row in src]
    n=len(mat);m=len(mat[0]) if n else 0
    k=0;max_abs=0
    while k<min(n,m):
        pivot=next(((i,j) for i in range(k,n) for j in range(k,m)
                    if abs(mat[i][j])==1),None)
        if pivot is None:break
        i,j=pivot
        mat[i],mat[k]=mat[k],mat[i]
        for row in mat:
            row[j],row[k]=row[k],row[j]
        s=mat[k][k]
        # eliminate column: integer elementary row operations
        for i in range(k+1,n):
            t=mat[i][k]//s
            if t:
                for j in range(k,m):mat[i][j]-=t*mat[k][j]
        # eliminate row: integer elementary column operations
        for j in range(k+1,m):
            t=mat[k][j]//s
            if t:
                for i in range(k,n):mat[i][j]-=t*mat[i][k]
        assert all(mat[i][k]==0 for i in range(k+1,n))
        assert all(mat[k][j]==0 for j in range(k+1,m))
        k+=1
    leftover=[mat[i][j] for i in range(k,n) for j in range(k,m)]
    max_abs=max(map(abs,leftover),default=0)
    assert max_abs==0,('incomplete-unit-reduction',max_abs,k,(n,m))
    return k


def verify_chain(boundaries,by_degree):
    for d in range(1,10):
        if d not in boundaries or d+1 not in boundaries:continue
        a=boundaries[d];b=boundaries[d+1]
        assert len(a[0])==len(b)
        for i in range(len(a)):
            for j in range(len(b[0])):
                assert sum(a[i][k]*b[k][j] for k in range(len(b)))==0


def direct_mod2(faces):
    """Independent unreduced simplicial ranks over F_2 using bit-vector elimination."""
    groups={d:[] for d in range(-1,10)}
    for f in faces:groups[f.bit_count()-1].append(f)
    ranks={}
    for d in range(0,10):
        lows=groups[d-1];ups=groups[d]
        if not lows or not ups:continue
        ind={f:i for i,f in enumerate(lows)}
        basis={}
        for f in ups:
            bitvec=0;bits=f
            while bits:
                bit=bits&-bits;bits-=bit
                bitvec^=1<<ind[f^bit]
            while bitvec:
                pivot=bitvec.bit_length()-1
                if pivot not in basis:
                    basis[pivot]=bitvec;break
                bitvec^=basis[pivot]
        ranks[d]=len(basis)
    return ranks,groups


def main():
    faces=enumerate_dfs();other=enumerate_dynamic()
    assert faces==other
    assert len(faces)==59203
    count=Counter(f.bit_count()-1 for f in faces)
    assert [count[d] for d in range(-1,9)]==[1,30,360,2240,7860,15912,18280,11160,3120,240]
    print('Graph: Petersen KG(5,2), vertices=10 undirected_edges=15 directed_arcs=30')
    print('Complete face enumerations agree:',len(faces),'including the empty face')
    print('Face counts by dimension:',dict(sorted(count.items())))
    for name,order in [('ascending',range(30)),('descending',range(29,-1,-1))]:
        pairing,critical=toggles(faces,order)
        incidences=acyclic_hasse(faces,pairing)
        groups,boundaries,cache=make_morse(critical,pairing)
        verify_chain(boundaries,groups)
        ranks={d:integer_unit_rank(m) for d,m in boundaries.items()}
        betti={d:len(groups[d])-ranks.get(d,0)-ranks.get(d+1,0)
               for d in range(3,9) if groups[d]}
        assert betti=={3:0,4:12,5:1,6:44,7:94}
        print(name,'matched_pairs=',len(pairing)//2,'Hasse incidences=',incidences)
        print(name,'critical cell counts:',{d:len(x) for d,x in groups.items() if x})
        print(name,'integer unit-pivot boundary ranks:',ranks)
        print(name,'reduced integral Betti numbers:',{d:b for d,b in betti.items() if b})
    direct_ranks,direct_groups=direct_mod2(faces)
    direct_betti={d:len(direct_groups[d])-direct_ranks.get(d,0)-direct_ranks.get(d+1,0)
                  for d in range(0,9)}
    assert {d:b for d,b in direct_betti.items() if b}=={4:12,5:1,6:44,7:94}
    print('Independent unreduced F2 ranks:',direct_ranks)
    print('Independent unreduced F2 Betti numbers:',{d:b for d,b in direct_betti.items() if b})
    euler=sum((-1)**d*len(g) for d,g in direct_groups.items())
    assert euler==12-1+44-94==-39
    print('Reduced Euler characteristic:',euler)
    print('PETERSEN_BIDIRECTED_MULTIPATH_INTEGRAL_HOMOLOGY_PASS')
if __name__=='__main__':main()
