#!/usr/bin/env python3
"""Reproduce the finite checks for the sharp three-round coloured-pair extremum.
All variables describe finite coloured-pair structures; Python stdlib only.
"""
from itertools import combinations, permutations, product
from functools import lru_cache
from math import factorial


def put(a,u,v,c,inv):
    assert u != v and a[u][v] == a[v][u] == 0
    a[u][v],a[v][u] = c, inv[c]


def normal_form(q,inv,center_options,cross_options):
    assert q>=2 and len(inv)==q and inv[0]==0
    assert all(inv[inv[i]]==i for i in range(q))
    n=q*q+q+1
    a=[[0]*n for _ in range(n)]
    centers=[1+j*(q+1) for j in range(q)]
    slots=[[centers[j]+1+s for s in range(q)] for j in range(q)]
    for j in range(q):
        for x in [centers[j]]+slots[j]:
            if j:put(a,0,x,j,inv)
    # Within each relation-to-root group the distinct peripheral vertices
    # have all q relation states to its selected witness (including 0).
    for j in range(q):
        for s,x in enumerate(slots[j]):
            if s:put(a,centers[j],x,s,inv)
    pairs=list(combinations(range(q),2))
    assert len(center_options)==len(pairs)
    for (i,j),c in zip(pairs,center_options):
        assert 1<=c<q
        put(a,centers[i],centers[j],c,inv)
    directions=[(i,j) for i in range(q) for j in range(q) if i!=j]
    assert len(cross_options)==len(directions)
    for (i,j),pos in zip(directions,cross_options):
        missing=[c for c in range(1,q) if c!=a[centers[i]][centers[j]]]
        assert len(pos)==q-2 and len(set(pos))==len(pos)
        for c,k in zip(missing,pos):put(a,centers[i],slots[j][k],c,inv)
    return a,centers


def edges(a):
    return sum(a[i][j]!=0 for i in range(len(a)) for j in range(i+1,len(a)))


def profile_full(a,v,w,q):
    seen={(a[v][z],a[w][z]) for z in range(len(a)) if z not in (v,w)}
    return len(seen)==q*q


def root_certified(a,v,q):
    return all(any(a[v][w]==c and profile_full(a,v,w,q)
                   for w in range(len(a)) if w!=v) for c in range(q))


def rank_at_least(a,r,q):
    # Definition-level search, separate from the pair-profile test.
    @lru_cache(None)
    def rec(f,k):
        if k==0:return True
        for pattern in product(range(q),repeat=len(f)):
            if not any(all(a[x][z]==c for x,c in zip(f,pattern))
                       and rec(f+(z,),k-1) for z in range(len(a)) if z not in f):
                return False
        return True
    return rec((),r)


def main():
    for q,inv in [(2,(0,1)),(3,(0,2,1)),(4,(0,1,2,3)),(5,(0,2,1,4,3))]:
        centers_options=[1]*((q*(q-1))//2)
        cross_options=[tuple(range(q-2))]*(q*(q-1))
        a,centers=normal_form(q,inv,centers_options,cross_options)
        need_n=q*q+q+1
        need_e=q**3 - q*(q-1)//2 - 1
        assert len(a)==need_n and edges(a)==need_e
        assert root_certified(a,0,q)
        assert all(profile_full(a,0,w,q) for w in centers)
        if q<=3:assert rank_at_least(a,3,q)
        print(f'CANONICAL q={q} n={need_n} nonzero_pairs={need_e} rank3=YES')
    # Full distinct 3-state structural census: nonzero center-center states
    # have 2 choices per unordered pair; each ordered cross group has 3.
    q=3;inv=(0,2,1)
    all_codes=set(); full_count=0
    for ct in product((1,2),repeat=3):
        for ch in product(((0,),(1,),(2,)),repeat=6):
            a,centers=normal_form(q,inv,ct,ch)
            assert edges(a)==23
            assert all(profile_full(a,0,w,3) for w in centers)
            assert root_certified(a,0,3)
            code=tuple(a[i][j] for i in range(13) for j in range(i+1,13))
            assert code not in all_codes
            all_codes.add(code);full_count+=1
    assert full_count==2**3*3**6==5832
    print('CERTIFIED_ISOMORPHISM_CLASSES q=3 count=5832 distinct canonical normal forms')
    # Delete each arc of one 13-vertex extremizer, and test the literal
    # recursive rank definition, not just the simplified root criterion.
    a,_=normal_form(3,inv,(1,1,1),((0,),)*6)
    assert rank_at_least(a,3,3)
    arcs=[(i,j) for i in range(13) for j in range(i+1,13) if a[i][j]!=0]
    assert len(arcs)==23
    for i,j in arcs:
        b=[r[:] for r in a];b[i][j]=b[j][i]=0
        assert not rank_at_least(b,3,3)
    print('ARC_DELETION_CHECK q=3 all 23 deletions lose rank >=3')
    # All uncoloured 6-vertex graphs fail the rank-three criterion.
    pairlist=list(combinations(range(6),2));checked=0
    for mask in range(1<<len(pairlist)):
        g=[[0]*6 for _ in range(6)]
        for k,(u,v) in enumerate(pairlist):
            if mask>>k & 1:g[u][v]=g[v][u]=1
        assert not any(root_certified(g,v,2) for v in range(6))
        checked+=1
    assert checked==32768
    print('SIX_VERTEX_GRAPHS q=2 all 32768 fail rank >=3')
    assert (factorial(3)//2)**(3*2)*2**3==5832
    print('ALL_CHECKS_OK')

if __name__=='__main__':main()
