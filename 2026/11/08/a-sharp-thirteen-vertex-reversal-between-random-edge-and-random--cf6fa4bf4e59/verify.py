#!/usr/bin/env python3
"""Exact exhaustive tree comparison and infinite-spider identities; stdlib only."""
from functools import lru_cache
from itertools import permutations, product
from fractions import Fraction
from collections import deque

@lru_cache(None)
def code_rooted(adj, v, parent):
    subs=sorted(code_rooted(adj,w,v) for w in adj[v] if w!=parent)
    return '('+''.join(subs)+')'

def canonical(adj):
    n=len(adj)
    if n==1:return '()'
    deg=[len(v) for v in adj]
    leaves=[i for i,d in enumerate(deg) if d<=1]
    remain=n
    while remain>2:
        remain-=len(leaves)
        nxt=[]
        for v in leaves:
            deg[v]=0
            for w in adj[v]:
                if deg[w]>0:
                    deg[w]-=1
                    if deg[w]==1:nxt.append(w)
        leaves=nxt
    centers=leaves
    if len(centers)==1:return code_rooted(adj,centers[0],-1)
    a,b=centers
    ca=code_rooted(adj,a,b); cb=code_rooted(adj,b,a)
    return '('+min(ca,cb)+max(ca,cb)+')'

def extend(t):
    n=len(t)
    for v in range(n):
        adj=[list(ns) for ns in t]
        adj[v].append(n); adj.append([v]);
        yield tuple(tuple(sorted(ns)) for ns in adj)

def gen_trees_upto(maxn):
    level={canonical(((),)):((),)}
    yield 1,level
    for n in range(2,maxn+1):
        nextlevel={}
        for t in level.values():
            for candidate in extend(t):
                label=canonical(candidate)
                if label not in nextlevel:nextlevel[label]=candidate
        level=nextlevel
        yield n,level

@lru_cache(None)
def exact(rows, nD):
    """Two expected match sizes, vertex-iterative / edge-priority."""
    rows=tuple(sorted(r for r in rows if r))
    if not rows:return Fraction(0),Fraction(0)
    m=len(rows); E=sum(r.bit_count() for r in rows)
    V=Fraction(0); R=Fraction(0)
    for i,r in enumerate(rows):
        deg=r.bit_count()
        for j in range(nD):
            if (r>>j)&1:
                others=[]
                for ix,s in enumerate(rows):
                    if ix==i:continue
                    t=(s&((1<<j)-1)) | ((s>>(j+1))<<j)
                    if t:others.append(t)
                nxt_v,nxt_r=exact(tuple(sorted(others)),nD-1)
                V+=(1+nxt_v)/Fraction(m*deg)
                R+=(1+nxt_r)/Fraction(E)
    return V,R

def as_rows(tree,side):
    color=[None]*len(tree);color[0]=0
    queue=deque([0])
    while queue:
        u=queue.popleft()
        for v in tree[u]:
            if color[v] is None:color[v]=1-color[u];queue.append(v)
            else:assert color[v]!=color[u]
    J=[u for u in range(len(tree)) if color[u]==side]
    D=[u for u in range(len(tree)) if color[u]!=side]
    idx={u:i for i,u in enumerate(D)}
    rows=tuple(sorted(sum(1<<idx[v] for v in tree[u]) for u in J))
    return rows,len(D)

def independent_priority_checks():
    """Enumerate priority orders directly, without using the DP recurrences."""
    for m in (1, 2, 3):
        edges=[]
        for i in range(m):
            a,b,d=1+3*i,2+3*i,3+3*i
            edges.extend(((0,a),(a,b),(b,d)))
        fail=total=0
        for ordering in permutations(edges):
            used=set()
            for a,b in ordering:
                if a not in used and b not in used:
                    used.add(a); used.add(b)
            fail += (0 not in used)
            total += 1
        assert Fraction(fail,total)==Fraction(1,3**m)
    for m in (1, 2, 3, 4):
        # Independently enumerate: permutation of all jobs, local priority
        # at each arm job, and priority of neighbors at the center.
        fail=total=0
        for job_order in permutations(range(m+1)):
            for local_orders in product((0,1),repeat=m):
                for center_order in permutations(range(m)):
                    occupied=set(); center_matched=False
                    for job in job_order:
                        if job==0:
                            d=next((2*i for i in center_order if 2*i not in occupied),None)
                            if d is not None:
                                occupied.add(d); center_matched=True
                        else:
                            i=job-1
                            pair=(2*i,2*i+1) if local_orders[i]==0 else (2*i+1,2*i)
                            d=next((x for x in pair if x not in occupied),None)
                            assert d is not None
                            occupied.add(d)
                    fail += (not center_matched)
                    total += 1
        assert Fraction(fail,total)==Fraction(1,(m+1)*2**m)
    print('DIRECT_PRIORITY_ENUMERATION PASS: edges m<=3, jobs m<=4')

def run():
    known={1:1,2:1,3:1,4:2,5:3,6:6,7:11,8:23,9:47,10:106,11:235,12:551,13:1301}
    tot=0; rowsout=[]; first=[]
    for n,level in gen_trees_upto(13):
        assert len(level)==known[n],(n,len(level))
        nnegative=0; worst=Fraction(0)
        for tree in level.values():
            for side in (0,1):
                R,nd=as_rows(tree,side)
                V,E=exact(R,nd)
                d=E-V
                if d>0:
                    nnegative+=1
                    if d>worst:worst=d
                    first.append((n,d,canonical(tree),tree,side,R,nd,V,E))
        tot+=2*len(level)
        print(f'n={n:2} trees={len(level):4} oriented={2*len(level):4} edge_better={nnegative:3} max_edge_advantage={worst}',flush=True)
        rowsout.append((n,len(level),nnegative))
    assert first and first[0][0]==13
    assert len(first)==1
    n,d,c,tree,side,rows,nd,V,E=first[0]
    assert d==Fraction(1,6480),(d,V,E)
    assert V==Fraction(5,1)-Fraction(1,80)
    assert E==Fraction(5,1)-Fraction(1,81)
    print('FIRST_ORIENTATION',n,d,'V',V,'E',E,'rows',rows,'nD',nd,'code',c)
    print('DP_CACHE',exact.cache_info())
    for m in range(1,22):
        pV=Fraction(1,(m+1)*2**m)
        pE=Fraction(1,3**m)
        assert (pV>pE)==(m>=4)
        # exact DP on spiders m<=6
        if m<=6:
            cen=0
            tree=[[] for _ in range(1+3*m)]
            for i in range(m):
                x,y,z=1+3*i,2+3*i,3+3*i
                for a,b in ((0,x),(x,y),(y,z)):
                    tree[a].append(b);tree[b].append(a)
            rows,k=as_rows(tuple(tuple(v) for v in tree),0)
            V,E=exact(rows,k)
            assert V == m+1-pV,(m,V,m+1-pV)
            assert E == m+1-pE,(m,E,m+1-pE)
    independent_priority_checks()
    print('ALL_PASS checked',tot,'oriented pairs, infinite formula finite spot checks m<=6')

if __name__=='__main__':run()
